## Definition
Instruction tuning is a process applied to large language models (LLMs) to enhance their ability to follow human instructions. It involves adjusting the model's parameters to better understand and execute tasks as specified by user inputs. This process can be improved through techniques like reinforcement learning from human feedback (RLHF), which uses human evaluations to guide the tuning process.

## Context
Instruction tuning is crucial for developing LLMs capable of performing tasks across various languages and contexts. Traditionally, most open-source LLMs have been tuned primarily for English and a few other widely spoken languages. However, systems like Okapi have expanded this capability to 26 diverse languages, including less studied and low-resource languages such as Telugu, Ukrainian, Nepali, and Kannada. Okapi is the first system to employ RLHF for instruction-tuned LLMs in multiple languages, demonstrating that RLHF generally outperforms supervised fine-tuning (SFT) in multilingual settings. The framework uses BLOOM and LLaMA as base pre-trained LLMs and provides resources like instruction datasets, response ranking data, benchmark datasets, and fine-tuned LLMs. These resources are available on GitHub, promoting further research and development in multilingual LLMs.

## Related Concepts
- [[Reinforcement Learning from Human Feedback (RLHF)]]
- [[Supervised Fine-Tuning (SFT)]]
- [[Multilingual Large Language Models (LLMs)]]
- [[Open-Source Large Language Models]]
- [[Low-resource Languages]]