## Definition
Self on-the-fly distillation is a machine learning technique aimed at improving the performance of dual-encoder architectures by dynamically transferring knowledge from more expressive models, such as cross-encoders and ColBERT, during the training process.

## Context
Self on-the-fly distillation is a key component of the ERNIE-Search approach, which enhances dense passage retrieval in open-domain question answering (QA). This technique effectively bridges the gap between cross-encoder and dual-encoder architectures, allowing dual-encoders to benefit from the strengths of more complex models without significant computational costs. It employs interaction distillation to mimic late interaction in dual-encoders and cascade distillation for stepwise knowledge transfer from cross-encoders to dual-encoders via ColBERT. Extensive experiments demonstrate that ERNIE-Search, utilizing self on-the-fly distillation, outperforms existing baselines and sets new benchmarks on large-scale QA datasets like MS MARCO Passage Ranking and Natural Question (NQ).

## Related Concepts
- [[ERNIE-Search]]
- [[Interaction Distillation]]
- [[Cascade Distillation]]
- [[Dual-Encoder]]
- [[Cross-Encoder]]
- [[ColBERT]]
- [[Open-Domain Question Answering]]
- [[Dense Passage Retrieval]]