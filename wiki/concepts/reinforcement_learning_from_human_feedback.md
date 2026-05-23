## Definition
Reinforcement Learning from Human Feedback (RLHF) is a machine learning paradigm where reinforcement learning agents are trained using feedback provided by humans. This feedback helps in shaping the reward function, guiding the agent towards more desirable behaviors and outputs.

## Context
RLHF is particularly useful in scenarios where traditional reward functions are difficult to define or may lead to unintended behaviors, such as reward hacking. In the context of aligning Large Multimodal Models (LMMs), RLHF can be adapted to address issues like multimodal misalignment, which can cause hallucinations in generated outputs. The paper "Aligning Large Multimodal Models with Factually Augmented RLHF" introduces a novel approach called Factually Augmented Reinforcement Learning from Human Feedback (Fact-RLHF). This method enhances vision-language alignment by incorporating factual information into the reward model, thereby improving performance and reducing hallucinations. The authors developed a new evaluation benchmark, MMHAL-BENCH, to assess model performance with a focus on penalizing hallucinations. The proposed method shows significant improvement, achieving 94% performance on LLaVA-Bench and a 60% improvement on MMHAL-BENCH compared to previous models. The authors have also open-sourced their code, model, and data for public use.

## Related Concepts
- [[Large Multimodal Models]]
- [[Multimodal Misalignment]]
- [[Hallucination]]
- [[Vision-Language Alignment]]
- [[Reward Hacking]]
- [[Factually Augmented RLHF]]
- [[MMHAL-BENCH]]