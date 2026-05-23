## Definition
Retrieval Augmented Generation (RAG) is a machine learning approach that combines information retrieval with text generation. It enhances the capabilities of generative models by incorporating relevant external information retrieved from a database or corpus, thereby improving the accuracy and relevance of the generated content.

## Context
RAG systems are particularly useful in domains where the generative model alone may lack sufficient domain-specific knowledge. A notable application is in electronic design automation (EDA), where standard RAG systems face challenges due to the specialized nature of the field. Customized RAG frameworks have been developed to address these limitations by integrating domain-specific techniques, such as contrastive learning for text embedding and fine-tuning large language models (LLMs) with domain-specific corpora. These enhancements aim to improve both retrieval accuracy and the quality of question-answering (QA) systems in specialized fields.

The paper "Customized Retrieval Augmented Generation and Benchmarking for EDA Tool Documentation QA" highlights the limitations of general-purpose RAG systems in knowledge-intensive domains like EDA. It proposes a customized RAG framework tailored for EDA tool documentation QA, incorporating a contrastive learning scheme, a reranker model distilled from proprietary LLMs, and a generative LLM fine-tuned with an EDA domain corpus. Additionally, a two-stage training scheme involving domain-knowledge pre-training and task-specific instruction tuning is introduced. The ORD-QA benchmark is developed to evaluate this framework, demonstrating superior performance on both academic and commercial EDA tools.

## Related Concepts
- [[Electronic Design Automation (EDA)]]
- [[Contrastive Learning]]
- [[Large Language Model (LLM)]]
- [[Information Retrieval]]
- [[Lexical Retrieval]]
- [[Semantic Retrieval]]
- [[Reciprocal Rank Fusion]]
- [[Text Embedding Model]]
- [[Reranker Model]]
- [[Domain-Specific Fine-Tuning]]
- [[ORD-QA Benchmark]]