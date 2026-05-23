## Definition
On-device LLM deployment refers to the process of running large language models (LLMs) directly on local devices, such as smartphones, tablets, or edge devices, rather than relying on cloud-based servers. This approach aims to enhance privacy, reduce latency, and improve accessibility by enabling models to operate independently of internet connectivity.

## Context
Deploying LLMs on devices with limited computational resources requires optimization techniques to reduce their memory footprint and accelerate inference. Activation-aware Weight Quantization (AWQ) is a prominent method used for this purpose. AWQ reduces the model size through low-bit weight-only quantization, focusing on minimizing quantization error by identifying and protecting a small fraction of salient weights based on activation distribution. This method does not rely on backpropagation or reconstruction, making it efficient and hardware-friendly.

AWQ has been implemented in frameworks like TinyChat, which provides significant speedups on edge devices, outperforming existing quantization methods on various benchmarks. The adoption of such techniques is crucial for the practical deployment of LLMs on-device, allowing them to generalize across different domains and modalities effectively.

## Related Concepts
- [[Activation-aware Weight Quantization]]
- [[Low-bit Quantization]]
- [[Salient Weights]]
- [[Per-channel Scaling]]
- [[TinyChat]]
- [[Edge Computing]]
- [[Inference Acceleration]]