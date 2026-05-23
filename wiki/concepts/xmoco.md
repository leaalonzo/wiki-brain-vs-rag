## Definition
xMoCo, or Cross Momentum Contrastive Learning, is a method designed to enhance dense passage retrieval in open-domain question answering systems. It employs a dual-encoder model to independently encode questions and passages into vector representations, facilitating efficient retrieval through vector space search. xMoCo specifically optimizes both question-to-passage and passage-to-question tasks by managing a large pool of negative samples.

## Context
xMoCo builds on the dense passage retrieval paradigm by addressing the limitations of traditional momentum contrastive learning (MoCo). It introduces a novel contrastive learning method for question-passage matching, using separate encoders for questions and passages. The method employs two sets of fast/slow encoders, allowing for efficient management of negative samples, which is crucial for the performance of dense passage retrieval models. Evaluations on various open-domain QA datasets have demonstrated significant improvements in performance over existing methods.

## Related Concepts
- [[Dense Passage Retrieval]]
- [[Dual-Encoder Model]]
- [[Contrastive Learning]]
- [[Momentum Contrastive Learning]]
- [[Question-Passage Matching]]
- [[Negative Samples]]
- [[Vector Space Search]]