## Definition
Retrieval-guided reasoning is an approach in artificial intelligence, particularly in the domain of natural language processing, that involves interleaving information retrieval steps with reasoning processes to enhance the performance of language models in tasks such as multi-step question answering (QA). This method aims to improve the accuracy of information retrieval and the factual correctness of reasoning by integrating retrieval with chain-of-thought (CoT) reasoning.

## Context
The concept of retrieval-guided reasoning has been exemplified by the IRCoT (Interleaving Retrieval with Chain-of-Thought Reasoning) approach, which was introduced to address the limitations of traditional one-step retrieval methods in handling complex, knowledge-intensive multi-step questions. By interleaving retrieval with CoT reasoning, IRCoT has demonstrated significant improvements in both retrieval accuracy and QA performance across various datasets, such as HotpotQA and 2WikiMultihopQA. This approach is effective in reducing model hallucination and enhancing factual accuracy. It performs well even with smaller models like Flan-T5 without requiring additional training. The method significantly enhances retrieval accuracy (up to 21 points) and downstream QA performance (up to 15 points), and it is effective in both in-distribution and out-of-distribution settings.

## Related Concepts
- [[Chain-of-Thought Reasoning]]
- [[Multi-Step Question Answering]]
- [[Large Language Models]]
- [[Open-Domain Question Answering]]
- [[Model Hallucination]]