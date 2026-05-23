# wiki-brain-vs-rag

**wiki-brain-vs-rag** turns a folder of research papers into a queryable knowledge base in two complementary ways: a compiled wiki of concept articles (synthesized by an LLM) and a standard RAG pipeline backed by ChromaDB. A built-in eval harness runs both systems head-to-head on the same questions, with GPT-4o as judge.

> Motivation: Andrej Karpathy observed that reading papers accumulates a knowledge debt — you can't recall or connect what you've read. This project tests whether an LLM can compile that debt into a structured, searchable wiki, and how that wiki compares to a baseline vector RAG pipeline for Q&A.

---

## Results (LLM/NLP corpus, 36 papers, 10 eval questions)

**Per-category averages** (GPT-4o judge, 1–5 each):

| Category | Wiki | RAG |
|---|---|---|
| Accuracy | 4.6 | 4.4 |
| Completeness | 4.6 | 4.3 |
| Citation | 2.5 | 2.7 |
| Synthesis | 4.3 | 4.1 |
| **Overall** | **4.0** | **3.88** |

**Per-question breakdown** (scores out of 20):

| Q | Question | Wiki | RAG | Diff | Winner |
|---|---|---|---|---|---|
| Q1 | What is chain-of-thought prompting and why does it improve reasoning? | 16 | 17 | −1 | RAG |
| Q2 | What are the main failure modes of chain-of-thought prompting? | 16 | 9 | +7 | Wiki |
| Q3 | How does Plan-and-Solve prompting differ from standard CoT? | 14 | 18 | −4 | RAG |
| Q4 | What is RLHF and what are its main limitations? | 12 | 17 | −5 | RAG |
| Q5 | How does ERNIE-Search bridge cross-encoder and dual-encoder? | 18 | 18 | 0 | Tie |
| Q6 | How does AWQ compare to other quantization methods? | 14 | 18 | −4 | RAG |
| Q7 | What is speculative decoding and how does it accelerate inference? | 17 | 4 | +13 | Wiki |
| Q8 | What problem does FreshLLMs address? | 19 | 19 | 0 | Tie |
| Q9 | What is IRCoT and how does it combine retrieval with CoT? | 18 | 17 | +1 | Wiki |
| Q10 | How does RocketQA improve dense passage retrieval? | 16 | 18 | −2 | RAG |

**Why wiki has higher averages but fewer wins:** RAG's 5 wins were all narrow (−1 to −5 points). Wiki's 3 wins included two large swings: Q7 (+13, RAG had a missing document) and Q2 (+7). Those outliers pulled wiki's category averages up without adding win count. RAG is more consistently good; wiki is higher-variance with bigger upside when its compiled knowledge is on-topic.

Win/loss: Wiki 3 — RAG 5 — Ties 2 (out of 10 questions)

Cost per 10 queries: Wiki $0.45 — RAG $0.31  
One-time compilation cost: ~$0.65  
Full write-up: [Substack series](https://substack.com) *(link to be added after publication)*

---

## Key takeaway

Precomputed structure beats simple retrieval — but the comparison has limits.

The wiki won on questions that required connecting ideas across papers (Q2: CoT failure modes, Q7: speculative decoding, Q9: IRCoT). RAG won on straightforward factual questions where a single relevant chunk was sufficient. Q7 exposed RAG's core weakness: if retrieval fails, the answer fails completely — RAG returned four irrelevant documents and scored 1/5 across all categories. The wiki had no such single point of failure because knowledge was already compiled.

The honest caveat is that **RAG's losses are partly self-inflicted**. This implementation uses fixed chunking, cosine similarity only, and no reranking. A stronger RAG stack (hybrid sparse+dense search, reranking, semantic chunking) would likely close the gap or flip some results.

The finding is therefore scoped: **for a simple RAG baseline, a precompiled wiki is more robust and higher-variance**. This is not a comparison between wiki and RAG in general — it is a comparison between a precompiled wiki and the simplest reasonable RAG implementation.

---

## What this project is actually comparing

This project compares two different approaches to organizing knowledge from research papers:

- **Wiki pipeline:** precomputes synthesis during ingestion by generating summaries, concept articles, and backlinks across the corpus.
- **RAG pipeline:** retrieves relevant chunks dynamically at query time and synthesizes answers from retrieved context.

In other words, this benchmark compares precomputed semantic structure versus query-time retrieval.

The RAG implementation intentionally uses a simple baseline retrieval stack: dense vector retrieval over fixed-size chunks without reranking, hybrid sparse+dense search, or graph traversal.

> Evaluation note: GPT-4o served as a single automated evaluator using a fixed rubric. This benchmark is intended as an exploratory comparison for rapid iteration, not a definitive human evaluation.

---

## Architecture

```
raw/*.md  (paper text + YAML frontmatter)
   │
   ├─► rag/ingest.py  ─────────────► ChromaDB  ──► rag/qa.py
   │     fixed chunking                              top-k retrieval + gpt-4o
   │
   └─► wiki_compiler/compile.py ──► wiki/      ──► wiki_compiler/query.py
         Phase 2a: summarize                         LLM selects articles + gpt-4o
         Phase 2b: concept articles
         Phase 2c: lint
         Phase 2d: index + backlinks
```

---

## Quick Start

**Requirements:** Python 3.11+, an OpenAI API key.

### 1. Clone and install

```bash
git clone https://github.com/YOUR_USERNAME/wiki-brain-vs-rag.git
cd wiki-brain-vs-rag
python3 -m venv .venv && source .venv/bin/activate
make install
```

### 2. Configure

```bash
cp .env.example .env
# Edit .env and set OPENAI_API_KEY=sk-...
```

### 3. Add your corpus

**Option A — use the included sample corpus (5 CC-licensed papers, instant start):**
```bash
cp sample_corpus/*.md raw/
```

**Option B — fetch papers from Semantic Scholar on your own topic:**
```bash
# Edit tools/queries.yaml to set your search queries, then:
make fetch-papers
```

**Option C — drop in your own PDFs:**
```bash
# Place PDFs in raw/pdfs/, then convert to Markdown:
python3 - <<'EOF'
import pymupdf4llm
from pathlib import Path
for pdf in Path("raw/pdfs").glob("*.pdf"):
    md = pymupdf4llm.to_markdown(str(pdf))
    Path("raw/" + pdf.stem + ".md").write_text(md)
EOF
```

### 4. Build the wiki and RAG index

```bash
make compile-wiki   # ~$0.02 per paper with gpt-4o
make ingest         # embed chunks into ChromaDB
```

### 5. Ask questions

```bash
# Wiki Q&A (synthesis-focused):
make run-wiki-qa

# RAG Q&A (retrieval-focused):
make run-rag

# Run the full eval against both systems:
make run-eval
```

---

## Changing the topic

To use wiki-brain-vs-rag on a completely different subject:

1. **Edit `tools/queries.yaml`** — replace the search queries with your topic.
2. **Run `make fetch-papers`** — pulls open-access PDFs from Semantic Scholar.
3. **Clear stale state** — `rm -rf wiki/ rag/chroma_db/ .compile_state.json`
4. **Rebuild** — `make compile-wiki && make ingest`
5. **Update `eval/questions.md`** — write 10 questions drawn from your new corpus.

No other files need editing. The pipeline is topic-agnostic.

---

## Cost estimates

All costs use gpt-4o pricing (input $2.50/1M, output $10.00/1M, 80/20 split assumed).

| Step | Tokens | Estimated cost |
|---|---|---|
| Fetch + convert 36 papers | — | free |
| Compile wiki (summarize + concept articles) | 161,825 | ~$0.65 |
| Ingest into ChromaDB (embeddings only) | 621 chunks | ~$0.02 |
| Run eval — Wiki system (10 questions) | 112,281 | ~$0.45 |
| Run eval — RAG system (10 questions) | 78,643 | ~$0.31 |
| **Total experiment** | | **~$1.43** |


---

## Project layout

```
wiki-brain-vs-rag/
├── raw/                  # Source documents (gitignored except manifest)
│   └── _manifest.json    # Metadata for the original 36-paper corpus
├── sample_corpus/        # 5 CC-licensed papers — ready to copy into raw/
├── wiki/                 # Compiled output: summaries, concept articles, index
├── rag/                  # RAG pipeline: ingest.py, retrieval.py, qa.py
├── wiki_compiler/        # Wiki pipeline: compile.py, lint.py, query.py
├── eval/                 # Evaluation harness and results
│   ├── questions.md      # 10 benchmark questions
│   └── results/          # Per-question JSON + summary.md
├── tools/                # fetch_papers, search, blog_generator
├── content/drafts/       # Generated Substack and LinkedIn posts
├── obsidian/             # Preconfigured Obsidian vault (open in Obsidian)
├── Makefile
└── .env.example
```

---

## All Makefile targets

```
make install               Install Python dependencies
make fetch-papers          Fetch open-access PDFs from Semantic Scholar
make compile-wiki          LLM-compile raw/ → wiki/ (incremental)
make compile-wiki-force    Recompile everything
make lint-wiki             LLM health-check wiki/ articles
make lint-wiki-fast        Structural checks only (no LLM calls)
make ingest                Chunk + embed raw/ docs into ChromaDB
make ingest-force          Re-embed everything
make run-rag               Interactive RAG Q&A
make run-wiki-qa           Interactive wiki Q&A
make run-eval              Eval both systems on eval/questions.md
make search Q="..."        Keyword search across wiki/
```

---

## Obsidian integration

Open the `wiki/` directory as an Obsidian vault. Concept articles use `[[wikilink]]` syntax and form a navigable graph. The preconfigured `obsidian/` vault can be opened directly in Obsidian.

```bash
# If you prefer a symlink so changes appear instantly:
ln -sf "$(pwd)/wiki" obsidian/wiki
```

---

## Models used

| Task | Model | Configurable via |
|---|---|---|
| Wiki compilation, Q&A, eval judging | `gpt-4o` | `COMPILE_MODEL`, `QA_MODEL` |
| Linting | `gpt-4o` | `LINT_MODEL` |
| Embeddings | `text-embedding-3-small` | `EMBED_MODEL` |

---

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | — | **Required** |
| `SEMANTIC_SCHOLAR_API_KEY` | — | Optional; raises S2 rate limit |
| `COMPILE_MODEL` | `gpt-4o` | Wiki compilation model |
| `QA_MODEL` | `gpt-4o` | Q&A model |
| `LINT_MODEL` | `gpt-4o` | Lint and eval judge model |
| `EMBED_MODEL` | `text-embedding-3-small` | Embedding model |
| `CHROMA_PERSIST_DIR` | `rag/chroma_db` | ChromaDB storage path |
| `CHROMA_COLLECTION` | `wiki_brain` | ChromaDB collection name |

---

## Requirements

- Python 3.11+
- OpenAI API key (required)
- Semantic Scholar API key (optional; increases fetch rate limit from ~1 req/s to 10 req/s)
- ~500 MB disk space for a 36-paper corpus with ChromaDB index

