## Definition
Interaction distillation is a machine learning technique aimed at enhancing dual-encoder architectures, particularly for open-domain question answering tasks. It involves replicating the interaction patterns of more expressive models, such as ColBERT, within simpler models like dual-encoders to improve their performance.

## Context
Interaction distillation plays a crucial role in narrowing the performance gap between cross-encoder and dual-encoder architectures. This technique is prominently utilized in the ERNIE-Search model, which employs interaction distillation to transfer the sophisticated interaction capabilities of models like ColBERT to dual-encoders. It is used alongside cascade distillation, which facilitates knowledge transfer from cross-encoders to dual-encoders through intermediary models like ColBERT. The goal is to leverage the strengths of pre-trained language models to enhance dense passage retrieval in open-domain question answering, achieving state-of-the-art results on benchmarks such as MS MARCO Passage Ranking and Natural Question (NQ).

## Related Concepts
- [[ERNIE-Search]]
- [[Self On-the-Fly Distillation]]
- [[Cascade Distillation]]
- [[Dual-Encoder]]
- [[Cross-Encoder]]
- [[ColBERT]]
- [[Open-Domain Question Answering]]
- [[Dense Passage Retrieval]]