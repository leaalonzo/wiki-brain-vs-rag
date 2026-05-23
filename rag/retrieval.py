"""
Phase 3 RAG — Retrieval: embed query → query ChromaDB → return ranked chunks.

Usage:
    python -m rag.retrieval "What is the spacing effect?"
    python -m rag.retrieval "chain of thought" --top-k 5
"""

import os
from pathlib import Path

import chromadb
import click
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "rag/chroma_db")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "learning-science")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")
DEFAULT_TOP_K = 10


def _get_collection() -> chromadb.Collection:
    client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
    return client.get_or_create_collection(
        name=CHROMA_COLLECTION,
        metadata={"hnsw:space": "cosine"},
    )


def retrieve(query: str, top_k: int = DEFAULT_TOP_K) -> list[dict]:
    """
    Embed query with text-embedding-3-small and return top_k chunks.

    Each result: {text, source, score, metadata}
      text     : chunk content (may include overlap prefix)
      source   : path to the source file
      score    : cosine similarity in [0, 1], higher = more relevant
      metadata : {source_file, chunk_index, char_start, char_end}
    """
    openai_client = OpenAI()
    resp = openai_client.embeddings.create(model=EMBED_MODEL, input=[query])
    query_embedding = resp.data[0].embedding

    collection = _get_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    for i in range(len(results["ids"][0])):
        distance = results["distances"][0][i]
        meta = results["metadatas"][0][i]
        hits.append({
            "text": results["documents"][0][i],
            "source": meta.get("source_file", "unknown"),
            "score": round(1 - distance, 4),
            "metadata": meta,
        })
    return hits


def format_context(hits: list[dict]) -> str:
    """Format retrieved chunks into a numbered context block for the LLM."""
    parts = []
    for i, hit in enumerate(hits, 1):
        source = Path(hit["source"]).name
        parts.append(f"[{i}] {source} (similarity: {hit['score']})\n{hit['text']}")
    return "\n\n---\n\n".join(parts)


@click.command()
@click.argument("query")
@click.option("--top-k", default=DEFAULT_TOP_K, show_default=True, help="Number of chunks to return.")
def main(query: str, top_k: int) -> None:
    """Retrieve top-k chunks from ChromaDB for a query."""
    hits = retrieve(query, top_k=top_k)
    if not hits:
        print("No results. Run `make ingest` first.")
        return
    for i, hit in enumerate(hits, 1):
        print(f"\n[{i}] {Path(hit['source']).name} | score: {hit['score']:.4f}")
        print(hit["text"][:400])


if __name__ == "__main__":
    main()
