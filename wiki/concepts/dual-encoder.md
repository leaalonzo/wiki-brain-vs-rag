## Definition
A dual-encoder is a neural network architecture used in natural language processing tasks, particularly for dense passage retrieval and open-domain question answering. It consists of two separate encoders that independently process input pairs, such as a query and a document, to generate embeddings that can be compared using a similarity function.

## Context
Dual-encoders are favored in scenarios where efficiency is crucial, as they allow for pre-computation of document embeddings, enabling rapid retrieval during inference. Unlike cross-encoders, which jointly encode input pairs and often provide higher accuracy, dual-encoders offer a more scalable solution due to their ability to handle large datasets efficiently. Recent advancements, such as ERNIE-Search, have enhanced dual-encoder performance by integrating techniques like self on-the-fly distillation, interaction distillation, and cascade distillation. These methods facilitate knowledge transfer from more expressive models, such as cross-encoders and ColBERT, to dual-encoders, improving their effectiveness in open-domain QA tasks. ERNIE-Search has demonstrated superior performance on QA benchmarks, establishing a new state-of-the-art, particularly on datasets like MS MARCO and Natural Questions.

## Related Concepts
- [[Cross-Encoder]]
- [[ColBERT]]
- [[Open-Domain Question Answering]]
- [[Dense Passage Retrieval]]
- [[Pre-trained Language Models]]
- [[ERNIE-Search]]