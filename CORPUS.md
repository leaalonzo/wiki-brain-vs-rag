# Corpus

## The original experiment corpus

The experiment used 36 open-access papers covering LLM reasoning, retrieval-augmented generation, and efficient inference. All papers were fetched from Semantic Scholar and arXiv using `tools/fetch_papers.py`. Full metadata is in `raw/_manifest.json`.

**Topic rationale:** This subject was chosen because:
1. It's a fast-moving field where synthesis across papers matters more than recalling any single paper.
2. The concepts are interconnected (RAG, CoT, quantization, RLHF all reference each other), which stresses the wiki's ability to build a concept graph rather than just summarize in isolation.
3. All papers are on arXiv and freely accessible — the fetch pipeline works without institutional access.

**Query tags used:**

| Tag | Topic |
|---|---|
| `chain_of_thought` | Step-by-step reasoning prompting |
| `reinforcement_learning_from_human_feedback` | RLHF, instruction tuning |
| `rag_retrieval` | Retrieval-augmented generation |
| `dense_retrieval` | Bi-encoder / DPR-style retrieval |
| `vector_databases` | ANN search, embedding compression |
| `knowledge_graphs` | KG embedding and reasoning |
| `large_language_models` | Emergent abilities, scaling |
| `quantization` | LLM weight compression (AWQ, SpQR) |
| `speculative_decoding` | Fast inference for transformers |
| `code_generation` | LLMs for program synthesis |
| `llm_evaluation` | Benchmarking, factuality, hallucination |

---

## Sample corpus (included)

The `sample_corpus/` directory contains 5 papers with CC BY 4.0 licenses, sourced from arXiv. They cover the core topics of the experiment and are sufficient to run the full pipeline end-to-end:

| File | Paper | arXiv |
|---|---|---|
| `attention_is_all_you_need.md` | Attention Is All You Need (Vaswani et al., 2017) | 1706.03762 |
| `chain_of_thought_prompting.md` | Chain-of-Thought Prompting Elicits Reasoning (Wei et al., 2022) | 2201.11903 |
| `dense_passage_retrieval.md` | Dense Passage Retrieval for Open-Domain QA (Karpukhin et al., 2020) | 2004.04906 |
| `rag_for_knowledge_intensive_nlp.md` | RAG for Knowledge-Intensive NLP Tasks (Lewis et al., 2020) | 2005.11401 |
| `llama_open_foundation_models.md` | LLaMA: Open and Efficient Foundation Language Models (Touvron et al., 2023) | 2302.13971 |

These files contain the paper abstract and key metadata only (not the full text, which you can fetch via `make fetch-papers` or convert from the PDFs yourself). The pipeline will compile summaries and concept articles from whatever content is present.

---

## Using a different corpus

wiki-brain-vs-rag is topic-agnostic. To use it on your own subject:

1. Edit `tools/queries.yaml` with your search terms.
2. Run `make fetch-papers` to pull papers from Semantic Scholar.
3. Or drop your own PDFs into `raw/pdfs/` and convert them with pymupdf4llm.
4. Clear the old wiki: `rm -rf wiki/ rag/chroma_db/ .compile_state.json`
5. Rebuild: `make compile-wiki && make ingest`

Good candidates for topics: a software engineering concept you're learning, a narrow domain like protein folding papers, or papers from a conference proceedings.
