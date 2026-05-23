## Definition
Outlier weights refer to specific parameters within a machine learning model that cause disproportionately large quantization errors when the model is compressed. These weights are typically isolated and stored in higher precision to maintain the model's accuracy during inference.

## Context
In the context of compressing large language models (LLMs), outlier weights are crucial for achieving near-lossless accuracy. Techniques like Sparse-Quantized Representation (SpQR) identify these outlier weights and handle them separately from the rest of the model's parameters. By isolating and storing outlier weights in higher precision while compressing other weights to 3-4 bits, SpQR enables the deployment of large models on memory-limited devices without significant performance degradation. This approach achieves less than 1% accuracy loss in perplexity for models such as LLaMA and Falcon, allowing a 33B parameter LLM to run on a 24 GB consumer GPU with no performance degradation and a 15% speedup. SpQR provides a 4x memory compression gain compared to 16-bit baselines.

## Related Concepts
[[Sparse-Quantized Representation]], [[Quantization]], [[Perplexity]], [[LLaMA]], [[Falcon]], [[GPU Inference]], [[Memory Compression]]