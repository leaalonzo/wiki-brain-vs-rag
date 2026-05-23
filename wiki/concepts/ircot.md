## Definition
IRCoT (Interleaving Retrieval with Chain-of-Thought) is an advanced method designed to enhance the performance of large language models (LLMs) in multi-step question answering (QA). It improves retrieval accuracy and factual correctness by interleaving retrieval steps with chain-of-thought (CoT) reasoning.

## Context
IRCoT addresses the limitations of traditional one-step retrieval methods by integrating retrieval with CoT reasoning. This approach allows for more relevant information retrieval and improved reasoning accuracy. The method significantly enhances retrieval accuracy (up to 21 points) and downstream QA performance (up to 15 points) across multiple datasets such as HotpotQA, 2WikiMultihopQA, MuSiQue, and IIRC. IRCoT is effective in both in-distribution and out-of-distribution settings and performs well with smaller models like Flan-T5-large without requiring additional training. It also reduces model hallucination, leading to more factually accurate CoT reasoning. The approach outperforms traditional one-step question-based retrieval, especially in complex multi-step reasoning tasks.

## Related Concepts
- [[Chain-of-Thought Reasoning]]
- [[Multi-Step Question Answering]]
- [[Large Language Models]]
- [[Retrieval-Guided Reasoning]]
- [[Model Hallucination]]