## Definition
Supervised Fine-Tuning (SFT) is a machine learning technique used to adapt a pre-trained model to a specific task by training it on a labeled dataset. This process involves adjusting the model's parameters to improve its performance on the task at hand, leveraging the knowledge acquired during the initial pre-training phase.

## Context
Supervised Fine-Tuning is a critical step in the development of large language models (LLMs) and other machine learning systems. It allows models to specialize in particular tasks by learning from examples provided in the labeled dataset. While SFT is effective in enhancing a model's performance on specific tasks, it may not always generalize well to out-of-distribution (OOD) inputs. In contrast, techniques like Reinforcement Learning from Human Feedback (RLHF) have been shown to improve OOD generalization but at the cost of reduced output diversity. This highlights a trade-off between generalization and diversity in current fine-tuning methods.

Recent advancements, such as the Okapi system, demonstrate the advantages of RLHF over SFT for multilingual instruction tuning in large language models. Okapi expands accessibility and performance in 26 diverse languages, emphasizing less studied and low-resource languages. This underscores the evolving landscape of fine-tuning methodologies, where RLHF is increasingly favored for its ability to handle multilingual and diverse datasets more effectively than traditional SFT.

## Related Concepts
- [[Reinforcement Learning from Human Feedback (RLHF)]]
- [[Out-of-Distribution (OOD) Generalisation]]
- [[Output Diversity]]
- [[Reward Modelling]]
- [[Best-of-N (BoN) Sampling]]
- [[Instruction Tuning]]
- [[Multilingual LLMs]]