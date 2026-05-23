## Definition
ERNIE-Search is an innovative approach designed to enhance dense passage retrieval in open-domain question answering (QA). It integrates cross-encoder and dual-encoder architectures using a self on-the-fly distillation method, which facilitates the transfer of knowledge from more expressive models to dual-encoders, thereby improving their performance.

## Context
ERNIE-Search leverages pre-trained language models (PLMs) to boost the effectiveness of dual-encoders in open-domain QA. The method introduces interaction and cascade distillation techniques to bridge the gap between cross-encoder and dual-encoder architectures. Interaction distillation allows dual-encoders to mimic the late interaction capabilities of models like [[ColBERT]], while cascade distillation transfers knowledge from cross-encoders to dual-encoders via ColBERT. This approach addresses the structural differences between teacher and student models in cross-architecture distillation. Extensive experiments have demonstrated that ERNIE-Search outperforms existing methods and sets new benchmarks on large-scale QA datasets, such as [[MS MARCO Passage Ranking]] and [[Natural Question (NQ)]], establishing a new state-of-the-art.

## Related Concepts
- [[Self On-the-Fly Distillation]]
- [[Interaction Distillation]]
- [[Cascade Distillation]]
- [[Dual-Encoder]]
- [[Cross-Encoder]]
- [[ColBERT]]
- [[Open-Domain Question Answering]]
- [[Dense Passage Retrieval]]