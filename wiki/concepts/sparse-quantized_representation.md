## Definition
Sparse-Quantized Representation (SpQR) is a technique for compressing large language models (LLMs) to 3-4 bits per parameter while maintaining near-lossless accuracy. It achieves this by isolating and storing outlier weights in higher precision, which reduces quantization errors, allowing for efficient operation on memory-limited devices.

## Context
SpQR is particularly beneficial for deploying LLMs on devices with limited memory, such as laptops and mobile phones. The method allows a 33 billion parameter LLM to run on a single 24 GB consumer GPU without performance degradation, offering a 15% speedup in inference and over 4x memory compression gains. SpQR has demonstrated less than 1% accuracy loss in perplexity for models like LLaMA and Falcon. This makes it a viable solution for efficient inference and substantial memory savings. The technique includes efficient algorithms for encoding and decoding weights, with a specialized GPU inference algorithm, combining sparse and quantized representations to optimize memory and computational efficiency.

## Related Concepts
- [[Quantization]]
- [[Large Language Models]]
- [[Perplexity]]
- [[GPU Inference]]
- [[Memory Compression]]
- [[LLaMA]]
- [[Falcon]]
- [[Outlier Weights]]
- [[LLM Weight Compression]]