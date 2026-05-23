## Definition
Speculative decoding is an algorithm designed to accelerate inference in large autoregressive models, such as Transformers. It achieves this by enabling the parallel computation of multiple tokens, thereby speeding up the process without altering the output distribution. This method can be applied to existing models without necessitating retraining or changes to the model architecture.

## Context
Speculative decoding was introduced in the paper "Fast Inference from Transformers via Speculative Decoding." The algorithm leverages easier subtasks within complex language-modeling tasks, using more efficient models for approximation. It employs speculative execution and a novel sampling method known as speculative sampling to maintain the original output distribution while increasing the speed of inference. The method has been demonstrated on models like T5-XXL, achieving a 2X-3X acceleration compared to standard implementations.

## Related Concepts
- [[Autoregressive Models]]
- [[Parallel Computation]]
- [[Speculative Execution]]
- [[Adaptive Computation Methods]]
- [[Transformers]]