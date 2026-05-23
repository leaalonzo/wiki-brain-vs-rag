---
title: "LLaMA: Open and Efficient Foundation Language Models"
authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "Xavier Martinet", "Marie-Anne Lachaux", "Timothée Lacroix", "Baptiste Rozière", "Naman Goyal", "Eric Hambro", "Faisal Azhar", "Aurélien Rodriguez", "Armand Joulin", "Edouard Grave", "Guillaume Lample"]
year: 2023
abstract: "We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community."
source_url: "https://arxiv.org/abs/2302.13971"
pdf_url: "https://arxiv.org/pdf/2302.13971"
doi: "10.48550/arXiv.2302.13971"
query_tag: "large_language_models"
license: "CC BY 4.0"
---

# LLaMA: Open and Efficient Foundation Language Models

Touvron et al., 2023 · arXiv:2302.13971

## Abstract

We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community.

## Key contributions

- Demonstrates that open-access training data (CommonCrawl, The Pile, Wikipedia) can produce models competitive with proprietary-data models at the same scale.
- LLaMA-13B surpasses GPT-3 (175B) on most benchmarks — efficiency gain from longer training on more tokens (Chinchilla insight applied).
- Releases model weights, enabling the open-source fine-tuning ecosystem (Alpaca, Vicuna, Llama 2, etc.).

## Core concepts

- **Chinchilla scaling**: train smaller models on more tokens rather than scaling parameters alone.
- **Training data**: public datasets only — CommonCrawl, C4, GitHub, Wikipedia, Books, ArXiv, StackExchange.
- **Architecture modifications**: RMSNorm pre-normalization, SwiGLU activation, rotary positional embeddings (RoPE).
- **Parameter counts**: 7B, 13B, 33B, 65B — designed to be runnable on research hardware.

## Connections

- Foundation model that enabled community fine-tuning experiments including RLHF-based Alpaca and Vicuna.
- Quantization methods (AWQ, SpQR) were benchmarked on LLaMA to show near-lossless 4-bit compression.
- The open release directly contrasts with the closed-weights models discussed in RLHF alignment papers.
- LLaMA-2 (65B) is the model used in SpQR and AWQ compression benchmarks in this corpus.
