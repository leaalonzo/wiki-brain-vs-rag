## Definition
Plan-and-Solve (PS) Prompting is a zero-shot chain-of-thought (CoT) prompting method designed to enhance the reasoning capabilities of large language models (LLMs). It improves performance by dividing complex tasks into smaller subtasks with a structured approach, thus eliminating the need for manually crafted examples.

## Context
PS Prompting addresses the limitations of traditional zero-shot CoT methods, which often suffer from calculation errors, missing reasoning steps, and semantic misunderstandings. By employing a two-step process of planning and executing subtasks, PS Prompting enhances reasoning accuracy. The PS+ variant further refines this method by incorporating detailed instructions to mitigate calculation errors and improve the quality of reasoning steps. This makes it suitable for a wide range of reasoning tasks, including mathematical, commonsense, and symbolic reasoning. Experimental evaluations demonstrate that PS Prompting consistently outperforms Zero-shot-CoT methods and is competitive with few-shot CoT approaches, with PS+ even surpassing few-shot manual-CoT prompting on certain datasets. PS+ prompting achieves performance similar to 8-shot CoT prompting in arithmetic reasoning tasks without requiring manual examples. The method has been evaluated on ten datasets across three reasoning problems, showing significant improvements.

## Related Concepts
- [[Zero-shot Chain-of-Thought]]
- [[Few-shot Chain-of-Thought]]
- [[Zero-shot Program-of-Thought]]
- [[Large Language Models]]