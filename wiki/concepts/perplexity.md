## Definition
Perplexity is a measurement used in natural language processing to evaluate the performance of language models. It quantifies how well a model predicts a sample, with lower values indicating better predictive performance.

## Context
In the context of language models, perplexity is often used to assess the accuracy of models like LLaMA and Falcon. Techniques such as SpQR (Sparse-Quantized Representation) aim to compress large language models while maintaining near-lossless accuracy in perplexity. SpQR achieves less than 1% accuracy loss in perplexity by isolating and storing outlier weights in higher precision, allowing models to be efficiently deployed on memory-limited devices without significant performance degradation. This approach enables a 33B parameter LLM to run on a 24 GB consumer GPU with no performance degradation and a 15% speedup, providing a 4x memory compression gain compared to 16-bit baselines.

## Related Concepts
[[Sparse-Quantized Representation]], [[Quantization]], [[LLaMA]], [[Falcon]], [[GPU Inference]], [[Memory Compression]], [[LLM Weight Compression]], [[Outlier Weights]]