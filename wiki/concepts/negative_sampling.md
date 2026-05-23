## Definition
Negative sampling is a technique used in machine learning and natural language processing to efficiently train models by selecting a subset of negative examples (i.e., incorrect or irrelevant data points) from a large pool. This approach helps in improving the model's ability to distinguish between relevant and irrelevant data, particularly in tasks involving large datasets.

## Context
In the context of open-domain question answering (QA) systems, negative sampling is crucial for enhancing the performance of models designed to match questions with relevant passages. Techniques like xMoCo (Cross Momentum Contrastive Learning) leverage negative sampling to maintain a large pool of negative samples efficiently. This is particularly important for optimizing both question-to-passage and passage-to-question matching in dual-encoder models. By selecting appropriate negative examples during training, models can better approximate real-world inference scenarios, leading to improved retrieval accuracy.

## Related Concepts
- [[Contrastive Learning]]
- [[Dense Passage Retrieval]]
- [[Dual-Encoder Model]]
- [[Open-Domain Question Answering]]
- [[Momentum Contrastive Learning]]