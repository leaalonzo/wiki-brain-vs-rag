## Definition
A retrieval score is a metric used to evaluate the relevance of documents retrieved in response to a query. In dense passage retrieval systems, it is typically calculated using the inner product between encoded vectors of the query and the documents. This score helps determine which documents are most relevant to the query, guiding the selection of documents for further processing or answer generation.

## Context
Retrieval scores are fundamental in information retrieval systems, particularly in question-answering systems that rely on dense passage retrieval (DPR). These systems use transformer networks to encode both questions and documents into dense vectors. The retrieval score is then computed to assess the similarity between these vectors, helping to identify documents that are likely to contain the correct answers.

In advanced systems like FetcHR, retrieval scores are calculated at multiple layers of a transformer network, leveraging hierarchical representations to improve retrieval accuracy. This approach allows for a more nuanced understanding of the query and documents, enhancing the performance of question-answering benchmarks. FetcHR demonstrates state-of-the-art performance by integrating retrieval at each layer of a transformer network, leading to improved results on datasets such as Natural Question and WebQuestion.

## Related Concepts
- [[Dense Passage Retrieval]]
- [[Transformer Networks]]
- [[Question-Answering Systems]]
- [[Hierarchical Representations]]
- [[Contrastive Training]]
- [[FetcHR]]