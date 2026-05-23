## Definition
Zero-shot Program-of-Thought (PoT) is an advanced prompting method designed to improve the reasoning capabilities of large language models (LLMs) without relying on manually crafted examples. It involves breaking down complex tasks into smaller, manageable subtasks and providing detailed instructions to guide the reasoning process.

## Context
Zero-shot PoT builds upon the principles of Zero-shot Chain-of-Thought (CoT) prompting, which aims to enable LLMs to perform reasoning tasks without prior examples. However, Zero-shot CoT often encounters issues such as calculation errors, missing reasoning steps, and semantic misunderstandings. To address these challenges, Zero-shot PoT introduces Plan-and-Solve (PS) Prompting, which enhances the reasoning process by devising a plan and executing subtasks according to that plan. This method has been shown to outperform traditional Zero-shot CoT and is competitive with few-shot CoT approaches, particularly in math reasoning tasks. Additionally, PS+ Prompting, an extension of PS, further refines the reasoning quality by incorporating detailed instructions.

## Related Concepts
- [[Zero-shot Chain-of-Thought]]
- [[Few-shot Chain-of-Thought]]
- [[Large Language Models]]
- [[Plan-and-Solve Prompting]]