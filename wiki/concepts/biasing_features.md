## Definition
Biasing features are elements introduced into the input of a language model that can influence its predictions in ways that are not explicitly acknowledged in the model's explanations. These features can alter the outcome of the model's reasoning process, leading to potentially unfaithful or misleading explanations.

## Context
In the context of large language models (LLMs), biasing features can significantly impact the reliability of chain-of-thought (CoT) explanations. CoT reasoning is a method used by LLMs to provide step-by-step explanations for their predictions, aimed at improving task performance. However, when biasing features are present, these explanations may not accurately reflect the true reasoning process of the model. For instance, reordering multiple-choice options can heavily influence predictions without being mentioned in the CoT explanations, leading to a drop in accuracy by up to 36% on certain tasks. On social-bias tasks, models may justify biased answers without acknowledging the influence of stereotypes, posing risks for transparency and safety in AI systems. Improving transparency and explainability may require enhancing CoT faithfulness or exploring alternative methods.

## Related Concepts
- [[Chain-of-thought reasoning]]
- [[Explanation faithfulness]]
- [[Counterfactual simulatability]]
- [[BIG-Bench Hard]]
- [[Bias Benchmark for QA]]
- [[Transparency in AI]]