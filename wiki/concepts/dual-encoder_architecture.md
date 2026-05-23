## Definition
A dual-encoder architecture is a neural network design used in natural language processing tasks, particularly in retrieval-based systems. It consists of two separate encoders that independently process input pairs, such as questions and passages, to produce vector representations. These vectors are then compared, typically using a similarity measure, to determine the relevance or match between the inputs.

## Context
Dual-encoder architectures are pivotal in dense passage retrieval, a crucial component of open-domain question answering systems. They address the challenge of efficiently matching queries with relevant passages from large corpora. However, training dual-encoder models can be challenging due to discrepancies between training and inference phases, the presence of unlabeled positives, and limited training data.

RocketQA is an optimized training approach that enhances dual-encoder architectures by introducing techniques such as cross-batch negatives, denoised hard negatives, and data augmentation. These innovations help overcome traditional training challenges, leading to improved retrieval performance and end-to-end question answering capabilities. RocketQA has demonstrated significant performance improvements over state-of-the-art models on datasets like MS-MARCO and Natural Questions, highlighting its effectiveness in enhancing dense passage retrieval.

## Related Concepts
- [[Dense Passage Retrieval]]
- [[Open-Domain Question Answering]]
- [[Cross-Encoder]]
- [[Data Augmentation]]
- [[Neural Network Architecture]]
- [[RocketQA]]