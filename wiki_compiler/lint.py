"""
Wiki health linter — Phase 2c.

Checks:
  1. Consistency : contradictory claims across concept articles (gpt-4o)
  2. Coverage    : concept tags in summaries but missing from wiki/concepts/ (regex)
  3. Orphans     : summaries not cited by any concept article (regex)
  4. Gap finder  : suggest 3-5 new concept articles to write (gpt-4o)
  5. Imputation  : fill missing abstracts in raw/ from Semantic Scholar

Writes wiki/_lint_report.md after every run.

Usage:
    python -m wiki_compiler.lint
    python -m wiki_compiler.lint --fix    # also run imputation + auto-repair
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

import click
import requests
import yaml
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

WIKI_DIR = Path("wiki")
CONCEPTS_DIR = WIKI_DIR / "concepts"
SUMMARIES_DIR = WIKI_DIR / "summaries"
RAW_DIR = Path("raw")
LINT_REPORT = WIKI_DIR / "_lint_report.md"

LINT_MODEL = os.getenv("LINT_MODEL", "gpt-4o")
S2_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")


# ── Frontmatter helpers ───────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (metadata_dict, body) for a file with YAML frontmatter."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    try:
        meta = yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        meta = {}
    body = text[end + 4:].lstrip()
    return meta, body


def write_frontmatter(path: Path, meta: dict, body: str) -> None:
    path.write_text(
        "---\n" + yaml.dump(meta, allow_unicode=True, sort_keys=False) + "---\n\n" + body,
        encoding="utf-8",
    )


# ── Concept tag parsing (shared with compile.py) ─────────────────────────────

def parse_concept_tags(summary_text: str) -> list[str]:
    match = re.search(r"## Concepts[^\n]*\n(.*?)(?=\n##|\Z)", summary_text, re.DOTALL)
    if not match:
        return []
    content = match.group(1).strip()
    return [t.strip().strip("-").strip() for t in re.split(r"[,\n]", content) if t.strip().strip("-").strip()]


def concept_slug(name: str) -> str:
    # Strip parenthetical abbreviations like "(LLMs)" or "(RAG)" before slugging
    name = re.sub(r"\s*\([^)]*\)", "", name)
    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "_", slug).strip("_-")
    # Normalize common plural/singular variants
    slug = re.sub(r"_llms?$", "_llm", slug)
    return slug


# ── Check 1: Consistency ──────────────────────────────────────────────────────

def check_consistency(client: OpenAI) -> list[str]:
    """Ask gpt-4o to find contradictory claims across concept articles."""
    concept_files = sorted(CONCEPTS_DIR.glob("*.md"))
    if len(concept_files) < 2:
        return []

    # Condense each article to its Definition + Key Mechanisms sections only
    snippets = []
    for cf in concept_files:
        text = cf.read_text(encoding="utf-8")
        # Keep first 600 chars — enough to catch definitional contradictions
        snippets.append(f"### {cf.stem}\n{text[:600]}")

    combined = "\n\n".join(snippets)

    response = client.chat.completions.create(
        model=LINT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a wiki quality reviewer checking for logical consistency.",
            },
            {
                "role": "user",
                "content": (
                    "Review these concept article excerpts and identify any pairs that make "
                    "contradictory or mutually inconsistent claims. For each contradiction, "
                    "name the two articles and describe the conflict in one sentence.\n\n"
                    "Return a JSON object: {\"contradictions\": [{\"articles\": [\"a\", \"b\"], "
                    "\"description\": \"...\"}]}. If none, return {\"contradictions\": []}.\n\n"
                    f"{combined[:14000]}"
                ),
            },
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    try:
        data = json.loads(response.choices[0].message.content)
        findings = []
        for c in data.get("contradictions", []):
            arts = " vs ".join(c.get("articles", []))
            findings.append(f"**{arts}**: {c.get('description', '')}")
        return findings
    except (json.JSONDecodeError, KeyError):
        return []


# ── Check 2: Coverage ─────────────────────────────────────────────────────────

def check_coverage() -> list[str]:
    """Find concept tags mentioned in summaries but with no concept article."""
    existing_slugs = {p.stem for p in CONCEPTS_DIR.glob("*.md")}
    missing: dict[str, list[str]] = {}  # slug → [summary names that mention it]

    for sf in SUMMARIES_DIR.glob("*.md"):
        text = sf.read_text(encoding="utf-8")
        for tag in parse_concept_tags(text):
            slug = concept_slug(tag)
            if slug not in existing_slugs:
                missing.setdefault(slug, []).append(sf.stem)

    return [
        f"`{slug}` — mentioned in: {', '.join(sources[:3])}{'...' if len(sources) > 3 else ''}"
        for slug, sources in sorted(missing.items())
    ]


# ── Check 3: Orphans ──────────────────────────────────────────────────────────

def _summary_keywords(stem: str) -> list[str]:
    """Extract 2-3 meaningful words from a summary filename stem to use for matching."""
    # Remove common stopwords from the slug
    stopwords = {"the", "a", "an", "of", "for", "in", "on", "and", "via", "from",
                 "with", "to", "by", "its", "are", "is", "as", "at", "be", "or"}
    words = [w for w in stem.replace("-", "_").split("_") if len(w) > 3 and w not in stopwords]
    # Return the first 3 meaningful words — enough to identify the paper
    return words[:3]


def check_orphans() -> list[str]:
    """Find summaries not referenced by any concept article.

    Matches by significant words from the filename (not the exact slug) to avoid
    false positives when concept articles cite papers by title rather than slug.
    """
    all_concept_text = " ".join(
        cf.read_text(encoding="utf-8").lower()
        for cf in CONCEPTS_DIR.glob("*.md")
    )

    orphans = []
    for sf in SUMMARIES_DIR.glob("*.md"):
        keywords = _summary_keywords(sf.stem)
        # Orphan only if NONE of its meaningful keywords appear in any concept article
        if keywords and not any(kw in all_concept_text for kw in keywords):
            orphans.append(sf.stem)

    return sorted(orphans)


# ── Check 4: Gap Finder ───────────────────────────────────────────────────────

def check_gaps(client: OpenAI) -> list[str]:
    """Ask gpt-4o to suggest 3-5 missing concept articles."""
    existing_concepts = sorted(p.stem for p in CONCEPTS_DIR.glob("*.md"))
    existing_summaries = sorted(p.stem for p in SUMMARIES_DIR.glob("*.md"))

    if not existing_concepts and not existing_summaries:
        return []

    concepts_list = "\n".join(f"- {c}" for c in existing_concepts)
    summaries_list = "\n".join(f"- {s}" for s in existing_summaries)

    response = client.chat.completions.create(
        model=LINT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a knowledge base curator for a wiki on cognitive science and learning.",
            },
            {
                "role": "user",
                "content": (
                    "Given the concept articles and source summaries already in this wiki, "
                    "suggest 3-5 concept articles that are clearly missing but would add "
                    "significant value. Prioritize foundational concepts that would connect "
                    "many existing articles.\n\n"
                    f"Existing concept articles:\n{concepts_list}\n\n"
                    f"Source summaries:\n{summaries_list}\n\n"
                    "Return a JSON object: {\"suggestions\": [{\"concept\": \"...\", "
                    "\"reason\": \"one sentence\"}]}"
                ),
            },
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )
    try:
        data = json.loads(response.choices[0].message.content)
        return [
            f"**{s['concept']}** — {s.get('reason', '')}"
            for s in data.get("suggestions", [])
        ]
    except (json.JSONDecodeError, KeyError):
        return []


# ── Check 5: Imputation ───────────────────────────────────────────────────────

def s2_fetch_abstract(title: str) -> str | None:
    """Search Semantic Scholar for a paper title and return its abstract."""
    headers = {"x-api-key": S2_API_KEY} if S2_API_KEY else {}
    try:
        resp = requests.get(
            S2_SEARCH_URL,
            params={"query": title, "limit": 1, "fields": "title,abstract"},
            headers=headers,
            timeout=10,
        )
        if resp.status_code == 200:
            papers = resp.json().get("data", [])
            if papers and papers[0].get("abstract"):
                return papers[0]["abstract"].strip()
    except requests.RequestException:
        pass
    return None


def check_imputation(fix: bool) -> list[str]:
    """Find raw/ files missing abstracts; optionally fill from Semantic Scholar."""
    findings = []
    raw_mds = [
        p for p in RAW_DIR.glob("*.md")
        if not p.name.startswith("_")
    ]

    for path in raw_mds:
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        if meta.get("abstract"):
            continue  # abstract present

        title = meta.get("title", "")
        if not title:
            findings.append(f"`{path.name}` — no title in frontmatter, cannot search")
            continue

        if fix:
            abstract = s2_fetch_abstract(title)
            if abstract:
                meta["abstract"] = abstract
                write_frontmatter(path, meta, body)
                findings.append(f"`{path.name}` — abstract filled from Semantic Scholar")
            else:
                findings.append(f"`{path.name}` — abstract missing, S2 search returned nothing")
        else:
            findings.append(f"`{path.name}` — abstract missing (run with --fix to impute)")

    return findings


# ── Report writer ─────────────────────────────────────────────────────────────

def status_line(label: str, findings: list[str], ok_msg: str = "No issues found.") -> str:
    icon = "✅" if not findings else "⚠️"
    return f"- {icon} **{label}**: {len(findings)} issue(s)" if findings else f"- ✅ **{label}**: {ok_msg}"


def write_report(
    consistency: list[str],
    coverage: list[str],
    orphans: list[str],
    gaps: list[str],
    imputation: list[str],
) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    def section(title: str, items: list[str], empty_msg: str = "_None found._") -> str:
        body = "\n".join(f"- {i}" for i in items) if items else empty_msg
        return f"## {title}\n\n{body}\n"

    report = f"""# Wiki Lint Report

> Generated: {now}

## Summary

{status_line("Consistency", consistency, "No contradictions found.")}
{status_line("Coverage", coverage, "All concept tags have articles.")}
{status_line("Orphans", orphans, "All summaries are cited.")}
- 💡 **Gap Finder**: {len(gaps)} suggestion(s)
{status_line("Imputation", imputation, "All abstracts present.")}

---

{section("1. Consistency Check", consistency, "_No contradictions detected._")}

{section("2. Coverage Check — missing concept articles", coverage, "_All concept tags have articles._")}

{section("3. Orphan Check — summaries not cited by any concept", orphans, "_All summaries are referenced._")}

{section("4. Gap Finder — suggested new articles", gaps, "_No suggestions._")}

{section("5. Imputation — missing abstracts", imputation, "_All abstracts present._")}
"""
    LINT_REPORT.write_text(report, encoding="utf-8")
    print(f"Wrote {LINT_REPORT}")


# ── CLI ───────────────────────────────────────────────────────────────────────

@click.command()
@click.option("--fix", is_flag=True, help="Run imputation to fill missing abstracts.")
@click.option("--skip-llm", is_flag=True, help="Skip LLM checks (consistency + gaps); faster.")
def main(fix: bool, skip_llm: bool) -> None:
    """Run wiki health checks and write wiki/_lint_report.md."""
    WIKI_DIR.mkdir(parents=True, exist_ok=True)

    client = OpenAI() if not skip_llm else None

    print("Check 1: Consistency...")
    consistency = check_consistency(client) if client else ["(skipped — use without --skip-llm)"]

    print("Check 2: Coverage...")
    coverage = check_coverage()

    print("Check 3: Orphans...")
    orphans = check_orphans()

    print("Check 4: Gap finder...")
    gaps = check_gaps(client) if client else ["(skipped — use without --skip-llm)"]

    print("Check 5: Imputation...")
    imputation = check_imputation(fix=fix)

    write_report(consistency, coverage, orphans, gaps, imputation)

    total = len(consistency) + len(coverage) + len(orphans) + len(imputation)
    print(f"\nDone. {total} issue(s) found. {len(gaps)} gap suggestion(s). See {LINT_REPORT}")


if __name__ == "__main__":
    main()
