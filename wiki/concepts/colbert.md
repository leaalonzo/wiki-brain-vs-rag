## Definition
ColBERT (Contextualized Late Interaction over BERT) is a dense passage retrieval model designed to improve the efficiency and accuracy of information retrieval tasks, particularly in open-domain question answering (QA). It employs BERT-based architectures to perform late interaction between query and document representations, allowing for more precise retrieval of relevant information.

## Context
ColBERT is part of the dual-encoder family of models, which encode queries and documents separately before interaction. Unlike traditional dual-encoders that utilize simple dot-product interactions, ColBERT introduces a sophisticated late interaction mechanism that captures richer contextual information. This design enables ColBERT to balance computational efficiency with retrieval accuracy.

ColBERT has been integrated into various research efforts, such as ERNIE-Search, which employs ColBERT in its self on-the-fly distillation process. This process bridges the gap between cross-encoder and dual-encoder architectures, enhancing dual-encoder performance by leveraging knowledge from more expressive models like cross-encoders. ERNIE-Search has demonstrated superior performance on QA benchmarks, setting new state-of-the-art results on datasets like MS MARCO and Natural Questions.

## Related Concepts
- [[ERNIE-Search]]
- [[Self On-the-Fly Distillation]]
- [[Interaction Distillation]]
- [[Cascade Distillation]]
- [[Dual-Encoder]]
- [[Cross-Encoder]]
- [[Open-Domain Question Answering]]
- [[Dense Passage Retrieval]]
- [[BERT]]