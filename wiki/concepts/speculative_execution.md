## Definition
Speculative execution is a computational technique used to improve the efficiency and speed of processing tasks by executing multiple potential future steps in parallel. In the context of machine learning, it is used to accelerate inference from large autoregressive models, such as Transformers, by predicting and computing multiple tokens simultaneously without altering the output distribution.

## Context
The concept of speculative execution is applied in the paper "Fast Inference from Transformers via Speculative Decoding," which introduces speculative decoding as a method to speed up inference in large language models. This technique leverages easier subtasks within complex language-modeling tasks, allowing for parallel computation of tokens and achieving significant acceleration in processing time. The method is demonstrated on the T5-XXL model, achieving a 2X-3X speed increase compared to standard implementations, while maintaining identical outputs. Importantly, speculative execution can be integrated into existing models without requiring retraining or architectural modifications.

## Related Concepts
- [[Speculative Decoding]]
- [[Speculative Sampling]]
- [[Autoregressive Models]]
- [[Parallel Computation]]
- [[Adaptive Computation Methods]]