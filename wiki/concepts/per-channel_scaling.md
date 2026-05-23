## Definition
Per-channel scaling is a technique used in the quantization of neural networks, particularly in optimizing large language models (LLMs) for efficient on-device deployment. It involves adjusting the scale of weights individually for each channel to minimize quantization error and enhance model performance.

## Context
Per-channel scaling is a critical component of Activation-aware Weight Quantization (AWQ), a method aimed at reducing the memory footprint and accelerating the inference of LLMs. AWQ employs per-channel scaling to optimize quantization error by focusing on the distribution of activations rather than weights. This approach allows for the protection of a small fraction of salient weights, significantly reducing quantization error without requiring backpropagation or reconstruction. The technique is especially beneficial for deploying LLMs on edge devices, as demonstrated by the TinyChat inference framework, which implements AWQ to achieve substantial speedups. AWQ and per-channel scaling have shown to generalize well across various domains and modalities, outperforming existing quantization methods.

## Related Concepts
[[Activation-aware Weight Quantization]], [[Quantization]], [[Large Language Models]], [[TinyChat]], [[On-device Deployment]], [[Salient Weights]], [[Activation Distribution]]