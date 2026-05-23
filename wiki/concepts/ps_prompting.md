# PS+ Prompting

## Definition
PS+ Prompting is an advanced method designed to enhance the reasoning capabilities of large language models (LLMs) in zero-shot scenarios. It builds upon the Plan-and-Solve (PS) prompting technique by incorporating detailed instructions to further reduce errors and improve the quality of reasoning. This approach allows LLMs to break down complex tasks into smaller, manageable subtasks, thereby improving accuracy without the need for manually crafted examples.

## Key Mechanisms
PS+ Prompting operates through a two-step process:
1. **Planning**: The model devises a structured plan to tackle the given task by identifying and organizing the necessary subtasks. This step aims to mitigate common errors such as calculation mistakes, missing steps, and semantic misunderstandings.
2. **Solving**: The model executes the subtasks as per the devised plan, ensuring a more accurate and coherent reasoning process.

The PS+ extension enhances this process by providing more detailed instructions, which help the model to further minimize errors and improve performance in reasoning tasks.

## Evidence Base
The concept of PS+ Prompting is primarily supported by the paper "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models." The paper demonstrates that PS+ Prompting consistently outperforms Zero-shot Chain-of-Thought (CoT) prompting across various datasets and reasoning problems. Notably, PS+ Prompting achieves performance comparable to 8-shot CoT prompting in arithmetic reasoning tasks without requiring manual examples.

## Connections to Other Concepts
- [[Zero-shot Chain-of-Thought]]: PS+ Prompting is an enhancement of Zero-shot CoT, addressing its limitations by introducing a structured planning phase.
- [[Few-shot Chain-of-Thought]]: While PS+ Prompting operates in a zero-shot context, its performance is comparable to few-shot methods, such as 8-shot CoT, in certain tasks.
- [[Zero-shot-Program-of-Thought]]: PS+ Prompting is shown to be comparable to or exceed the performance of Zero-shot PoT prompting, another method aimed at improving reasoning in LLMs.
- [[Large Language Models]]: PS+ Prompting is specifically designed to enhance the reasoning capabilities of LLMs, such as GPT-3.

## Open Questions
- How can PS+ Prompting be further optimized to handle a broader range of reasoning tasks beyond arithmetic?
- What are the limitations of PS+ Prompting in terms of scalability and applicability to different types of LLMs?
- Can the principles of PS+ Prompting be integrated into other areas of AI, such as natural language understanding or generation?

## Further Reading
- "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models" - This paper provides a comprehensive overview of the PS+ Prompting method and its evaluation across various datasets and reasoning problems.