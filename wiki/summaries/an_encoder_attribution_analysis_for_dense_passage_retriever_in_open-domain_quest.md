```markdown
## Overview
The paper "An Encoder Attribution Analysis for Dense Passage Retriever in Open-Domain Question Answering" by Minghan Li, Xueguang Ma, and Jimmy J. Lin explores the individual contributions of question and passage encoders in Dense Passage Retriever (DPR) systems. The study introduces a probabilistic framework called encoder marginalization to analyze these contributions, revealing that the passage encoder plays a more significant role in retrieval accuracy than the question encoder. The findings suggest ways to optimize training data usage without compromising performance.

## Key Points
- The study addresses the encoder attribution problem in DPR, focusing on the individual contributions of question and passage encoders.
- A probabilistic framework, encoder marginalization, is used to quantify each encoder's contribution by marginalizing other variables.
- The passage encoder is found to contribute more to in-domain retrieval accuracy than the question encoder.
- Positive passage overlap and corpus coverage significantly impact the passage encoder, while the question encoder is affected by training sample complexity.
- Data-efficient training regimes can be developed, reducing training data by up to 60% without losing accuracy.

## Concepts Introduced
encoder attribution, dense passage retriever, encoder marginalization, probabilistic framework, data-efficient training

## Quotes or Data
- "We manage to train a passage encoder on SQuAD using 60% less training data without loss of accuracy."
```
