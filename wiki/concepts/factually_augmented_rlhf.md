## Definition
Factually Augmented RLHF, or Factually Augmented Reinforcement Learning from Human Feedback (Fact-RLHF), is an algorithm designed to improve the alignment of vision-language models by integrating factual data into the reward model. This approach aims to reduce hallucinations in Large Multimodal Models (LMMs) by enhancing the accuracy of textual outputs within a multimodal context.

## Context
Factually Augmented RLHF tackles the issue of multimodal misalignment in LMMs, which can lead to hallucinations where generated text is not accurately grounded in the visual context. By incorporating factual information, such as image captions, into the reward model, this algorithm enhances the performance of Reinforcement Learning from Human Feedback (RLHF) in aligning vision and language. The approach adapts RLHF, traditionally used for text-based AI, to the vision-language domain. It has demonstrated significant improvements, achieving a 94% performance level on the LLaVA-Bench dataset and a 60% improvement on the MMHAL-BENCH benchmark compared to other methods. The authors have open-sourced their code, model, and data to facilitate further research and development.

## Related Concepts
- [[Large Multimodal Models]]
- [[Multimodal Misalignment]]
- [[Hallucination]]
- [[Reinforcement Learning from Human Feedback]]
- [[Vision-Language Alignment]]
- [[MMHAL-BENCH]]