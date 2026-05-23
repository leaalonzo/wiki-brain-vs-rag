"""
Naive full-text search engine over wiki/ — Karpathy-style CLI tool.

Scores each article by term frequency of the query tokens, then prints
ranked results with highlighted snippets. No embeddings required.

Usage:
    python -m tools.search "attention mechanism"
    python tools/search.py "transformer" --top 10 --summaries-only
"""

import math
import re
from pathlib import Path

import click
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel

WIKI_DIR = Path("wiki")
CONCEPTS_DIR = WIKI_DIR / "concepts"
SUMMARIES_DIR = WIKI_DIR / "summaries"
SNIPPET_CHARS = 300

console = Console()


def tokenize(text: str) -> list[str]:
    """Lowercase, strip punctuation, split into tokens."""
    return re.findall(r"[a-z0-9']+", text.lower())


def tf_idf_score(query_tokens: list[str], doc_tokens: list[str], df: dict, N: int) -> float:
    """
    Compute a simple TF-IDF score for query_tokens against doc_tokens.

    df[term] = number of documents containing term.
    N = total document count.
    """
    if not doc_tokens:
        return 0.0
    doc_freq: dict[str, int] = {}
    for t in doc_tokens:
        doc_freq[t] = doc_freq.get(t, 0) + 1

    score = 0.0
    for qt in set(query_tokens):
        tf = doc_freq.get(qt, 0) / len(doc_tokens)
        idf = math.log((N + 1) / (df.get(qt, 0) + 1))
        score += tf * idf
    return score


def extract_snippet(text: str, query_tokens: list[str], chars: int = SNIPPET_CHARS) -> str:
    """Find the passage in text most dense with query terms, return a short snippet."""
    lower = text.lower()
    best_pos = 0
    best_count = 0
    for i in range(0, len(lower) - chars, 50):
        window = lower[i : i + chars]
        count = sum(1 for qt in query_tokens if qt in window)
        if count > best_count:
            best_count = count
            best_pos = i

    snippet = text[best_pos : best_pos + chars].strip()
    # Highlight query terms
    for qt in query_tokens:
        snippet = re.sub(rf"\b{re.escape(qt)}\b", f"[bold yellow]{qt}[/bold yellow]", snippet, flags=re.IGNORECASE)
    return snippet


def build_df(docs: list[tuple[Path, list[str]]]) -> dict[str, int]:
    """Build document-frequency table."""
    df: dict[str, int] = {}
    for _, tokens in docs:
        for t in set(tokens):
            df[t] = df.get(t, 0) + 1
    return df


@click.command()
@click.argument("query")
@click.option("--top", default=5, show_default=True, help="Number of results to show.")
@click.option("--concepts-only", is_flag=True, help="Search only concept articles.")
@click.option("--summaries-only", is_flag=True, help="Search only summary articles.")
def main(query: str, top: int, concepts_only: bool, summaries_only: bool) -> None:
    """Full-text search over wiki/ articles. Ranked by TF-IDF."""
    paths: list[Path] = []
    if not summaries_only:
        paths += sorted(CONCEPTS_DIR.glob("*.md"))
    if not concepts_only:
        paths += sorted(SUMMARIES_DIR.glob("*.md"))

    if not paths:
        console.print("[yellow]No wiki articles found. Run `make compile-wiki` first.[/yellow]")
        return

    docs: list[tuple[Path, str, list[str]]] = []
    for p in paths:
        text = p.read_text(encoding="utf-8")
        docs.append((p, text, tokenize(text)))

    query_tokens = tokenize(query)
    df = build_df([(p, tokens) for p, _, tokens in docs])
    N = len(docs)

    scored = [
        (tf_idf_score(query_tokens, tokens, df, N), path, text)
        for path, text, tokens in docs
    ]
    scored.sort(key=lambda x: x[0], reverse=True)
    top_results = [(s, p, t) for s, p, t in scored if s > 0][:top]

    if not top_results:
        console.print(f"[red]No results for:[/red] {query}")
        return

    console.print(f"\n[bold]Search:[/bold] {escape(query)}  |  {len(top_results)} result(s)\n")
    for rank, (score, path, text) in enumerate(top_results, 1):
        snippet = extract_snippet(text, query_tokens)
        label = f"[{rank}] {path.parent.name}/{path.name}  (score: {score:.4f})"
        console.print(Panel(snippet, title=escape(label), border_style="cyan"))


if __name__ == "__main__":
    main()
