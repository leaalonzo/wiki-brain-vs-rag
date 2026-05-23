## Definition
A dual-encoder model is a neural network architecture that utilizes two separate encoders to independently process and encode different types of input data into vector representations. This model is commonly used in tasks that involve matching or comparing two distinct types of data, such as questions and passages in information retrieval systems.

## Context
Dual-encoder models are particularly effective in scenarios where it is necessary to encode and compare two different inputs, such as in open-domain question answering systems. In these systems, the dual-encoder model encodes questions and passages separately, allowing for efficient retrieval through vector space search. The xMoCo method, or Cross Momentum Contrastive Learning, enhances the dual-encoder model's ability to match questions with relevant passages by efficiently managing negative samples. xMoCo builds on the dense passage retrieval paradigm and optimizes both question-to-passage and passage-to-question matching tasks using separate encoders for questions and passages. This method has demonstrated effectiveness across various QA datasets.

## Related Concepts
- [[Contrastive Learning]]
- [[Dense Passage Retrieval]]
- [[Momentum Contrastive Learning]]
- [[Question-Passage Matching]]
- [[Negative Sampling]]
- [[Vector Space Search]]
- [[xMoCo]]