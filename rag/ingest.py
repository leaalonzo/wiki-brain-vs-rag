"""
Phase 3 RAG — Ingest: semantic chunking + OpenAI embeddings → ChromaDB.

Chunking strategy:
  1. Split on double newlines (paragraph boundaries)
  2. If a paragraph exceeds MAX_TOKENS, split further at sentence boundaries
  3. Merge short paragraphs until approaching MAX_TOKENS
  4. Prepend OVERLAP_TOKENS tokens from the previous chunk as context overlap

Metadata per chunk: source_file, chunk_index, char_start, char_end.

Usage:
    python -m rag.ingest
    python -m rag.ingest --file raw/my_doc.md
    python -m rag.ingest --force
"""

import hashlib
import os
import re
from pathlib import Path

import chromadb
import click
import tiktoken
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

RAW_DIR = Path("raw")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "rag/chroma_db")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "learning-science")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")

MAX_TOKENS = 800
OVERLAP_TOKENS = 50

_enc = tiktoken.get_encoding("cl100k_base")


# ── Chunking ──────────────────────────────────────────────────────────────────

def _token_count(text: str) -> int:
    return len(_enc.encode(text))


def _split_sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def semantic_chunk(text: str) -> list[tuple[str, int, int]]:
    """
    Return list of (chunk_text, char_start, char_end).

    char_start/char_end are positions in the original text; overlap prefix is
    not counted toward those positions.
    """
    # Step 1: paragraph split
    atomics: list[tuple[str, int, int]] = []
    pos = 0
    for para in re.split(r"\n\n+", text):
        stripped = para.strip()
        if not stripped:
            continue
        start = text.find(stripped, pos)
        end = start + len(stripped)
        pos = end

        if _token_count(stripped) <= MAX_TOKENS:
            atomics.append((stripped, start, end))
        else:
            # Step 2: sentence split for oversized paragraphs
            s_pos = start
            for sent in _split_sentences(stripped):
                s_start = text.find(sent, s_pos)
                s_end = s_start + len(sent)
                atomics.append((sent, s_start, s_end))
                s_pos = s_end

    # Step 3: merge atomics into MAX_TOKENS chunks
    raw_chunks: list[tuple[str, int, int]] = []
    bucket: list[tuple[str, int, int]] = []
    bucket_tokens = 0

    for part, start, end in atomics:
        t = _token_count(part)
        if bucket and bucket_tokens + t > MAX_TOKENS:
            raw_chunks.append(
                ("\n\n".join(p for p, _, _ in bucket), bucket[0][1], bucket[-1][2])
            )
            bucket, bucket_tokens = [], 0
        bucket.append((part, start, end))
        bucket_tokens += t

    if bucket:
        raw_chunks.append(
            ("\n\n".join(p for p, _, _ in bucket), bucket[0][1], bucket[-1][2])
        )

    # Step 4: prepend overlap from the previous chunk
    result: list[tuple[str, int, int]] = []
    for i, (chunk_text, char_start, char_end) in enumerate(raw_chunks):
        if i > 0:
            prev_tokens = _enc.encode(raw_chunks[i - 1][0])
            overlap = _enc.decode(prev_tokens[-OVERLAP_TOKENS:])
            chunk_text = overlap + "\n\n" + chunk_text
        result.append((chunk_text, char_start, char_end))

    return result


# ── ChromaDB / embedding helpers ──────────────────────────────────────────────

def _get_collection(chroma: chromadb.ClientAPI) -> chromadb.Collection:
    return chroma.get_or_create_collection(
        name=CHROMA_COLLECTION,
        metadata={"hnsw:space": "cosine"},
    )


def _embed(client: OpenAI, texts: list[str]) -> list[list[float]]:
    """Embed texts in batches of 100 (API limit)."""
    embeddings: list[list[float]] = []
    for i in range(0, len(texts), 100):
        batch = texts[i : i + 100]
        resp = client.embeddings.create(model=EMBED_MODEL, input=batch)
        embeddings.extend(item.embedding for item in resp.data)
    return embeddings


def _chunk_id(path: Path, index: int) -> str:
    stem = hashlib.md5(str(path).encode()).hexdigest()[:8]
    return f"{path.stem}_{stem}_{index}"


# ── Core ingest ───────────────────────────────────────────────────────────────

def ingest_file(
    path: Path,
    collection: chromadb.Collection,
    openai_client: OpenAI,
    force: bool = False,
) -> int:
    text = path.read_text(encoding="utf-8")
    chunks = semantic_chunk(text)
    if not chunks:
        return 0

    ids = [_chunk_id(path, i) for i in range(len(chunks))]
    documents = [chunk_text for chunk_text, _, _ in chunks]
    metadatas = [
        {
            "source_file": str(path),
            "chunk_index": i,
            "char_start": char_start,
            "char_end": char_end,
        }
        for i, (_, char_start, char_end) in enumerate(chunks)
    ]

    if not force:
        existing = set(collection.get(ids=ids)["ids"])
        new_items = [
            (doc, id_, meta)
            for doc, id_, meta in zip(documents, ids, metadatas)
            if id_ not in existing
        ]
        if not new_items:
            print(f"  All {len(chunks)} chunks already indexed.")
            return 0
        documents, ids, metadatas = map(list, zip(*new_items))

    print(f"  Embedding {len(documents)} chunk(s)...")
    embeddings = _embed(openai_client, documents)
    collection.add(documents=documents, embeddings=embeddings, ids=ids, metadatas=metadatas)
    print(f"  Added {len(documents)} chunk(s).")
    return len(documents)


# ── CLI ───────────────────────────────────────────────────────────────────────

@click.command()
@click.option("--file", "target_file", default=None, help="Ingest a single file.")
@click.option("--force", is_flag=True, default=False, help="Re-embed even if already indexed.")
def main(target_file: str | None, force: bool) -> None:
    """Semantic chunk and embed raw/ .md files into ChromaDB."""
    Path(CHROMA_PERSIST_DIR).mkdir(parents=True, exist_ok=True)
    chroma = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
    openai_client = OpenAI()
    collection = _get_collection(chroma)

    if target_file:
        paths = [Path(target_file)]
    else:
        paths = [
            p for p in RAW_DIR.glob("**/*.*")
            if p.suffix.lower() in {".md", ".txt"}
            and RAW_DIR / "pdfs" not in p.parents
        ]

    if not paths:
        print("No documents found in raw/.")
        return

    total = 0
    for path in paths:
        print(f"Ingesting: {path.name}")
        try:
            total += ingest_file(path, collection, openai_client, force=force)
        except Exception as exc:
            print(f"  Skipping (error): {exc}")

    print(f"\nDone. {total} new chunk(s) embedded across {len(paths)} file(s).")


if __name__ == "__main__":
    main()
