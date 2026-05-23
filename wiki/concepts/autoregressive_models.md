## Definition
Autoregressive models are a class of models used in machine learning and statistics where the output depends on its own previous outputs. These models generate data sequences one step at a time, predicting the next element in the sequence based on the preceding elements.

## Context
Autoregressive models are widely used in natural language processing (NLP) tasks, particularly in generating text, where each word or token is predicted based on the sequence of words or tokens that precede it. Transformers, a popular architecture for NLP, often employ autoregressive models for tasks such as language translation, text generation, and more.

The paper "Fast Inference from Transformers via Speculative Decoding" introduces speculative decoding, a novel algorithm designed to enhance the efficiency of inference in large autoregressive models like Transformers. Speculative decoding allows for the parallel computation of tokens, significantly speeding up the process without altering the output distribution. This method can be applied to existing models without requiring retraining or architectural changes, making it practical for production settings.

## Related Concepts
- [[Speculative Decoding]]
- [[Transformers]]
- [[Parallel Computation]]
- [[Natural Language Processing]]
- [[Adaptive Computation Methods]]