## Definition
Few-shot Chain-of-Thought (CoT) is a prompting technique used in large language models (LLMs) to enhance their reasoning capabilities by providing a few examples of step-by-step reasoning. This approach helps the model generate more coherent and accurate responses by mimicking the thought process demonstrated in the examples.

## Context
Few-shot CoT is part of a broader set of techniques aimed at improving the reasoning performance of LLMs. It contrasts with zero-shot CoT methods, which do not rely on manually crafted examples. Few-shot CoT has been shown to be effective in various reasoning tasks, including mathematical problem-solving and commonsense reasoning. However, it requires carefully chosen examples to guide the model, which can be a limitation in scenarios where such examples are not readily available.

Recent advancements, such as Plan-and-Solve (PS) Prompting, have introduced zero-shot methods that aim to achieve similar performance levels without the need for example-based guidance. PS Prompting divides complex tasks into smaller subtasks and provides detailed instructions, addressing common pitfalls in zero-shot CoT, such as calculation errors and missing reasoning steps. PS+ prompting, an extension of PS, achieves performance comparable to 8-shot CoT prompting in arithmetic reasoning tasks without requiring manual examples.

## Related Concepts
- [[Zero-shot Chain-of-Thought]]
- [[Plan-and-Solve Prompting]]
- [[Large Language Models]]
- [[Zero-shot Program-of-Thought]]