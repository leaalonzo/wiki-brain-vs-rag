## Definition
Reasoning tasks involve the cognitive process of drawing conclusions, making inferences, or solving problems based on given information. In the context of artificial intelligence, particularly large language models (LLMs), reasoning tasks require the model to process and analyze information to arrive at logical conclusions or solutions.

## Context
The development of advanced prompting strategies for LLMs has significantly enhanced their ability to perform reasoning tasks. Traditional Zero-shot Chain-of-Thought (CoT) prompting has been used to enable LLMs to reason without prior examples. However, this method has limitations, such as calculation errors, missing-step errors, and semantic misunderstanding errors. To address these issues, the Plan-and-Solve (PS) prompting strategy was introduced, which involves a two-step process of planning and executing subtasks. This structured approach improves reasoning accuracy in zero-shot settings. The PS+ prompting further refines this method by providing detailed instructions to mitigate errors and enhance reasoning quality. PS+ prompting has shown to consistently outperform Zero-shot-CoT and achieve performance similar to 8-shot CoT prompting in arithmetic reasoning tasks without requiring manual examples. These advancements have been tested across various datasets and have shown improved performance over traditional Zero-shot-CoT and comparable results to few-shot CoT prompting.

## Related Concepts
- [[Plan-and-Solve Prompting]]
- [[Zero-shot-CoT]]
- [[PS+ Prompting]]
- [[Large Language Models]]
- [[Few-shot CoT Prompting]]
- [[Zero-shot-Program-of-Thought]]
- [[Commonsense Reasoning]]
- [[Symbolic Reasoning]]