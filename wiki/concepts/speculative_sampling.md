## Definition
Speculative sampling is a novel sampling method used in the context of speculative decoding, aimed at accelerating inference in large autoregressive models such as Transformers. It allows for parallel computation of tokens while maintaining the original output distribution, thereby increasing the speed of inference without necessitating changes to the model architecture or retraining.

## Context
Speculative sampling is part of a broader algorithm called speculative decoding, which is designed to enhance the efficiency of inference processes in language models. This method leverages the ability to perform easier subtasks within complex language modeling tasks, using more efficient models for approximation. Speculative sampling plays a crucial role in ensuring that the speed gains from parallel computation do not compromise the accuracy or distribution of the model's outputs. The technique has been demonstrated to achieve significant acceleration, as seen in the T5-XXL model, where it provided a 2X-3X speedup compared to standard implementations.

## Related Concepts
- [[Speculative Decoding]]
- [[Speculative Execution]]
- [[Autoregressive Models]]
- [[Parallel Computation]]
- [[Adaptive Computation Methods]]