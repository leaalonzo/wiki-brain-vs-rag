## Definition
Zero-shot-Program-of-Thought (PoT) is a prompting technique used in large language models (LLMs) to enhance reasoning capabilities without the need for manually crafted examples. It builds upon the principles of Zero-shot Chain-of-Thought (CoT) by allowing the model to generate reasoning steps autonomously, aiming to improve the accuracy of complex reasoning tasks.

## Context
Zero-shot-Program-of-Thought is part of a broader effort to improve the reasoning performance of LLMs in zero-shot scenarios, where the model has not been explicitly trained on specific examples of the task at hand. Traditional Zero-shot-CoT techniques have been limited by calculation errors, missing-step errors, and semantic misunderstanding errors. The introduction of Plan-and-Solve (PS) prompting and its extension, PS+ prompting, has shown that these limitations can be addressed by breaking down tasks into smaller, manageable subtasks. PS+ prompting, in particular, has demonstrated performance comparable to 8-shot CoT prompting in arithmetic reasoning tasks, without the need for manual examples.

## Related Concepts
- [[Zero-shot Chain-of-Thought]]
- [[Few-shot Chain-of-Thought]]
- [[Plan-and-Solve Prompting]]
- [[Large Language Models]]
- [[Reasoning Tasks]]
- [[Subtasks]]