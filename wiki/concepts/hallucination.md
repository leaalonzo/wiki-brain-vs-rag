## Definition
Hallucination, in the context of large language models (LLMs) and large multimodal models (LMMs), refers to the generation of outputs that are factually incorrect or not grounded in reality. This occurs when models produce information that appears plausible but is unsupported by verifiable data or context.

## Context
Hallucination is a significant challenge in deploying LLMs and LMMs, especially for tasks requiring accurate and up-to-date information. In LLMs, hallucinations often arise due to limitations in handling rapidly changing world knowledge and questions based on false premises. The study "FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation" proposes FreshPrompt, a method that incorporates real-time data from search engines to enhance response accuracy on the FreshQA benchmark.

In LMMs, hallucinations can result from multimodal misalignment, where textual outputs are not grounded in the multimodal context. The paper "Aligning Large Multimodal Models with Factually Augmented RLHF" introduces Factually Augmented Reinforcement Learning from Human Feedback (Fact-RLHF) to improve vision-language alignment. This approach enhances the reward model with factual data, such as image captions, to reduce hallucinations and improve model performance, achieving notable results on the LLaVA-Bench and MMHAL-BENCH datasets.

## Related Concepts
- [[FreshQA]]
- [[FreshPrompt]]
- [[In-Context Learning]]
- [[Search Engine Augmentation]]
- [[Dynamic QA Benchmark]]
- [[Large Multimodal Models]]
- [[Multimodal Misalignment]]
- [[Reinforcement Learning from Human Feedback]]
- [[Factually Augmented RLHF]]
- [[Vision-Language Alignment]]
- [[Reward Hacking]]
- [[MMHAL-BENCH]]