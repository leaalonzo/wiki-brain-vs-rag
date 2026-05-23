## Definition
ORD-QA Benchmark is an evaluation benchmark developed to assess question-answering (QA) systems specifically tailored to electronic design automation (EDA) tool documentation. It was introduced as part of a customized retrieval augmented generation (RAG) framework designed to enhance the accuracy and quality of QA in the EDA domain.

## Context
The ORD-QA Benchmark was developed in response to the limitations of standard RAG systems when applied to the specialized field of EDA. These systems often lack the domain-specific knowledge necessary to perform effectively in this context. The benchmark is part of a broader effort to create a customized RAG framework that includes enhancements such as contrastive learning for text embedding, a reranker distilled from a proprietary large language model (LLM), and a generative LLM fine-tuned with an EDA domain corpus. The ORD-QA Benchmark consists of 90 high-quality QA pairs and is used to evaluate the performance of these methods, demonstrating superior results compared to existing state-of-the-art approaches in both academic and commercial EDA tools. The benchmark and training dataset are open-source, facilitating further research in this domain.

## Related Concepts
- [[Retrieval Augmented Generation (RAG)]]
- [[Electronic Design Automation (EDA)]]
- [[Contrastive Learning]]
- [[Large Language Model (LLM)]]
- [[Information Retrieval]]
- [[Lexical Retrieval]]
- [[Semantic Retrieval]]
- [[Reciprocal Rank Fusion]]