## Definition
Multimodal Misalignment refers to the discrepancy in Large Multimodal Models (LMMs) where the generated outputs, particularly textual ones, are not accurately grounded in the multimodal context. This misalignment can lead to hallucinations, where the model produces information that is not supported by the input data.

## Context
Multimodal Misalignment is a significant challenge in the development of LMMs, which integrate multiple types of data, such as text and images, to generate outputs. The issue arises when the model fails to properly align these different modalities, resulting in outputs that may be factually incorrect or misleading. The paper "Aligning Large Multimodal Models with Factually Augmented RLHF" proposes a solution to this problem by using Reinforcement Learning from Human Feedback (RLHF) enhanced with factual data. This approach, known as Factually Augmented RLHF, aims to improve vision-language alignment and reduce hallucinations by incorporating factual information into the reward model.

## Related Concepts
- [[Large Multimodal Models]]
- [[Hallucination]]
- [[Reinforcement Learning from Human Feedback]]
- [[Vision-Language Alignment]]
- [[Reward Hacking]]
- [[Factually Augmented RLHF]]