"""
Phase 3 RAG — Q&A: retrieve context chunks then answer with gpt-4o.

answer() returns:
  {answer, sources_used, chunks_retrieved, token_count}

Usage:
    python -m rag.qa "What is the spacing effect?"
    python -m rag.qa --interactive
"""

import os
from pathlib import Path

import click
from dotenv import load_dotenv
from openai import OpenAI

from rag.retrieval import retrieve, format_context

load_dotenv()

QA_MODEL = os.getenv("QA_MODEL", "gpt-4o")

SYSTEM_PROMPT = (
    "You are a research assistant. Answer questions using ONLY the provided "
    "context. Cite your sources. If the context is insufficient, say so."
)


def answer(question: str, top_k: int = 10) -> dict:
    """
    Retrieve relevant chunks and generate an answer with gpt-4o.

    Returns:
        answer           : str
        sources_used     : list[str] — unique source filenames
        chunks_retrieved : list[dict] — raw retrieve() results
        token_count      : int — total tokens consumed
    """
    client = OpenAI()
    hits = retrieve(question, top_k=top_k)

    if not hits:
        return {
            "answer": "No indexed documents found. Run `make ingest` first.",
            "sources_used": [],
            "chunks_retrieved": [],
            "token_count": 0,
        }

    context = format_context(hits)
    response = client.chat.completions.create(
        model=QA_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Question: {question}\n\nContext:\n{context}"},
        ],
        temperature=0.2,
    )

    return {
        "answer": response.choices[0].message.content,
        "sources_used": sorted({Path(h["source"]).name for h in hits}),
        "chunks_retrieved": hits,
        "token_count": response.usage.total_tokens,
    }


@click.command()
@click.argument("question", required=False)
@click.option("--top-k", default=10, show_default=True, help="Chunks to retrieve.")
@click.option("--interactive", "-i", is_flag=True, help="Start an interactive Q&A loop.")
def main(question: str | None, top_k: int, interactive: bool) -> None:
    """RAG Q&A: retrieve from ChromaDB then answer with gpt-4o."""
    if interactive:
        print("RAG Q&A — type 'quit' to exit\n")
        while True:
            q = input("Q: ").strip()
            if q.lower() in {"quit", "exit", "q"}:
                break
            if not q:
                continue
            result = answer(q, top_k=top_k)
            print(f"\nA: {result['answer']}")
            print(f"\nSources: {', '.join(result['sources_used'])}")
            print(f"Tokens: {result['token_count']}\n")
    elif question:
        result = answer(question, top_k=top_k)
        print(result["answer"])
        print(f"\nSources: {', '.join(result['sources_used'])}")
        print(f"Tokens: {result['token_count']}")
    else:
        raise click.UsageError("Provide a QUESTION or use --interactive.")


if __name__ == "__main__":
    main()
