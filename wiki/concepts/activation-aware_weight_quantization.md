## Definition
Activation-aware Weight Quantization (AWQ) is a method designed to optimize large language models (LLMs) by reducing their memory usage and accelerating inference through low-bit weight-only quantization. It identifies and protects a small fraction of salient weights based on activation distribution to minimize quantization error, enhancing the model's performance across various domains and modalities without requiring backpropagation or reconstruction.

## Context
AWQ is particularly relevant for on-device deployment of LLMs, where memory and computational resources are limited. By employing a hardware-friendly approach, AWQ facilitates efficient execution of LLMs on edge devices. It focuses on protecting only 0.1%-1% of weights identified as salient through activation distribution, significantly reducing quantization error. The method utilizes per-channel scaling to further optimize quantization, making it a preferred choice over traditional quantization techniques. AWQ has been implemented in frameworks like TinyChat, achieving notable speedups, such as more than 3× over the Huggingface FP16 implementation on both desktop and mobile GPUs, and outperforming existing methods on various benchmarks. It supports the deployment of large models like Llama-2 on edge devices.

## Related Concepts
- [[Low-bit Weight-only Quantization]]
- [[Salient Weights]]
- [[Activation Distribution]]
- [[Per-channel Scaling]]
- [[On-device LLM Deployment]]
- [[TinyChat]]
- [[Inference Acceleration]]
- [[Quantization Error Reduction]]