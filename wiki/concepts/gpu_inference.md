## Definition
GPU inference refers to the process of using a Graphics Processing Unit (GPU) to perform inference tasks in machine learning models. Inference is the phase where a trained model is used to make predictions or decisions based on new data. GPUs are particularly well-suited for inference due to their ability to handle parallel computations efficiently, which is essential for processing large models and datasets quickly.

## Context
In the realm of large language models (LLMs), GPU inference is crucial for deploying models in real-time applications. Techniques like Sparse-Quantized Representation (SpQR) have been developed to optimize GPU inference by compressing model weights to 3-4 bits per parameter while maintaining near-lossless accuracy. This allows for significant memory savings and performance improvements, enabling large models to run on consumer-grade GPUs without degradation. For instance, SpQR can enable a 33 billion parameter model to run on a single 24 GB GPU with a 15% speedup in inference time.

## Related Concepts
- [[Sparse-Quantized Representation]]
- [[Quantization]]
- [[Perplexity]]
- [[Large Language Models]]
- [[Memory Compression]]
- [[Parallel Computing]]