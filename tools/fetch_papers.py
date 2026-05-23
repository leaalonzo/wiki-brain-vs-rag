"""
Fetch open-access research papers from Semantic Scholar and ingest them into raw/.

Pipeline per query (from tools/queries.yaml):
  1. Search Semantic Scholar API → top 10 results
  2. Filter for papers with an open-access PDF URL
  3. Download PDF  → raw/pdfs/<sanitized_title>.pdf
  4. Convert PDF   → Markdown via pymupdf4llm
  5. Prepend YAML frontmatter (title, authors, year, abstract, urls, query_tag)
  6. Save Markdown → raw/<sanitized_title>.md
  7. Update        → raw/_manifest.json

Usage:
    python -m tools.fetch_papers
    python -m tools.fetch_papers --tag rag_retrieval
    python -m tools.fetch_papers --dry-run
    python -m tools.fetch_papers --queries tools/queries.yaml --limit 5
"""

import json
import logging
import os
import re
import time
from datetime import datetime, UTC
from pathlib import Path

import click
import requests
import yaml
from dotenv import load_dotenv

load_dotenv()

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
PDF_DIR = RAW_DIR / "pdfs"
MANIFEST_PATH = RAW_DIR / "_manifest.json"
LOG_PATH = ROOT / "tools" / "fetch.log"
DEFAULT_QUERIES = ROOT / "tools" / "queries.yaml"

# ── Semantic Scholar ─────────────────────────────────────────────────────────
S2_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_FIELDS = "title,authors,year,abstract,openAccessPdf,externalIds,url"
S2_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")

# ── Rate limiting ────────────────────────────────────────────────────────────
# Without API key: ~100 req/5 min (≈1 req/3 s). With key: up to 10 req/s.
REQUEST_DELAY = 3.5 if not S2_API_KEY else 0.15
MAX_RETRIES = 4
BACKOFF_BASE = 5.0   # seconds; doubles on each retry → 5, 10, 20, 40 s


# ── Logging ──────────────────────────────────────────────────────────────────

def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("fetch_papers")
    logger.setLevel(logging.DEBUG)

    fmt = logging.Formatter("%(asctime)s  %(levelname)-8s  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    fh = logging.FileHandler(LOG_PATH, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


log = setup_logging()


# ── Helpers ───────────────────────────────────────────────────────────────────

def sanitize_filename(title: str, max_len: int = 80) -> str:
    """Convert an arbitrary title into a safe, lowercase filename stem."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "_", slug).strip("_-")
    return slug[:max_len]


def build_frontmatter(meta: dict) -> str:
    """Render a YAML frontmatter block from a metadata dict."""
    block = {
        "title": meta.get("title", ""),
        "authors": meta.get("authors", []),
        "year": meta.get("year"),
        "abstract": meta.get("abstract", ""),
        "source_url": meta.get("source_url", ""),
        "pdf_url": meta.get("pdf_url", ""),
        "doi": meta.get("doi", ""),
        "semantic_scholar_id": meta.get("paper_id", ""),
        "query_tag": meta.get("query_tag", ""),
        "fetched_at": meta.get("fetched_at", ""),
    }
    return "---\n" + yaml.dump(block, allow_unicode=True, sort_keys=False) + "---\n\n"


def load_manifest() -> dict:
    """Load existing manifest or return empty structure."""
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"fetched_at": None, "documents": []}


def save_manifest(manifest: dict) -> None:
    manifest["fetched_at"] = datetime.now(UTC).isoformat()
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


def already_fetched(manifest: dict, paper_id: str) -> bool:
    return any(d.get("paper_id") == paper_id for d in manifest["documents"])


def s2_request(params: dict, retries: int = MAX_RETRIES) -> dict | None:
    """
    GET the Semantic Scholar API with exponential back-off on 429 / 5xx.
    Returns parsed JSON or None on permanent failure.
    """
    headers = {}
    if S2_API_KEY:
        headers["x-api-key"] = S2_API_KEY

    for attempt in range(retries):
        try:
            resp = requests.get(S2_SEARCH_URL, params=params, headers=headers, timeout=20)
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code == 429:
                wait = BACKOFF_BASE ** attempt
                log.warning("Rate limited (429). Waiting %.1fs before retry %d/%d.", wait, attempt + 1, retries)
                time.sleep(wait)
                continue
            if resp.status_code >= 500:
                wait = BACKOFF_BASE ** attempt
                log.warning("Server error %d. Waiting %.1fs before retry %d/%d.", resp.status_code, wait, attempt + 1, retries)
                time.sleep(wait)
                continue
            log.error("Semantic Scholar returned %d for params %s", resp.status_code, params)
            return None
        except requests.RequestException as exc:
            wait = BACKOFF_BASE ** attempt
            log.warning("Request error: %s. Retrying in %.1fs (%d/%d).", exc, wait, attempt + 1, retries)
            time.sleep(wait)

    log.error("All %d retries exhausted for params %s", retries, params)
    return None


def search_papers(query: str, limit: int = 10) -> list[dict]:
    """Search Semantic Scholar and return raw paper dicts."""
    log.debug("Searching: %r (limit=%d)", query, limit)
    data = s2_request({"query": query, "limit": limit, "fields": S2_FIELDS})
    if not data:
        return []
    papers = data.get("data", [])
    log.debug("  → %d results returned.", len(papers))
    return papers


def filter_open_access(papers: list[dict]) -> list[dict]:
    """Keep only papers that have an openAccessPdf URL."""
    oa = [p for p in papers if p.get("openAccessPdf") and p["openAccessPdf"].get("url")]
    log.debug("  %d / %d papers have open-access PDFs.", len(oa), len(papers))
    return oa


def download_pdf(url: str, dest: Path, retries: int = MAX_RETRIES) -> bool:
    """Download a PDF to dest. Returns True on success."""
    if dest.exists():
        log.debug("  PDF already on disk: %s", dest.name)
        return True

    for attempt in range(retries):
        try:
            log.debug("  Downloading PDF (attempt %d): %s", attempt + 1, url)
            resp = requests.get(url, timeout=60, stream=True)
            if resp.status_code == 200:
                dest.write_bytes(resp.content)
                log.info("  Downloaded: %s (%.1f KB)", dest.name, len(resp.content) / 1024)
                return True
            if resp.status_code == 429:
                wait = BACKOFF_BASE ** attempt
                log.warning("  PDF download rate-limited. Waiting %.1fs.", wait)
                time.sleep(wait)
                continue
            log.error("  PDF download failed with HTTP %d: %s", resp.status_code, url)
            return False
        except requests.RequestException as exc:
            wait = BACKOFF_BASE ** attempt
            log.warning("  PDF download error: %s. Retrying in %.1fs.", exc, wait)
            time.sleep(wait)

    log.error("  PDF download exhausted retries: %s", url)
    return False


def pdf_to_md(pdf_path: Path) -> str | None:
    """Convert a PDF to Markdown using pymupdf4llm. Returns None on failure."""
    try:
        import pymupdf4llm
        return pymupdf4llm.to_markdown(str(pdf_path))
    except Exception as exc:
        log.error("  pymupdf4llm conversion failed for %s: %s", pdf_path.name, exc)
        return None


def extract_meta(paper: dict, query_tag: str) -> dict:
    """Flatten a Semantic Scholar paper dict into a clean metadata dict."""
    authors = [a.get("name", "") for a in (paper.get("authors") or [])]
    external_ids = paper.get("externalIds") or {}
    oa_pdf = paper.get("openAccessPdf") or {}
    return {
        "paper_id": paper.get("paperId", ""),
        "title": paper.get("title", "Untitled"),
        "authors": authors,
        "year": paper.get("year"),
        "abstract": (paper.get("abstract") or "").strip(),
        "source_url": paper.get("url", ""),
        "pdf_url": oa_pdf.get("url", ""),
        "doi": external_ids.get("DOI", ""),
        "query_tag": query_tag,
        "fetched_at": datetime.now(UTC).isoformat(),
    }


def process_paper(meta: dict, dry_run: bool) -> dict | None:
    """
    Download, convert, and write one paper. Returns manifest entry or None.
    """
    slug = sanitize_filename(meta["title"])
    pdf_path = PDF_DIR / f"{slug}.pdf"
    md_path = RAW_DIR / f"{slug}.md"

    log.info("Processing: %s", meta["title"][:70])

    if dry_run:
        log.info("  [DRY RUN] Would download %s → %s", meta["pdf_url"], pdf_path.name)
        return {**meta, "pdf_path": str(pdf_path), "md_path": str(md_path)}

    # Download PDF
    ok = download_pdf(meta["pdf_url"], pdf_path)
    if not ok:
        return None

    # Convert to Markdown
    md_text = pdf_to_md(pdf_path)
    if md_text is None:
        return None

    # Write .md with frontmatter
    full_md = build_frontmatter(meta) + md_text
    md_path.write_text(full_md, encoding="utf-8")
    log.info("  Saved Markdown: %s (%.1f KB)", md_path.name, len(full_md) / 1024)

    return {**meta, "pdf_path": str(pdf_path.relative_to(ROOT)), "md_path": str(md_path.relative_to(ROOT))}


# ── CLI ──────────────────────────────────────────────────────────────────────

@click.command()
@click.option("--queries", "queries_file", default=str(DEFAULT_QUERIES), show_default=True,
              help="Path to queries YAML file.")
@click.option("--tag", default=None, help="Only run the query with this tag.")
@click.option("--limit", default=20, show_default=True, help="Max results per query.")
@click.option("--dry-run", is_flag=True, help="Search and log without downloading anything.")
@click.option("--force", is_flag=True, help="Re-download papers already in the manifest.")
def main(queries_file: str, tag: str | None, limit: int, dry_run: bool, force: bool) -> None:
    """Fetch open-access papers from Semantic Scholar into raw/."""
    queries_path = Path(queries_file)
    if not queries_path.exists():
        log.error("Queries file not found: %s", queries_path)
        raise SystemExit(1)

    config = yaml.safe_load(queries_path.read_text(encoding="utf-8"))
    queries: list[dict] = config.get("queries", [])

    if tag:
        queries = [q for q in queries if q.get("tag") == tag]
        if not queries:
            log.error("No query found with tag %r", tag)
            raise SystemExit(1)

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    if force:
        manifest["documents"] = []

    total_fetched = 0
    total_skipped = 0

    for entry in queries:
        q_tag = entry.get("tag", "untagged")
        q_text = entry.get("query", "")
        log.info("=== Query [%s]: %r ===", q_tag, q_text)

        papers = search_papers(q_text, limit=limit)

        oa_papers = filter_open_access(papers)
        if not oa_papers:
            log.warning("  No open-access papers found for tag [%s]. Cooling down 15 s.", q_tag)
            time.sleep(15)   # bucket recovery after failed/empty query
            continue

        time.sleep(REQUEST_DELAY)

        for paper in oa_papers:
            meta = extract_meta(paper, q_tag)

            if not force and already_fetched(manifest, meta["paper_id"]):
                log.debug("  Already in manifest, skipping: %s", meta["title"][:60])
                total_skipped += 1
                continue

            result = process_paper(meta, dry_run=dry_run)
            if result:
                if not dry_run:
                    manifest["documents"].append(result)
                    save_manifest(manifest)
                total_fetched += 1

            time.sleep(REQUEST_DELAY)

    log.info(
        "Done. Fetched: %d  |  Skipped (already indexed): %d  |  Manifest: %s",
        total_fetched,
        total_skipped,
        MANIFEST_PATH if not dry_run else "not written (dry-run)",
    )


if __name__ == "__main__":
    main()
