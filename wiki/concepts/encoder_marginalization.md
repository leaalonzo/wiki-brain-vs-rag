## Definition
Encoder marginalization is a probabilistic framework used to quantify the contribution of individual components within a system by marginalizing other variables. In neural networks, it is applied to understand the roles of different encoders in models such as the Dense Passage Retriever (DPR).

## Context
In open-domain question answering, the Dense Passage Retriever utilizes two main components: a question encoder and a passage encoder. Encoder marginalization is employed to analyze the attribution of each encoder to the overall performance of the system. Studies, such as "An Encoder Attribution Analysis for Dense Passage Retriever in Open-Domain Question Answering" by Minghan Li, Xueguang Ma, and Jimmy J. Lin, have shown that the passage encoder has a more substantial impact on in-domain retrieval accuracy compared to the question encoder. The passage encoder is particularly influenced by positive passage overlap and corpus coverage, while the question encoder is affected by training sample complexity. This analysis aids in developing data-efficient training regimes, allowing for effective model training with up to 60% reduced data requirements without compromising accuracy.

## Related Concepts
- [[Encoder Attribution]]
- [[Dense Passage Retriever]]
- [[Open-Domain Question Answering]]
- [[Data-Efficient Training]]