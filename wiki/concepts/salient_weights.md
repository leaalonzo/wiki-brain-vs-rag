## Definition
Salient weights refer to a small fraction of weights in a neural network that are critical for maintaining the model's performance during quantization. In the context of Activation-aware Weight Quantization (AWQ), salient weights are identified based on activation distribution rather than weight distribution. Protecting these weights helps minimize quantization error, allowing for effective low-bit weight-only quantization.

## Context
In large language models (LLMs), quantization is a technique used to reduce the model's memory footprint and accelerate inference, particularly for on-device deployment. Activation-aware Weight Quantization (AWQ) is a method that focuses on low-bit weight-only quantization, where identifying and protecting salient weights is crucial. By safeguarding only 0.1%-1% of these weights, AWQ achieves significant reductions in quantization error without the need for backpropagation or reconstruction. This enhances the model's generalization capabilities across various domains and modalities. AWQ employs a per-channel scaling method to optimize quantization error reduction, and it is implemented in frameworks like TinyChat, which facilitates the deployment of large models such as Llama-2 on edge devices.

## Related Concepts
- [[Activation-aware Weight Quantization]]
- [[Low-bit Weight-only Quantization]]
- [[Per-channel Scaling]]
- [[TinyChat]]
- [[On-device LLM Deployment]]