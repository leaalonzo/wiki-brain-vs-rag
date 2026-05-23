## Definition
A cross-encoder is a type of neural network architecture used in natural language processing tasks, particularly those involving pairwise input, such as question answering and information retrieval. It processes input pairs jointly, allowing for rich interaction between the elements of the pair, which can lead to more accurate predictions compared to models that process inputs independently.

## Context
Cross-encoders are often contrasted with dual-encoders, which process each input element separately and then combine their representations. While cross-encoders can achieve higher accuracy due to their ability to model interactions between inputs, they are typically more computationally expensive. Recent advancements, such as the ERNIE-Search approach, aim to bridge the gap between cross-encoders and dual-encoders by using techniques like self on-the-fly distillation. This method enhances the performance of dual-encoders by transferring knowledge from more expressive models like ColBERT and cross-encoders, leading to improved results in tasks like open-domain question answering. ERNIE-Search introduces interaction and cascade distillation techniques, establishing new state-of-the-art results on QA benchmarks such as MS MARCO and Natural Questions.

## Related Concepts
- [[Dual-Encoder]]
- [[ERNIE-Search]]
- [[ColBERT]]
- [[Open-Domain Question Answering]]
- [[Dense Passage Retrieval]]