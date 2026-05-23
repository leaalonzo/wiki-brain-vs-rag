## Definition
Dense Passage Retriever (DPR) is a neural network-based model used in open-domain question answering systems. It consists of two main components: a question encoder and a passage encoder. These encoders transform questions and passages into dense vector representations, enabling efficient retrieval of relevant passages from a large corpus.

## Context
In open-domain question answering, retrieving relevant passages quickly and accurately is crucial. DPR addresses this by using dense vector representations to match questions with passages. Recent studies, such as the encoder attribution analysis, have highlighted the importance of understanding the individual contributions of the question and passage encoders to the overall performance of DPR. The analysis revealed that the passage encoder plays a more significant role in retrieval accuracy, particularly in in-domain settings. A probabilistic framework called encoder marginalization has been introduced to quantify each encoder's contribution, revealing that positive passage overlap and corpus coverage significantly impact the passage encoder. Additionally, data-efficient training regimes have been proposed, allowing the passage encoder to be trained with significantly less data without compromising accuracy.

## Related Concepts
- [[Open-Domain Question Answering]]
- [[Neural Network]]
- [[Encoder Attribution]]
- [[Encoder Marginalization]]
- [[Data-Efficient Training]]