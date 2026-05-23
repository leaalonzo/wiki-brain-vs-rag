## Definition
Best-of-N (BoN) Sampling is a technique used in generating outputs from large language models (LLMs). It involves producing multiple candidate outputs and selecting the best one based on specific criteria. This approach aims to enhance the quality and diversity of generated text by utilizing the range of outputs produced by the model.

## Context
BoN Sampling is particularly important in scenarios where both output quality and diversity are crucial. It is mentioned in the study "Understanding the Effects of RLHF on LLM Generalisation and Diversity" as a method related to evaluating output diversity. The study highlights a trade-off between generalisation and diversity in fine-tuning methods for LLMs, such as Reinforcement Learning from Human Feedback (RLHF) and Supervised Fine-Tuning (SFT). While RLHF improves generalisation to new inputs, it tends to reduce output diversity. Techniques like BoN Sampling can help mitigate this reduction by selecting the most suitable output from a diverse set of candidates.

## Related Concepts
- [[Reinforcement Learning from Human Feedback (RLHF)]]
- [[Out-of-Distribution (OOD) Generalisation]]
- [[Output Diversity]]
- [[Supervised Fine-Tuning (SFT)]]
- [[Reward Modelling]]