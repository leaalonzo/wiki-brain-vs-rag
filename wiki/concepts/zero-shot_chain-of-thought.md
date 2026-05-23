## Definition
Zero-shot Chain-of-Thought (CoT) is a prompting method used in large language models (LLMs) to enhance their reasoning capabilities without relying on manually crafted examples. It involves generating a sequence of reasoning steps to solve complex tasks directly from the prompt, without prior examples or training on similar tasks.

## Context
Zero-shot CoT is part of a broader effort to improve the reasoning and problem-solving abilities of LLMs. Traditional zero-shot methods often struggle with calculation errors, missing reasoning steps, and semantic misunderstandings. To address these issues, Plan-and-Solve (PS) Prompting has been developed as a novel zero-shot CoT approach. PS Prompting divides tasks into smaller subtasks and provides detailed instructions, resulting in improved reasoning performance. This method has been shown to outperform traditional zero-shot CoT and is competitive with few-shot CoT methods, particularly in mathematical reasoning tasks. PS+ prompting, an extension of PS prompting, further reduces errors and enhances reasoning quality, achieving performance similar to 8-shot CoT prompting in arithmetic reasoning tasks without requiring manual examples.

## Related Concepts
- [[Plan-and-Solve Prompting]]
- [[Few-shot Chain-of-Thought]]
- [[Zero-shot Program-of-Thought]]
- [[Large Language Models]]
- [[Reasoning Tasks]]
- [[Subtasks]]
- [[PS+ Prompting]]