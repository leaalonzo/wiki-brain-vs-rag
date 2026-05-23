## Definition
PS+ Prompting is an advanced prompting strategy for large language models (LLMs) designed to enhance reasoning capabilities in zero-shot settings. It extends the Plan-and-Solve (PS) prompting method by providing detailed instructions to address calculation errors and improve reasoning quality.

## Context
PS+ Prompting was introduced in the paper "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models." This method aims to overcome the limitations of Zero-shot Chain-of-Thought (CoT) prompting, which include calculation errors, missing-step errors, and semantic misunderstanding errors. By incorporating a structured approach that involves planning and executing subtasks, PS+ Prompting improves reasoning accuracy. It can be adapted for various reasoning tasks beyond mathematics, such as commonsense and symbolic reasoning. The strategy has been evaluated on ten datasets across three reasoning problems, demonstrating superior performance over Zero-shot-CoT and comparable results to few-shot CoT prompting. PS+ Prompting achieves performance similar to 8-shot CoT prompting in arithmetic reasoning tasks without requiring manual examples.

## Related Concepts
- [[Plan-and-Solve Prompting]]
- [[Zero-shot-CoT]]
- [[Large Language Models]]
- [[Reasoning Tasks]]
- [[Few-shot CoT Prompting]]
- [[Zero-shot-Program-of-Thought]]