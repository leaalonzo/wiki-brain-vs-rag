```markdown
## Overview
The paper "Hierarchical Representations in Dense Passage Retrieval for Question-Answering" introduces a novel approach to improve question-answering systems by leveraging hierarchical representations within transformer networks. The authors propose a method called FetcHR, which integrates retrieval at each layer of a transformer network, enhancing the retrieval process and ultimately improving the performance of downstream tasks such as question answering.

## Key Points
- Introduces FetcHR, a document fetcher based on hierarchical retrieval within transformer networks.
- Utilizes hidden representations from each layer of a transformer to contribute to the retrieval query.
- Demonstrates that combining retrieval from all layers outperforms retrieval from individual layers.
- FetcHR achieves state-of-the-art performance on the Natural Question and WebQuestion datasets.
- The approach requires training only the retrieval networks, avoiding modifications to the underlying language model.

## Concepts Introduced
Hierarchical Representations, Dense Passage Retrieval, Transformer Networks, FetcHR, Retrieval Score, Contrastive Training

## Quotes or Data
- "Our retriever FetcHR outperforms DPR on critical word features in the question."
- Performance improvements: "up to 1.9 EM score on Natural Question and 2.1 EM score on WebQuestion."
- Example retrieval data: 
  - "When did Harvard become an Ivy League school? FetcHR: Harvard: 300, Ivy League: 109; DPR: Harvard: 341, Ivy League: 66"
  - "Who overthrew the Mongols and established the Ming Dynasty? FetcHR: Mongols: 108, Ming: 112; DPR: Mongols: 108, Ming: 87"
  - "When did the Soviet Union first gain control of parts of Poland and the Baltic Republics? FetcHR: Soviet Union: 139, Poland: 93, Baltic Republics: 7; DPR: Soviet Union: 133, Poland: 214, Baltic Republics: 2"
```
