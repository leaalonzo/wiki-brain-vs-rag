## Definition
Memory compression refers to techniques used to reduce the memory footprint of data or models, enabling efficient storage and processing. In the context of large language models (LLMs), memory compression involves reducing the size of model parameters while maintaining accuracy, allowing deployment on devices with limited memory resources.

## Context
SpQR (Sparse-Quantized Representation) is a prominent memory compression technique specifically designed for LLMs. It compresses model parameters to 3-4 bits per parameter, achieving near-lossless accuracy. SpQR works by identifying and isolating outlier weights, which cause significant quantization errors, and storing them in higher precision. This method results in less than 1% accuracy loss in perplexity for models like LLaMA and Falcon. SpQR enables a 33 billion parameter LLM to run on a single 24 GB consumer GPU without performance degradation, providing a 15% speedup in inference and over 4x memory compression gains compared to 16-bit baselines. It includes efficient algorithms for encoding and decoding weights and a specialized GPU inference algorithm, combining sparse and quantized representations to optimize memory and computational efficiency.

## Related Concepts
- [[Quantization]]
- [[Sparse-Quantized Representation]]
- [[Large Language Models]]
- [[Perplexity]]
- [[GPU Inference]]
- [[Outlier Weights]]