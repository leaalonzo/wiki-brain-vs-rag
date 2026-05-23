---
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"]
year: 2020
abstract: "Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation. We introduce two RAG formulations, one which conditions on all retrieved passages (RAG-Sequence) and one which conditions on each retrieved passage individually (RAG-Token). We marginalize the latent documents with a top-K approximation, either across the whole generated sequence or each token. We test our formulations on a wide range of knowledge intensive tasks and set the state of the art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a BART parametric-only baseline."
source_url: "https://arxiv.org/abs/2005.11401"
pdf_url: "https://arxiv.org/pdf/2005.11401"
doi: "10.48550/arXiv.2005.11401"
query_tag: "rag_retrieval"
license: "CC BY 4.0"
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

Lewis et al., 2020 · arXiv:2005.11401

## Abstract

Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation.

## Key contributions

- Introduces RAG: combines a DPR retriever with a BART generator in an end-to-end trainable system.
- RAG-Sequence: conditions the full generated sequence on each retrieved document and marginalizes.
- RAG-Token: each generated token can draw from a different retrieved document.
- Demonstrates that non-parametric memory (retrieval) complements parametric memory (model weights) for factual tasks.

## Core concepts

- **Parametric memory**: knowledge stored in model weights through pretraining.
- **Non-parametric memory**: external document store (Wikipedia dump) accessed at inference.
- **RAG-Sequence vs RAG-Token**: two formulations for how to integrate multiple retrieved passages.
- **Marginalization over documents**: top-K retrieved docs weighted by retrieval probability.

## Connections

- This paper names the pattern ("RAG") that wiki-brain-vs-rag's rag/ pipeline implements.
- DPR (Karpukhin et al.) is used as the retriever.
- FreshLLMs extends RAG to handle time-sensitive queries using live search engine results.
- The wiki Q&A approach in wiki-brain-vs-rag is an alternative to RAG: pre-compiled knowledge vs. on-demand retrieval.
