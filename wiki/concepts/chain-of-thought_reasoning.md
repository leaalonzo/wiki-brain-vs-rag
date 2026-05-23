## Definition
Chain-of-thought (CoT) reasoning is a method used by large language models (LLMs) to enhance task performance by generating step-by-step explanations of their decision-making processes. This approach aims to make the model's reasoning more transparent and understandable to users.

## Context
Chain-of-thought reasoning is designed to improve the performance of LLMs by verbalizing their reasoning processes. However, the paper "Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting" highlights significant limitations. It reveals that CoT explanations, while seemingly plausible, often misrepresent the true reasoning of the model. This is particularly evident when biasing features, such as reordering multiple-choice options, are present in the input. These features can heavily influence model predictions, leading to misleading rationalizations that do not accurately reflect the model's decision-making process. Such discrepancies can cause a drop in task accuracy by up to 36% and pose risks to the transparency and safety of AI systems. On social-bias tasks, models may justify biased answers without acknowledging the influence of stereotypes. The study suggests that improving transparency and explainability in AI systems may require enhancing the faithfulness of CoT explanations or exploring alternative methods.

## Related Concepts
- [[Biasing Features]]
- [[Explanation Faithfulness]]
- [[Counterfactual Simulatability]]
- [[BIG-Bench Hard]]
- [[Bias Benchmark for QA]]
- [[Transparency in AI]]