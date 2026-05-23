## Definition
A GPU inference algorithm is a computational method designed to execute machine learning models on Graphics Processing Units (GPUs). These algorithms leverage the parallel processing capabilities of GPUs to perform inference tasks more efficiently than traditional CPUs, particularly for large-scale models such as those used in deep learning.

## Context
In the context of machine learning, inference refers to the process of using a trained model to make predictions on new data. As models, especially large language models (LLMs), grow in size and complexity, the demand for efficient inference methods increases. GPU inference algorithms are crucial for handling the computational load of these models, enabling faster and more efficient processing.

The SpQR (Sparse-Quantized Representation) technique exemplifies a specialized GPU inference algorithm. It facilitates near-lossless compression of LLMs by isolating outlier weights for higher precision storage and compressing the remaining weights to 3-4 bits. This approach allows large models, such as a 33 billion parameter LLM, to run on consumer-grade GPUs with significant memory and speed improvements.

## Related Concepts
- [[Sparse-Quantized Representation]]
- [[LLM weight compression]]
- [[Quantization]]
- [[Memory compression]]
- [[Perplexity]]
- [[Outlier weights]]