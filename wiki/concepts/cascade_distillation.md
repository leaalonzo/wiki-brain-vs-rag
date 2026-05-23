## Definition
Cascade distillation is a machine learning technique used to transfer knowledge from complex models to simpler ones. It involves a sequential process where knowledge is distilled from a high-capacity model, such as a cross-encoder, to an intermediate model, like ColBERT, and finally to a simpler model, such as a dual-encoder.

## Context
Cascade distillation is employed in the field of open-domain question answering (QA) to enhance the performance of dual-encoder architectures. By leveraging the expressive capabilities of cross-encoders and the efficient retrieval abilities of dual-encoders, cascade distillation helps bridge the gap between these architectures. This technique is part of the ERNIE-Search approach, which aims to improve dense passage retrieval by using pre-trained language models and innovative distillation methods. ERNIE-Search introduces self on-the-fly distillation and interaction distillation to further enhance dual-encoder performance, achieving state-of-the-art results on QA benchmarks like MS MARCO and Natural Questions.

## Related Concepts
[[ERNIE-Search]], [[Self On-the-Fly Distillation]], [[Interaction Distillation]], [[Dual-Encoder]], [[Cross-Encoder]], [[ColBERT]], [[Open-Domain Question Answering]], [[Dense Passage Retrieval]]