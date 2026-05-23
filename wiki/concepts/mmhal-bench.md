## Definition
MMHAL-BENCH is an evaluation benchmark specifically designed to assess and penalize hallucinations in Large Multimodal Models (LMMs). It is a tool to measure the effectiveness of alignment strategies in reducing instances where textual outputs are not grounded in the multimodal context.

## Context
MMHAL-BENCH was introduced in the paper "Aligning Large Multimodal Models with Factually Augmented RLHF." The paper addresses the challenge of hallucinations in LMMs, where textual outputs may not align with the visual context. The authors propose Factually Augmented Reinforcement Learning from Human Feedback (Fact-RLHF) to improve vision-language alignment by incorporating factual information into the reward model. This approach adapts RLHF, traditionally used for text-based AI, to the vision-language domain, enhancing model performance and reducing hallucinations. MMHAL-BENCH demonstrated a 60% improvement over other baselines, highlighting its effectiveness in evaluating and improving LMM performance. The proposed method also achieved 94% performance on the LLaVA-Bench dataset. The authors have open-sourced their code, model, and data for public use.

## Related Concepts
- [[Large Multimodal Models]]
- [[Multimodal Misalignment]]
- [[Hallucination]]
- [[Reinforcement Learning from Human Feedback]]
- [[Factually Augmented RLHF]]
- [[Vision-Language Alignment]]
- [[Reward Hacking]]