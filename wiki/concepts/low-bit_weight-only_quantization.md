## Definition
Low-bit weight-only quantization is a technique used to optimize large language models (LLMs) for efficient on-device deployment. It involves reducing the precision of model weights to lower bit-widths, thereby decreasing the model's memory footprint and accelerating inference without significantly compromising performance.

## Context
Low-bit weight-only quantization is a crucial component in model compression and acceleration, particularly for deploying LLMs on edge devices with limited computational resources. Activation-aware Weight Quantization (AWQ) is a prominent method in this domain, focusing on identifying and protecting a small percentage of salient weights based on activation distribution to minimize quantization error. This approach does not rely on backpropagation or reconstruction, making it hardware-friendly and efficient for real-world applications. AWQ employs per-channel scaling to further optimize quantization error reduction and has been implemented in frameworks like TinyChat, achieving significant speedups on both desktop and mobile GPUs. AWQ generalizes well across different domains and modalities, enhancing the performance of LLMs without compromising their effectiveness.

## Related Concepts
- [[Activation-aware Weight Quantization]]
- [[Salient Weights]]
- [[Per-channel Scaling]]
- [[On-device LLM Deployment]]
- [[Model Compression]]
- [[Inference Acceleration]]