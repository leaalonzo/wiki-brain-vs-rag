## Definition
LLM weight compression refers to techniques used to reduce the memory footprint of large language models (LLMs) without significantly impacting their performance. One such technique is the Sparse-Quantized Representation (SpQR), which achieves near-lossless compression by isolating outlier weights for higher precision storage and compressing the remaining weights to 3-4 bits.

## Context
The increasing size of LLMs poses challenges in terms of memory usage and computational efficiency, especially on consumer-grade hardware. SpQR addresses these challenges by enabling powerful LLMs, such as LLaMA and Falcon, to run on devices with limited memory capacity. This is achieved with minimal accuracy loss, typically less than 1% in perplexity, and with a significant reduction in memory usage—up to a 4x compression gain compared to 16-bit baselines. Additionally, SpQR provides a 15% speedup in performance when running a 33B parameter LLM on a 24 GB consumer GPU.

## Related Concepts
- [[Sparse-Quantized Representation]]
- [[Outlier Weights]]
- [[Quantization]]
- [[GPU Inference Algorithm]]
- [[Memory Compression]]
- [[Perplexity]]