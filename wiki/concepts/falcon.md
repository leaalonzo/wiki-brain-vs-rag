## Definition
Falcon is a large language model (LLM) that can be compressed using the Sparse-Quantized Representation (SpQR) technique. This method allows the model to maintain near-lossless accuracy while being reduced to 3-4 bits per parameter, enabling efficient deployment on memory-limited devices.

## Context
Falcon, along with other LLMs like LLaMA, benefits from SpQR by achieving less than 1% accuracy loss in perplexity. This compression technique isolates outlier weights that cause significant quantization errors and stores them in higher precision. The result is a substantial reduction in memory usage, allowing a 33 billion parameter LLM to run on a single 24 GB consumer GPU with no performance degradation and a 15% speedup in inference.

## Related Concepts
- [[Sparse-Quantized Representation]]
- [[Quantization]]
- [[Perplexity]]
- [[LLaMA]]
- [[GPU Inference]]
- [[Memory Compression]]