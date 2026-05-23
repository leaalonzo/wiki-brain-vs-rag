## Definition
LLaMA (Large Language Model Meta AI) is a family of large language models designed to perform various natural language processing tasks. These models are known for their high accuracy and efficiency in generating human-like text.

## Context
LLaMA models have been enhanced using techniques such as SpQR (Sparse-Quantized Representation), which compresses the models to 3-4 bits per parameter while maintaining near-lossless accuracy. This compression allows LLaMA models to be deployed on memory-limited devices like laptops and mobile phones without significant performance degradation. SpQR specifically targets outlier weights that cause high quantization errors, storing them in higher precision to achieve less than 1% accuracy loss in perplexity.

## Related Concepts
- [[Sparse-Quantized Representation]]
- [[Quantization]]
- [[Perplexity]]
- [[GPU Inference]]
- [[Memory Compression]]
- [[Falcon (Language Model)]]