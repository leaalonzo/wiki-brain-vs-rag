# Supervised Fine-Tuning (SFT)

## Definition
Supervised Fine-Tuning (SFT) is a machine learning technique used to adapt a pre-trained model to a specific task by further training it on a labeled dataset. This process involves adjusting the model's parameters using supervised learning, where the model learns to map inputs to outputs based on example input-output pairs. SFT is commonly employed in natural language processing (NLP) to enhance the performance of large language models (LLMs) on specific tasks such as sentiment analysis, translation, or question answering.

## Key Mechanisms
- **Pre-trained Model Utilization**: SFT begins with a model that has already been trained on a large corpus of data, capturing general language patterns. This pre-training provides a strong foundation that SFT builds upon.
- **Task-Specific Data**: The model is fine-tuned using a dataset that is specific to the task at hand. This dataset contains labeled examples that guide the model in learning task-specific features.
- **Gradient Descent Optimization**: During SFT, the model's parameters are updated using gradient descent algorithms to minimize the loss function, which measures the difference between the model's predictions and the actual labels.
- **Regularization Techniques**: To prevent overfitting to the fine-tuning dataset, techniques such as dropout, weight decay, or early stopping may be employed.

## Evidence Base
The paper "Understanding the Effects of RLHF on LLM Generalisation and Diversity" provides insights into the performance of SFT compared to other fine-tuning methods. It highlights that while SFT is effective in maintaining output diversity, it may not generalize as well to out-of-distribution (OOD) data as Reinforcement Learning from Human Feedback (RLHF). Specifically, the study finds:
- RLHF improves OOD generalisation more effectively than SFT, particularly with larger distribution shifts between training and testing data.
- SFT maintains higher output diversity compared to RLHF, indicating a trade-off between generalisation and diversity in current fine-tuning methods.

## Connections to Other Concepts
- [[Reinforcement Learning from Human Feedback (RLHF)]]: A fine-tuning method that contrasts with SFT by using human feedback to guide model updates, often leading to better generalisation but reduced diversity.
- [[Out-of-Distribution (OOD) Generalisation]]: The ability of a model to perform well on data that differs from the training set, a key area where RLHF outperforms SFT.
- [[Output Diversity]]: The variety of outputs a model can generate, which SFT tends to preserve better than RLHF.

## Open Questions
- How can SFT be improved to enhance OOD generalisation without sacrificing output diversity?
- What novel methods can be developed to balance the trade-off between generalisation and diversity in fine-tuning LLMs?
- How does the size and quality of the task-specific dataset impact the effectiveness of SFT?

## Further Reading
For more detailed insights into the trade-offs between different fine-tuning methods, refer to the paper "Understanding the Effects of RLHF on LLM Generalisation and Diversity" and explore the open-source code provided by the authors [here](https://github.com/facebookresearch/rlfh-gen-div).