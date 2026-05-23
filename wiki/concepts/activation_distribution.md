## Definition
Activation distribution refers to the pattern or spread of activations within a neural network layer during the processing of input data. In the context of machine learning, particularly in large language models (LLMs), activation distribution is used to identify salient weights that significantly impact model performance.

## Context
In the field of model optimization, activation distribution plays a crucial role in techniques like Activation-aware Weight Quantization (AWQ). AWQ is designed to optimize LLMs for on-device deployment by reducing memory usage and improving inference speed. This is achieved through low-bit weight-only quantization, where a small percentage of weights are identified as salient based on their activation distribution. Protecting these salient weights minimizes quantization error, enhancing model performance across various domains and modalities without the need for backpropagation or reconstruction.

## Related Concepts
[[Activation-aware Weight Quantization]], [[Low-bit Quantization]], [[Salient Weights]], [[Per-channel Scaling]], [[TinyChat]]