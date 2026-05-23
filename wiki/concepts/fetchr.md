## Definition
FetcHR is a document retrieval system designed to enhance question-answering systems by utilizing hierarchical representations from all layers of a transformer network. It integrates retrieval into each layer, leveraging the different levels of abstraction to improve the quality of retrieved documents.

## Context
FetcHR addresses limitations in traditional dense passage retrieval (DPR) by focusing on critical features in questions that are often underrepresented in retrieved documents. By utilizing hidden representations from each layer of a transformer, FetcHR contributes to the retrieval query, demonstrating that combining retrieval from all layers outperforms retrieval from individual layers. This approach enhances the performance of question-answering benchmarks such as the Natural Question and WebQuestion datasets, achieving state-of-the-art performance with improvements of up to 1.9 EM score on Natural Question and 2.1 EM score on WebQuestion. The method involves training only the retrieval networks, avoiding modifications to the underlying language model. FetcHR uses a retrieval score based on the inner product between encoded question and document vectors at each layer, allowing it to retrieve multiple documents per layer from the document memory.

## Related Concepts
- [[Hierarchical Representations]]
- [[Dense Passage Retrieval]]
- [[Transformer Networks]]
- [[Question-Answering Systems]]
- [[Retrieval Score]]
- [[Contrastive Training]]