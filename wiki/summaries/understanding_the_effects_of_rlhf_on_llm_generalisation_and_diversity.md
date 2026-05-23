```markdown
## Overview
This paper explores the effects of Reinforcement Learning from Human Feedback (RLHF) on large language models (LLMs), focusing on two critical properties: out-of-distribution (OOD) generalisation and output diversity. The study finds that while RLHF enhances generalisation to new inputs better than supervised fine-tuning (SFT), it significantly reduces output diversity, highlighting a trade-off between these two desirable attributes in current LLM fine-tuning techniques.

## Key Points
- RLHF improves OOD generalisation compared to SFT, especially with larger distribution shifts between training and testing data.
- RLHF significantly decreases output diversity compared to SFT across various metrics.
- The study underscores a trade-off between generalisation and diversity in current LLM fine-tuning methods.
- The research suggests a need for novel methods to enhance both generalisation and diversity without compromising one for the other.
- The authors provide open-source code to facilitate reproducible research in this area.

## Concepts Introduced
Reinforcement Learning from Human Feedback (RLHF), Supervised Fine-Tuning (SFT), Out-of-Distribution (OOD) Generalisation, Output Diversity, Best-of-N (BoN) Sampling

## Quotes or Data
- "RLHF generalises better than SFT to new inputs, particularly as the distribution shift between train and test becomes larger."
- "RLHF significantly reduces output diversity compared to SFT across a variety of measures, implying a tradeoff in current LLM fine-tuning methods between generalisation and diversity."

[Open Source Code](https://github.com/facebookresearch/rlfh-gen-div)
```
