## Definition
Cross-batch negatives are a training technique used in machine learning, particularly in dense passage retrieval for open-domain question answering systems. This method increases the number of negative samples available during training by leveraging examples from multiple batches, rather than limiting to negatives within a single batch.

## Context
Cross-batch negatives are a key component of the RocketQA training approach, which optimizes the performance of dual-encoder architectures in dense passage retrieval. This technique addresses challenges such as the discrepancy between training and inference, the presence of unlabeled positives, and limited training data. By incorporating cross-batch negatives, RocketQA enhances the model's ability to distinguish between relevant and irrelevant passages, improving retrieval performance and reducing the risk of overfitting. RocketQA also introduces denoised hard negatives and data augmentation to further boost model performance, demonstrating significant improvements on datasets like MS-MARCO and Natural Questions.

## Related Concepts
[[RocketQA]], [[Dense Passage Retrieval]], [[Dual-Encoder Architecture]], [[Denoised Hard Negatives]], [[Data Augmentation]], [[Open-Domain Question Answering]], [[Semantic Matching]]