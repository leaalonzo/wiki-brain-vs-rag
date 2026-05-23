# bi-encoder

## Definition
A bi-encoder is a neural network architecture used primarily in natural language processing tasks, particularly in dense retrieval systems. It consists of two separate encoders that independently process two different inputs—typically a query and a document or passage—and then project these inputs into a shared embedding space. The similarity between the embeddings is computed to determine the relevance of the document to the query. This architecture is designed to capture semantic relationships between the inputs, making it effective for tasks that require understanding nuanced meanings beyond simple keyword matching.

## Key Mechanisms
Bi-encoders operate by encoding the query and the document into fixed-size vectors using two parallel neural networks, often based on transformer models like BERT or RoBERTa. These vectors are then compared using a similarity measure, such as cosine similarity or dot product, to assess the relevance of the document to the query. The bi-encoder architecture allows for efficient retrieval since the document embeddings can be precomputed and stored, enabling rapid similarity calculations during retrieval.

## Evidence Base
The paper "Hybrid Retrievers with Generative Re-Rankers" by M. Kozłowski (PolEval 2022) provides empirical evidence supporting the effectiveness of bi-encoder architectures in dense retrieval systems. In this study, bi-encoders based on Polish RoBERTa models were used to construct dense indexes that significantly improved the retrieval accuracy by capturing semantic relationships in text. The hybrid system described in the paper, which combines sparse and dense retrieval methods, demonstrated superior performance in passage retrieval tasks, highlighting the bi-encoder's role in enhancing retrieval systems (Kozłowski, 2022).

## Connections to Other Concepts
- [[Dense Retrieval]]: Bi-encoders are a core component of dense retrieval systems, where they are used to create dense vector representations of text.
- [[Sparse Retrieval]]: While bi-encoders are used for dense retrieval, they can be combined with sparse retrieval methods like BM25 to create hybrid systems that leverage the strengths of both approaches.
- [[Generative Re-Ranking]]: After initial retrieval using bi-encoders, generative models can be employed to re-rank the results, as seen in the hybrid retrieval system discussed in the paper.
- [[Neural Information Retrieval]]: Bi-encoders are part of the broader category of neural information retrieval techniques that use neural networks to improve the retrieval process.

## Open Questions
- How can bi-encoder architectures be optimized to handle languages with limited resources effectively?
- What are the trade-offs between computational efficiency and retrieval accuracy in bi-encoder systems?
- How can bi-encoders be integrated with other retrieval and ranking methods to further enhance performance?

## Further Reading
- "Hybrid Retrievers with Generative Re-Rankers" by M. Kozłowski (PolEval 2022) - This paper provides insights into the application of bi-encoders in hybrid retrieval systems and discusses their performance in the context of Polish-language datasets.