# Emergent Abilities

## Definition
Emergent abilities refer to capabilities that manifest in large-scale models, such as large language models (LLMs), but are absent in smaller models. These abilities cannot be predicted by simply extrapolating from the performance of smaller models. The phenomenon suggests that as models are scaled up, they may develop new, unforeseen abilities that enhance their performance on various tasks.

## Key Mechanisms
Emergent abilities often appear as a result of scaling laws, where increasing the size of a model leads to predictable improvements in performance. However, these abilities are characterized by a phase transition-like behavior, where performance on certain tasks remains at chance levels until a critical scale is reached, after which there is a significant improvement. This behavior is analogous to phase transitions in physical systems, where qualitative changes occur at specific thresholds.

## Evidence Base
1. **Emergent Abilities of Large Language Models**: This paper by Jason Wei et al. explores the phenomenon of emergent abilities in LLMs, highlighting that these abilities appear unpredictably at specific scales. The study provides examples of emergent abilities in few-shot prompting tasks and raises questions about the nature of emergence in language models.

2. **Are Emergent Abilities of Large Language Models a Mirage?**: This paper by Rylan Schaeffer et al. challenges the notion of emergent abilities, suggesting they are artifacts of the metrics used to evaluate model performance. The authors argue that nonlinear or discontinuous metrics can create the illusion of emergent abilities, whereas linear or continuous metrics reveal smooth and predictable improvements.

## Connections to Other Concepts
- **[[Phase Transition]]**: Emergent abilities in language models are analogous to phase transitions, where qualitative changes occur at certain thresholds.
- **[[Scaling Laws]]**: The predictable improvements in language model performance with scaling contrast with the unpredictable nature of emergent abilities, highlighting the complexity of model scaling.
- **[[Few-shot Prompting]]**: A common setting where emergent abilities have been observed, involving tasks where models generate responses based on a few examples.

## Open Questions
- What underlying mechanisms drive the emergence of new abilities in large-scale models?
- How can we predict or control the emergence of abilities in future model scaling?
- What role do data quality and model parameters play in the emergence of abilities?
- How can we better define and measure emergent abilities to avoid artifacts introduced by metric selection?

## Further Reading
- "Emergent Abilities of Large Language Models" by Jason Wei et al.
- "Are Emergent Abilities of Large Language Models a Mirage?" by Rylan Schaeffer et al.