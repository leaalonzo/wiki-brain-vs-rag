## Definition
Out-of-Distribution (OOD) Generalisation refers to the ability of a machine learning model to perform effectively on data that differs significantly from the data it was trained on. This capability is essential for ensuring that models remain robust and applicable in real-world scenarios where input data may not align with the training distribution.

## Context
OOD Generalisation is a significant challenge in machine learning, especially for large language models (LLMs). The paper "Understanding the Effects of RLHF on LLM Generalisation and Diversity" examines how Reinforcement Learning from Human Feedback (RLHF) influences OOD generalisation. The study concludes that RLHF enhances generalisation to new inputs more effectively than Supervised Fine-Tuning (SFT), particularly when there is a substantial distribution shift between training and testing data. However, this improvement in generalisation is often accompanied by a reduction in output diversity, indicating a trade-off in current fine-tuning methods. The research suggests the need for innovative approaches to improve both generalisation and diversity without sacrificing one for the other.

## Related Concepts
- [[Reinforcement Learning from Human Feedback (RLHF)]]
- [[Supervised Fine-Tuning (SFT)]]
- [[Output Diversity]]
- [[Reward Modelling]]
- [[Best-of-N (BoN) Sampling]]