## Definition
Reinforcement Learning from Human Feedback (RLHF) is a machine learning technique used to fine-tune large language models (LLMs). It leverages human feedback to guide the reinforcement learning process, aiming to enhance the model's performance on new inputs while aligning with human preferences.

## Context
RLHF is crucial in developing LLMs as it addresses the challenge of generalisation to out-of-distribution (OOD) inputs. Research indicates that RLHF improves generalisation compared to traditional supervised fine-tuning (SFT), especially with larger distribution shifts between training and testing data. However, it also significantly reduces output diversity, highlighting a trade-off between these two properties. The RLHF process typically involves stages such as supervised fine-tuning, reward modeling, and reinforcement learning. Further research is needed to balance generalisation and diversity effectively.

The Okapi system exemplifies RLHF's application, extending its use to instruction-tuned LLMs across multiple languages. It enhances accessibility and performance in 26 diverse languages, addressing limitations of existing open-source LLMs, which are primarily tuned for English and a few other popular languages. Okapi demonstrates RLHF's advantages over SFT for multilingual instruction tuning, particularly in less studied and low-resource languages like Telugu, Ukrainian, Nepali, and Kannada. The framework uses BLOOM and LLaMA as base pre-trained LLMs and provides resources such as instruction datasets, response ranking data, and fine-tuned LLMs, available on GitHub for further research and development.

## Related Concepts
- [[Out-of-Distribution Generalisation]]
- [[Output Diversity]]
- [[Supervised Fine-Tuning]]
- [[Reward Modelling]]
- [[Best-of-N Sampling]]
- [[Instruction Tuning]]
- [[Multilingual LLMs]]
- [[Open-Source LLMs]]
- [[Low-resource Languages]]