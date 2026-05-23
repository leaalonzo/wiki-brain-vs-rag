"""
Wiki Q&A — Phase 4 eval-compatible answering via compiled wiki/.

Two-step approach:
  1. LLM reads wiki/_index.md and selects relevant concept/summary slugs
  2. Load selected articles, generate answer with gpt-4o

answer() returns {answer, articles_used, token_count, latency_ms}

Usage:
    python -m wiki_compiler.query "What is X?"
    python -m wiki_compiler.query --interactive
"""

import json
import os
import time
from pathlib import Path

import click
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

WIKI_DIR = Path("wiki")
CONCEPTS_DIR = WIKI_DIR / "concepts"
SUMMARIES_DIR = WIKI_DIR / "summaries"
INDEX_FILE = WIKI_DIR / "_index.md"
QA_MODEL = os.getenv("QA_MODEL", "gpt-4o")
MAX_CONTEXT_CHARS = 80_000
MAX_CONCEPTS = 8
MAX_SUMMARIES = 4

SYSTEM_PROMPT = """You are a knowledgeable research assistant with access to a curated wiki.
Answer the user's question using the wiki articles provided. Be precise and cite
article names (e.g. "According to [[ConceptName]]..."). If the wiki does not cover
the topic, say so."""

SELECT_PROMPT = """You are selecting wiki articles to answer a research question.

Available articles are listed in the index below. Select the most relevant ones.
Return JSON: {{"concepts": ["slug1", "slug2", ...], "summaries": ["slug1", ...]}}
Select at most {max_concepts} concepts and {max_summaries} summaries.
Use exact slugs as they appear in the index (the text inside [[...]] markers).
If nothing is relevant, return empty lists.

Question: {question}

Wiki Index:
{index}"""


def _load_selected_articles(concepts: list[str], summaries: list[str]) -> tuple[str, list[str]]:
    """Load article text for selected slugs. Returns (context_str, articles_used)."""
    parts = []
    used = []

    for slug in concepts[:MAX_CONCEPTS]:
        path = CONCEPTS_DIR / f"{slug}.md"
        if not path.exists():
            # Try with .md already stripped
            candidates = list(CONCEPTS_DIR.glob(f"{slug}*.md"))
            path = candidates[0] if candidates else path
        if path.exists():
            parts.append(f"### Concept: {path.stem}\n\n{path.read_text(encoding='utf-8')}")
            used.append(str(path))

    for slug in summaries[:MAX_SUMMARIES]:
        path = SUMMARIES_DIR / f"{slug}.md"
        if not path.exists():
            candidates = list(SUMMARIES_DIR.glob(f"{slug}*.md"))
            path = candidates[0] if candidates else path
        if path.exists():
            parts.append(f"### Summary: {path.stem}\n\n{path.read_text(encoding='utf-8')}")
            used.append(str(path))

    return "\n\n---\n\n".join(parts), used


def _keyword_fallback(question: str) -> tuple[str, list[str]]:
    """Keyword-scored fallback when index is missing."""
    query_words = set(question.lower().split())
    all_files = sorted(CONCEPTS_DIR.glob("*.md")) + sorted(SUMMARIES_DIR.glob("*.md"))

    def score(p: Path) -> int:
        return sum(1 for w in query_words if w in p.read_text(encoding="utf-8").lower())

    ranked = sorted(all_files, key=score, reverse=True)
    parts, used, total = [], [], 0
    for path in ranked:
        text = path.read_text(encoding="utf-8")
        if total + len(text) > MAX_CONTEXT_CHARS:
            break
        parts.append(f"### {path.stem}\n\n{text}")
        used.append(str(path))
        total += len(text)

    return "\n\n---\n\n".join(parts), used


def answer(question: str) -> dict:
    """
    Two-step wiki answering: select relevant articles, then generate answer.

    Returns:
        answer       : str
        articles_used: list[str] — paths of articles loaded as context
        token_count  : int — total tokens across both LLM calls
        latency_ms   : int
    """
    client = OpenAI()
    t0 = time.time()
    total_tokens = 0

    # Step 1: select relevant articles via LLM
    if INDEX_FILE.exists():
        index_text = INDEX_FILE.read_text(encoding="utf-8")
        try:
            sel_response = client.chat.completions.create(
                model=QA_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": SELECT_PROMPT.format(
                            question=question,
                            index=index_text,
                            max_concepts=MAX_CONCEPTS,
                            max_summaries=MAX_SUMMARIES,
                        ),
                    }
                ],
                temperature=0.0,
                response_format={"type": "json_object"},
            )
            total_tokens += sel_response.usage.total_tokens
            sel = json.loads(sel_response.choices[0].message.content)
            context, articles_used = _load_selected_articles(
                sel.get("concepts", []), sel.get("summaries", [])
            )
        except Exception:
            context, articles_used = _keyword_fallback(question)
    else:
        context, articles_used = _keyword_fallback(question)

    if not context:
        return {
            "answer": "Wiki is empty or no relevant articles found. Run `make compile-wiki` first.",
            "articles_used": [],
            "token_count": total_tokens,
            "latency_ms": int((time.time() - t0) * 1000),
        }

    # Step 2: generate answer
    ans_response = client.chat.completions.create(
        model=QA_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Wiki articles:\n\n{context[:MAX_CONTEXT_CHARS]}\n\nQuestion: {question}",
            },
        ],
        temperature=0.2,
    )
    total_tokens += ans_response.usage.total_tokens

    return {
        "answer": ans_response.choices[0].message.content,
        "articles_used": articles_used,
        "token_count": total_tokens,
        "latency_ms": int((time.time() - t0) * 1000),
    }


@click.command()
@click.argument("question", required=False)
@click.option("--interactive", "-i", is_flag=True, help="Start an interactive session.")
def main(question: str | None, interactive: bool) -> None:
    """Q&A grounded in compiled wiki/ articles."""
    if interactive:
        print("Wiki Q&A — type 'quit' to exit\n")
        while True:
            q = input("Q: ").strip()
            if q.lower() in {"quit", "exit", "q"}:
                break
            if not q:
                continue
            result = answer(q)
            print(f"\nA: {result['answer']}")
            print(f"\nArticles used: {len(result['articles_used'])}  |  Tokens: {result['token_count']}\n")
    elif question:
        result = answer(question)
        print(result["answer"])
        print(f"\nArticles used: {len(result['articles_used'])}  |  Tokens: {result['token_count']}")
    else:
        raise click.UsageError("Provide a QUESTION or use --interactive.")


if __name__ == "__main__":
    main()
