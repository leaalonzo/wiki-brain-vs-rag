---
title: "Dense Passage Retrieval for Open-Domain Question Answering"
authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "Patrick Lewis", "Ledell Wu", "Sergey Edunov", "Danqi Chen", "Wen-tau Yih"]
year: 2020
abstract: "Open-domain question answering relies on efficient passage retrieval to select candidate contexts, where traditional sparse vector space models, such as TF-IDF or BM25, are the de facto method. In this work, we show that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework. When evaluated on a wide range of open-domain QA datasets, our dense retrieval approach substantially outperforms a strong Lucene-BM25 system largely used as the retrieval component in open-domain QA systems, by 9%-19% absolute in terms of top-20 passage retrieval accuracy, and helps our end-to-end QA system establish new state-of-the-art on multiple open-domain QA benchmarks."
source_url: "https://arxiv.org/abs/2004.04906"
pdf_url: "https://arxiv.org/pdf/2004.04906"
doi: "10.48550/arXiv.2004.04906"
query_tag: "dense_retrieval"
license: "CC BY 4.0"
---

# Dense Passage Retrieval for Open-Domain Question Answering

Karpukhin et al., 2020 · arXiv:2004.04906

## Abstract

Open-domain question answering relies on efficient passage retrieval to select candidate contexts, where traditional sparse vector space models, such as TF-IDF or BM25, are the de facto method. In this work, we show that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework. When evaluated on a wide range of open-domain QA datasets, our dense retrieval approach substantially outperforms a strong Lucene-BM25 system largely used as the retrieval component in open-domain QA systems, by 9%-19% absolute in terms of top-20 passage retrieval accuracy, and helps our end-to-end QA system establish new state-of-the-art on multiple open-domain QA benchmarks.

## Key contributions

- Shows dense vector retrieval can replace BM25 for open-domain QA with better accuracy.
- Introduces the dual-encoder (bi-encoder) architecture: separate BERT encoders for questions and passages.
- In-batch negatives training: efficient use of batch passages as negative examples during training.
- Releases DPR checkpoints and training data that became the standard baseline for dense retrieval.

## Core concepts

- **Dual-encoder / bi-encoder**: encode questions and passages independently into a shared embedding space; retrieval is inner-product search.
- **In-batch negatives**: treat other passages in the mini-batch as negative examples; avoids costly hard negative mining.
- **Maximum inner-product search (MIPS)**: FAISS used for efficient approximate nearest-neighbor retrieval at inference.
- **Open-domain QA pipeline**: retriever → reader (BERT extractive reader).

## Connections

- Foundation for wiki-brain-vs-rag's RAG pipeline (ChromaDB uses the same cosine similarity principle).
- Extended by RocketQA (cross-batch negatives, denoised hard negatives).
- ERNIE-Search distills cross-encoder knowledge into a DPR-style dual-encoder.
- Encoder attribution analysis (Li et al.) examines which DPR encoder matters more.
