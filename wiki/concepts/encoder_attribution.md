## Definition
Encoder attribution refers to the analysis of the individual contributions of different encoders within a machine learning model, particularly in systems like the Dense Passage Retriever (DPR) used in open-domain question answering. It involves assessing the impact of each encoder on the model's overall performance, often using frameworks like encoder marginalization.

## Context
In the context of open-domain question answering, encoder attribution is essential for understanding how different components of a model contribute to its effectiveness. The Dense Passage Retriever (DPR) utilizes two main encoders: the question encoder and the passage encoder. Research has shown that the passage encoder plays a more significant role in retrieval accuracy compared to the question encoder. Factors such as positive passage overlap and corpus coverage heavily influence the passage encoder, while the complexity of training samples affects the question encoder. Insights from encoder attribution have led to the development of data-efficient training regimes, enabling the training of a passage encoder on datasets like SQuAD with significantly reduced data without compromising accuracy.

## Related Concepts
- [[Dense Passage Retriever]]
- [[Open-Domain Question Answering]]
- [[Encoder Marginalization]]
- [[Data-Efficient Training]]