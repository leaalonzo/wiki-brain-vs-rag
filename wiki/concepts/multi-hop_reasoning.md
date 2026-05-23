## Definition
Multi-hop reasoning is a process in artificial intelligence and natural language processing that involves making inferences through multiple steps or "hops" to reach a conclusion. This approach mimics human-like reasoning by connecting various pieces of information to derive implicit meanings or insights.

## Context
Multi-hop reasoning is crucial in tasks that require understanding beyond surface-level information, such as implicit sentiment analysis (ISA). The paper "Reasoning Implicit Sentiment with Chain-of-Thought Prompting" introduces a framework called Three-hop Reasoning (THOR), which utilizes chain-of-thought (CoT) prompting to perform multi-hop reasoning. This method enables the detection of implicit sentiment by inferring latent opinions and aspects, significantly improving performance in both supervised and zero-shot settings. THOR employs a three-step prompting method to identify implicit aspects, opinions, and sentiment polarity, and uses a self-consistency mechanism to ensure the correctness of each reasoning step. The framework demonstrates substantial improvements in state-of-the-art results, particularly with models like THOR+Flan-T5 and THOR+GPT3, achieving over a 6% F1 score increase in supervised setups and over a 50% F1 score increase in zero-shot settings.

## Related Concepts
- [[Implicit Sentiment Analysis]]
- [[Chain-of-Thought Prompting]]
- [[Common-Sense Reasoning]]
- [[Self-Consistency Mechanism]]