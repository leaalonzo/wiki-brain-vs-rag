## Definition
Reward Modelling is a process in machine learning where a model is trained to predict a reward signal based on human feedback. This reward signal is then used to guide the training of another model, often through reinforcement learning, to achieve desired behaviors or outputs.

## Context
Reward Modelling is a critical component in Reinforcement Learning from Human Feedback (RLHF), a technique used to fine-tune large language models (LLMs). In RLHF, human feedback is used to create a reward model that evaluates the quality of model outputs. This reward model then guides the reinforcement learning process to improve model performance, particularly in terms of generalisation to out-of-distribution (OOD) inputs. However, studies have shown that while RLHF can enhance generalisation, it may also reduce output diversity compared to methods like supervised fine-tuning (SFT). This tradeoff highlights the need for further research to balance these competing objectives.

## Related Concepts
- [[Reinforcement Learning from Human Feedback (RLHF)]]
- [[Out-of-Distribution (OOD) Generalisation]]
- [[Output Diversity]]
- [[Supervised Fine-Tuning (SFT)]]
- [[Best-of-N (BoN) Sampling]]