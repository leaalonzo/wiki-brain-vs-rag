```markdown
## Overview
ERNIE-Search is a novel approach to dense passage retrieval in open-domain question answering (QA) that leverages a unique distillation method to bridge the gap between cross-encoder and dual-encoder architectures. This method, called self on-the-fly distillation, allows for effective knowledge transfer from more expressive models to dual-encoders, enhancing their performance on QA tasks. The approach introduces interaction and cascade distillation techniques, establishing new state-of-the-art results in open-domain QA benchmarks.

## Key Points
- ERNIE-Search introduces a self on-the-fly distillation method for dual-encoders.
- It bridges the structural gap between cross-encoder and dual-encoder models.
- The method uses interaction distillation to mimic late interaction in dual-encoders.
- Cascade distillation involves a stepwise knowledge transfer from cross-encoders to dual-encoders via ColBERT.
- Extensive experiments show that ERNIE-Search outperforms existing baselines.
- The approach achieves state-of-the-art performance on MS MARCO and Natural Question datasets.

## Concepts Introduced
ERNIE-Search, self on-the-fly distillation, interaction distillation, cascade distillation, dual-encoder, cross-encoder, ColBERT, open-domain QA, dense passage retrieval

## Quotes or Data
- "Our proposed solution outperforms strong baselines and establishes a new state-of-the-art on open-domain QA benchmarks."
```
