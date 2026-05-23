## Definition
Data-efficient training refers to methods and strategies that aim to reduce the amount of training data required to achieve a certain level of model performance. This approach is particularly valuable in scenarios where data is scarce, expensive to obtain, or time-consuming to process.

## Context
In the context of machine learning and natural language processing, data-efficient training is crucial for optimizing resource usage while maintaining model accuracy. The concept is highlighted in studies such as the encoder attribution analysis for Dense Passage Retriever (DPR) in open-domain question answering. This analysis demonstrated that a passage encoder could be trained on significantly less data without compromising retrieval accuracy. By understanding the contributions of different components within a model, researchers can design training regimes that focus on the most impactful elements, thus achieving data efficiency.

The paper "An Encoder Attribution Analysis for Dense Passage Retriever in Open-Domain Question Answering" by Minghan Li, Xueguang Ma, and Jimmy J. Lin explores the individual contributions of question and passage encoders in DPR systems. It introduces a probabilistic framework called encoder marginalization to analyze these contributions, revealing that the passage encoder plays a more significant role in retrieval accuracy than the question encoder. The findings suggest that data-efficient training regimes can be developed, reducing training data by up to 60% without losing accuracy.

## Related Concepts
- [[Encoder Attribution]]
- [[Dense Passage Retriever]]
- [[Open-Domain Question Answering]]
- [[Encoder Marginalization]]
- [[SQuAD]]