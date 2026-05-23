## Definition
Quantization is a process in machine learning and data compression where numerical values are approximated by a finite set of values. This technique is used to reduce the memory footprint and computational requirements of models, particularly in large language models (LLMs).

## Context
Quantization plays a critical role in deploying large language models on devices with limited memory resources, such as laptops and mobile phones. Techniques like SpQR (Sparse-Quantized Representation) have been developed to compress LLMs to 3-4 bits per parameter while maintaining near-lossless accuracy. SpQR works by identifying and isolating outlier weights that cause significant quantization errors and storing them in higher precision. This approach achieves less than 1% accuracy loss in perplexity for models like LLaMA and Falcon, enabling a 33B parameter LLM to run on a 24 GB consumer GPU with no performance degradation and a 15% speedup. SpQR provides a 4x memory compression gain compared to 16-bit baselines, allowing for efficient inference on consumer-grade hardware, providing substantial memory savings and improved performance.

## Related Concepts
- [[Sparse-Quantized Representation]]
- [[Outlier Weights]]
- [[Perplexity]]
- [[LLaMA]]
- [[Falcon]]
- [[GPU Inference]]
- [[Memory Compression]]