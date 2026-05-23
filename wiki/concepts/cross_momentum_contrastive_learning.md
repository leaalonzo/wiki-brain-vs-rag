## Definition
Cross Momentum Contrastive Learning (xMoCo) is a novel contrastive learning technique specifically designed for open-domain question answering (QA) systems. It enhances the dual-encoder model's capability to efficiently match questions with relevant passages by leveraging a large pool of negative samples.

## Context
xMoCo is an advancement in the field of dense passage retrieval within open-domain QA. It builds upon the principles of momentum contrastive learning, originally used in computer vision, and adapts them to the unique challenges of QA tasks. The method focuses on optimizing both question-to-passage and passage-to-question matching, enabling the use of separate encoders for questions and passages. This approach is particularly beneficial for maintaining a large pool of negative samples, which is crucial for training robust QA systems. xMoCo has been evaluated on various open-domain QA datasets, demonstrating its effectiveness in improving retrieval accuracy.

## Related Concepts
- [[Dense Passage Retrieval]]
- [[Dual-Encoder Model]]
- [[Momentum Contrastive Learning]]
- [[Open-Domain Question Answering]]
- [[Negative Sampling]]
- [[Vector Space Search]]