"""
Incrementally compile raw/ documents into wiki/ using gpt-4o.

Phase 2a — Document Summarizer:
  Read each .md in raw/ → write wiki/summaries/<slug>.md

Phase 2b — Concept Article Writer:
  Read all summaries → extract concept tags → write wiki/concepts/<slug>.md
  (one article per unique concept, gathering all relevant summaries as context)

Phase 2d — Master Index:
  wiki/_index.md  : table of all concepts with 1-sentence descriptions
  wiki/_backlinks.md : map of which concepts link to each other

Usage:
    python -m wiki_compiler.compile               # run all phases
    python -m wiki_compiler.compile --force       # recompile everything
    python -m wiki_compiler.compile --file raw/x.md   # single file (phase 2a only)
"""

import json
import os
import re
from datetime import datetime, UTC
from pathlib import Path

import click
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

RAW_DIR = Path("raw")
WIKI_DIR = Path("wiki")
SUMMARIES_DIR = WIKI_DIR / "summaries"
CONCEPTS_DIR = WIKI_DIR / "concepts"
INDEX_FILE = WIKI_DIR / "_index.md"
BACKLINKS_FILE = WIKI_DIR / "_backlinks.md"
COMPILE_LOG = WIKI_DIR / "_compilation_log.json"

COMPILE_MODEL = os.getenv("COMPILE_MODEL", "gpt-4o")

# ── Phase 2a prompts ──────────────────────────────────────────────────────────

SUMMARIZE_SYSTEM = (
    "You are a knowledge base compiler. Your job is to read research documents and "
    "produce precise, well-structured summaries for a personal wiki on learning science."
)

SUMMARIZE_USER = """Summarize this paper for a wiki on cognitive science and learning.
Output a markdown file with these sections:
## Summary (3-4 paragraphs)
## Key Claims (bullet list of 5-7 falsifiable claims)
## Concepts (comma-separated list of 3-8 concept tags this paper relates to)
## Connections (list 2-3 other concepts this connects to, with a 1-sentence explanation)
## Questions Raised (2-3 open questions this paper leaves)

Paper content:
{document_content}"""

# ── Phase 2b prompts ──────────────────────────────────────────────────────────

CONCEPT_SYSTEM = (
    "You are writing a personal research wiki on cognitive science. "
    "Write authoritative, interconnected articles like a technical encyclopedia."
)

CONCEPT_USER = """Write a wiki article for the concept: {concept_name}

Here are all the papers in my knowledge base that relate to this concept:
{relevant_summaries}

Output format:
# {concept_name}
## Definition
## Key Mechanisms
## Evidence Base (cite specific papers from the summaries above)
## Connections to Other Concepts (with [[wiki-link]] syntax)
## Open Questions
## Further Reading (from papers in the knowledge base)

Use [[concept-name]] syntax for any concept that should be a wiki link."""


# ── Helpers ───────────────────────────────────────────────────────────────────

def concept_slug(name: str) -> str:
    """Normalize a concept name to a safe filename stem."""
    # Strip parenthetical abbreviations like "(LLMs)" or "(RAG)"
    name = re.sub(r"\s*\([^)]*\)", "", name)
    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "_", slug).strip("_-")
    # Normalize common plural/singular variants
    slug = re.sub(r"_llms?$", "_llm", slug)
    return slug


def parse_concept_tags(summary_text: str) -> list[str]:
    """Extract comma-separated tags from the ## Concepts section of a summary."""
    match = re.search(r"## Concepts[^\n]*\n(.*?)(?=\n##|\Z)", summary_text, re.DOTALL)
    if not match:
        return []
    content = match.group(1).strip()
    tags = [t.strip().strip("-").strip() for t in re.split(r"[,\n]", content) if t.strip().strip("-").strip()]
    return tags


def extract_definition_sentence(article_text: str) -> str:
    """Return the first sentence from the ## Definition section."""
    match = re.search(r"## Definition\s*\n+(.*?)(?=\n##|\Z)", article_text, re.DOTALL)
    if not match:
        return ""
    content = match.group(1).strip()
    sentence_end = re.search(r"[.!?]\s", content)
    if sentence_end:
        return content[: sentence_end.end()].strip()
    return content[:200].strip()


def load_log() -> dict:
    if COMPILE_LOG.exists():
        return json.loads(COMPILE_LOG.read_text(encoding="utf-8"))
    return {"entries": []}


def append_log(log: dict, entry: dict) -> None:
    log["entries"].append(entry)
    COMPILE_LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")


# ── Phase 2a ──────────────────────────────────────────────────────────────────

def generate_summary(client: OpenAI, source_text: str, filename: str, log: dict) -> str:
    """Summarize one source document and log token usage."""
    response = client.chat.completions.create(
        model=COMPILE_MODEL,
        messages=[
            {"role": "system", "content": SUMMARIZE_SYSTEM},
            {"role": "user", "content": SUMMARIZE_USER.format(document_content=source_text[:12000])},
        ],
        temperature=0.3,
    )
    usage = response.usage
    append_log(log, {
        "timestamp": datetime.now(UTC).isoformat(),
        "phase": "summarize",
        "file": filename,
        "prompt_tokens": usage.prompt_tokens,
        "completion_tokens": usage.completion_tokens,
        "total_tokens": usage.total_tokens,
    })
    return response.choices[0].message.content


def run_phase_2a(client: OpenAI, log: dict, target_file: str | None, force: bool) -> int:
    """Summarize raw/ .md files → wiki/summaries/. Returns count of files compiled."""
    if target_file:
        paths = [Path(target_file)]
    else:
        paths = [
            p for p in RAW_DIR.glob("**/*.*")
            if p.suffix.lower() in {".md", ".txt"}
            and RAW_DIR / "pdfs" not in p.parents
        ]

    if not paths:
        print("Phase 2a: no source documents found in raw/.")
        return 0

    compiled = 0
    for path in paths:
        summary_file = SUMMARIES_DIR / f"{path.stem}.md"
        if not force and summary_file.exists():
            print(f"  [2a] Skipping (already summarized): {path.name}")
            continue

        print(f"  [2a] Summarizing: {path.name}")
        try:
            source_text = path.read_text(encoding="utf-8")
        except Exception as exc:
            print(f"       Skipping (unreadable): {exc}")
            continue

        try:
            summary = generate_summary(client, source_text, path.name, log)
        except Exception as exc:
            print(f"       Skipping (API error): {exc}")
            continue

        summary_file.write_text(summary, encoding="utf-8")
        print(f"       Wrote {summary_file}")
        compiled += 1

    return compiled


# ── Phase 2b ──────────────────────────────────────────────────────────────────

def write_concept_article(client: OpenAI, concept_name: str, relevant_summaries: list[tuple[str, str]], log: dict) -> str:
    """Call gpt-4o to write a concept article from the relevant summaries."""
    summaries_block = "\n\n---\n\n".join(
        f"**{name}**\n{text[:3000]}" for name, text in relevant_summaries
    )
    response = client.chat.completions.create(
        model=COMPILE_MODEL,
        messages=[
            {"role": "system", "content": CONCEPT_SYSTEM},
            {"role": "user", "content": CONCEPT_USER.format(
                concept_name=concept_name,
                relevant_summaries=summaries_block,
            )},
        ],
        temperature=0.3,
    )
    usage = response.usage
    append_log(log, {
        "timestamp": datetime.now(UTC).isoformat(),
        "phase": "concept",
        "concept": concept_name,
        "prompt_tokens": usage.prompt_tokens,
        "completion_tokens": usage.completion_tokens,
        "total_tokens": usage.total_tokens,
    })
    return response.choices[0].message.content


def run_phase_2b(client: OpenAI, log: dict, force: bool) -> int:
    """Write concept articles from summaries. Returns count of articles written."""
    summary_files = list(SUMMARIES_DIR.glob("*.md"))
    if not summary_files:
        print("Phase 2b: no summaries found — run phase 2a first.")
        return 0

    # Collect all concept tags and map them to the summaries that mention them
    concept_to_summaries: dict[str, list[tuple[str, str]]] = {}
    for sf in summary_files:
        text = sf.read_text(encoding="utf-8")
        tags = parse_concept_tags(text)
        for tag in tags:
            concept_to_summaries.setdefault(tag, []).append((sf.stem, text))

    written = 0
    for concept_name, summaries in sorted(concept_to_summaries.items()):
        slug = concept_slug(concept_name)
        concept_file = CONCEPTS_DIR / f"{slug}.md"
        if not force and concept_file.exists():
            print(f"  [2b] Skipping (exists): {concept_name}")
            continue

        print(f"  [2b] Writing concept: {concept_name} ({len(summaries)} source(s))")
        try:
            article = write_concept_article(client, concept_name, summaries, log)
        except Exception as exc:
            print(f"       Skipping (API error): {exc}")
            continue

        concept_file.write_text(article, encoding="utf-8")
        written += 1

    return written


# ── Phase 2d ──────────────────────────────────────────────────────────────────

def run_phase_3() -> None:
    """Rebuild _index.md (concept table) and _backlinks.md."""
    concept_files = sorted(CONCEPTS_DIR.glob("*.md"))
    summary_files = sorted(SUMMARIES_DIR.glob("*.md"))
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # _index.md — table of concepts with 1-sentence descriptions
    rows = []
    for cf in concept_files:
        text = cf.read_text(encoding="utf-8")
        desc = extract_definition_sentence(text) or "_No definition yet._"
        rows.append(f"| [[{cf.stem}]] | {desc} |")

    table = (
        "| Concept | Description |\n|---|---|\n" + "\n".join(rows)
        if rows else "_No concepts yet._"
    )

    source_lines = "\n".join(f"- [[{p.stem}]]" for p in summary_files)

    INDEX_FILE.write_text(
        f"""# Wiki Brain — Master Index

> Auto-maintained by `wiki_compiler/compile.py`. Do not edit manually.

## Concepts

{table}

## Source Summaries

{source_lines or "_None yet._"}

## Stats

- Last compiled: {now}
- Concept articles: {len(concept_files)}
- Source summaries: {len(summary_files)}
""",
        encoding="utf-8",
    )
    print(f"  [3] Wrote {INDEX_FILE}")

    # _backlinks.md — which concepts link to each other
    backlinks: dict[str, list[str]] = {}
    for cf in concept_files:
        text = cf.read_text(encoding="utf-8")
        links = re.findall(r"\[\[([^\]]+)\]\]", text)
        for link in links:
            target = concept_slug(link)
            backlinks.setdefault(target, []).append(cf.stem)

    bl_lines = []
    for target in sorted(backlinks):
        sources = ", ".join(f"[[{s}]]" for s in sorted(set(backlinks[target])))
        bl_lines.append(f"- **{target}** ← {sources}")

    BACKLINKS_FILE.write_text(
        f"""# Wiki Brain — Backlinks

> Auto-maintained by `wiki_compiler/compile.py`. Do not edit manually.
> Format: **concept** ← concepts that link to it

{chr(10).join(bl_lines) or "_No links yet._"}
""",
        encoding="utf-8",
    )
    print(f"  [3] Wrote {BACKLINKS_FILE}")


# ── CLI ───────────────────────────────────────────────────────────────────────

@click.command()
@click.option("--file", "target_file", default=None, help="Run phase 2a on a single file only.")
@click.option("--force", is_flag=True, help="Recompile all phases even if output exists.")
def main(target_file: str | None, force: bool) -> None:
    """Run all compilation phases: summarize → concept articles → index."""
    client = OpenAI()
    log = load_log()

    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    CONCEPTS_DIR.mkdir(parents=True, exist_ok=True)
    WIKI_DIR.mkdir(parents=True, exist_ok=True)

    print("=== Phase 2a: Document Summarizer ===")
    n_summaries = run_phase_2a(client, log, target_file, force)

    if not target_file:
        print("\n=== Phase 2b: Concept Article Writer ===")
        n_concepts = run_phase_2b(client, log, force)

        print("\n=== Phase 2d: Master Index ===")
        run_phase_3()
    else:
        n_concepts = 0

    print(f"\nDone. Summaries: {n_summaries}  |  Concepts: {n_concepts}")
    if log["entries"]:
        total = sum(e["total_tokens"] for e in log["entries"])
        print(f"Tokens logged this session: {total:,}")


if __name__ == "__main__":
    main()
