## Definition
TinyChat is an inference framework designed to optimize large language models (LLMs) for on-device deployment. It implements Activation-aware Weight Quantization (AWQ) to reduce memory usage and accelerate inference, achieving significant speedups on edge devices.

## Context
TinyChat utilizes AWQ, a method focused on low-bit weight-only quantization. This approach identifies and protects a small fraction of salient weights based on activation distribution, minimizing quantization error without the need for backpropagation or reconstruction. By employing a per-channel scaling method, TinyChat enhances the generalization capabilities of LLMs across various domains and modalities. It offers more than a 3× speedup over the Huggingface FP16 implementation on both desktop and mobile GPUs. TinyChat facilitates the deployment of large models like Llama-2 on edge devices, outperforming existing methods on various language modeling and domain-specific benchmarks.

## Related Concepts
- [[Activation-aware Weight Quantization]]
- [[Low-bit weight-only quantization]]
- [[Salient weights]]
- [[Activation distribution]]
- [[Per-channel scaling]]
- [[On-device LLM deployment]]