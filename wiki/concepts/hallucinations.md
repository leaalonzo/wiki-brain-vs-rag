## Definition
Hallucinations in the context of machine learning, particularly in Large Multimodal Models (LMMs), refer to instances where the model generates outputs that are not grounded in the input data. These outputs often include incorrect or fabricated information that does not align with the visual or textual context provided to the model.

## Context
Hallucinations are a significant challenge in the development of LMMs, which integrate both vision and language modalities. Misalignment between these modalities can lead to outputs that are inconsistent with the input data. The paper "Aligning Large Multimodal Models with Factually Augmented RLHF" addresses this issue by proposing an adaptation of Reinforcement Learning from Human Feedback (RLHF). This approach incorporates factual information into the reward model to improve vision-language alignment and reduce hallucinations. The introduction of a new evaluation benchmark, MMHAL-BENCH, allows for the assessment of models in real-world scenarios with a focus on penalizing hallucinations.

## Related Concepts
- [[Large Multimodal Models]]
- [[Reinforcement Learning from Human Feedback]]
- [[Vision-Language Alignment]]
- [[Factually Augmented RLHF]]
- [[MMHAL-BENCH]]