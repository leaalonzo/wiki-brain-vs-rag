---
title: "Attention Is All You Need"
authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Lukasz Kaiser", "Illia Polosukhin"]
year: 2017
abstract: "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature."
source_url: "https://arxiv.org/abs/1706.03762"
pdf_url: "https://arxiv.org/pdf/1706.03762"
doi: "10.48550/arXiv.1706.03762"
query_tag: "transformers"
license: "CC BY 4.0"
---

# Attention Is All You Need

Vaswani et al., 2017 · arXiv:1706.03762

## Abstract

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.

## Key contributions

- Introduces the Transformer architecture based entirely on self-attention, removing recurrence and convolutions.
- Multi-head attention allows the model to attend to information from different representation subspaces simultaneously.
- Positional encodings substitute for recurrence to retain sequence order information.
- Achieves state-of-the-art results on machine translation with significantly lower training compute.

## Core concepts

- **Self-attention**: each position in the sequence attends to all other positions to compute its representation.
- **Multi-head attention**: h parallel attention heads, each learning different attention patterns.
- **Scaled dot-product attention**: `Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V`
- **Encoder-decoder architecture**: encoder maps input to continuous representations; decoder generates output autoregressively.
- **Positional encoding**: sine and cosine functions of different frequencies added to token embeddings.

## Connections

- Foundation for all modern large language models (GPT, BERT, T5, LLaMA).
- Self-attention is the mechanism that RAG systems rely on to integrate retrieved context.
- The parallelizability of Transformers (vs. RNNs) enabled the large-scale pretraining that led to emergent abilities.
