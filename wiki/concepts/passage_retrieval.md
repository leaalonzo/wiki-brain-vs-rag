# Passage Retrieval

## Definition
Passage retrieval is a critical component of information retrieval systems, particularly in the context of open-domain question answering (QA) and tasks requiring external knowledge. It involves identifying and retrieving relevant text passages from a large corpus in response to a specific query. The goal is to find the most pertinent information that can answer a question or fulfill an information need, often from unstructured data sources.

## Key Mechanisms
Passage retrieval systems typically employ a combination of sparse and dense retrieval methods:

1. **Sparse Retrieval**: This traditional approach relies on lexical matching, where algorithms like BM25 are used to retrieve passages based on keyword overlap between the query and the documents. Sparse retrieval is robust in zero-shot or few-shot scenarios due to its reliance on exact term matching.

2. **Dense Retrieval**: This method uses neural networks to map queries and documents into a shared vector space, allowing for semantic matching beyond exact keyword overlap. Dense retrieval models, such as those based on bi-encoder architectures, are capable of capturing semantic relationships in text, improving retrieval accuracy.

3. **Generative Re-Ranking**: After initial retrieval, a re-ranking step can be employed using generative models to assess the relevance of passages more deeply. This process involves scoring the passages to retain only the most relevant ones, often using advanced models like mt5-13b-mmarco.

## Evidence Base
- The paper "Hybrid Retrievers with Generative Re-Rankers" demonstrates the effectiveness of combining sparse (BM25) and dense retrieval methods with generative re-ranking to enhance passage retrieval performance. The hybrid approach leverages the strengths of both retrieval methods and addresses the limitations of traditional lexical approaches (Kozłowski, PolEval 2022).

- In "Passage Retrieval for Outside-Knowledge Visual Question Answering," dense retrieval using a dual-encoder architecture significantly outperforms sparse retrieval methods in tasks requiring external knowledge for visual question answering. This research highlights the potential of dense retrieval in handling multi-modal information needs (Chen Qu et al.).

## Connections to Other Concepts
- [[Open-domain Question Answering]]: Passage retrieval is a foundational element in open-domain QA systems, where it is used to extract relevant information from large, unstructured collections.
- [[Sparse Retrieval]]: A traditional method often used in passage retrieval, particularly effective in scenarios with limited data.
- [[Dense Retrieval]]: An advanced retrieval method that enhances semantic understanding and is crucial for tasks involving complex information needs.
- [[Generative Re-Ranking]]: A process that refines initial retrieval results by evaluating passage relevance through generative models.

## Open Questions
- How can passage retrieval systems be further optimized to handle languages with limited resources, such as Polish?
- What are the potential benefits and challenges of integrating multi-modal data in passage retrieval systems beyond visual question answering?
- How can the scalability of dense retrieval methods be improved to handle ever-growing datasets efficiently?

## Further Reading
- "Hybrid Retrievers with Generative Re-Rankers" by M. Kozłowski, PolEval 2022.
- "Passage Retrieval for Outside-Knowledge Visual Question Answering" by Chen Qu et al.