## Definition
Three-hop Reasoning (THOR) is a framework designed to enhance implicit sentiment analysis (ISA) by employing a structured, three-step reasoning process. It leverages chain-of-thought (CoT) prompting to mimic human-like reasoning, enabling the inference of sentiments that are not explicitly expressed in text.

## Context
Implicit Sentiment Analysis requires the ability to deduce sentiment from text that lacks direct opinion expressions, necessitating common-sense and multi-hop reasoning. The THOR framework addresses this challenge by breaking down the reasoning process into three distinct steps: identifying the implicit aspect, determining the opinion, and establishing the sentiment polarity. This method has demonstrated significant improvements in both supervised and zero-shot settings. Notably, THOR+Flan-T5 (11B) has improved the state-of-the-art (SoTA) by over 6% F1 score in supervised scenarios, while THOR+GPT3 (175B) has achieved over a 50% F1 score increase in zero-shot settings. The framework also incorporates a self-consistency mechanism to ensure the accuracy of each reasoning step. Additionally, the THOR framework can be broadly applied to other natural language processing (NLP) problems with minimal effort.

## Related Concepts
- [[Implicit Sentiment Analysis]]
- [[Chain-of-Thought Prompting]]
- [[Common-sense Reasoning]]
- [[Multi-hop Reasoning]]
- [[Self-consistency Mechanism]]