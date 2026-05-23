## Definition
Dense passage retrieval is a technique used in information retrieval systems, particularly in open-domain question answering (QA), to efficiently retrieve relevant passages from a large corpus. It involves encoding passages and queries into dense vectors using neural networks, allowing for fast and effective similarity searches.

## Context
Dense passage retrieval has gained prominence in the field of natural language processing (NLP) as it enables more accurate retrieval of information compared to traditional sparse retrieval methods. The approach typically employs dual-encoder architectures, where both the query and passages are encoded independently into dense vectors. This allows for scalable retrieval as vector similarity can be computed efficiently.

Recent advancements, such as [[ERNIE-Search]], have further enhanced dense passage retrieval by integrating techniques from cross-encoder architectures, which consider interactions between query and passage pairs. ERNIE-Search introduces a self on-the-fly distillation method to bridge the gap between cross-encoder and dual-encoder architectures, resulting in improved performance on open-domain QA benchmarks like [[MS MARCO]] Passage Ranking and [[Natural Question]] (NQ). It employs interaction and cascade distillation techniques to facilitate knowledge transfer from more expressive models to dual-encoders.

[[RocketQA]] is an optimized training approach designed to enhance dense passage retrieval. It addresses key challenges in training dual-encoder architectures, such as discrepancies between training and inference, the presence of unlabeled positives, and limited training data. RocketQA introduces techniques like cross-batch negatives, denoised hard negatives, and data augmentation to significantly improve retrieval performance. It demonstrates significant performance improvements over state-of-the-art models on datasets like MS-MARCO and Natural Questions.

A novel approach called [[FetcHR]] improves question-answering systems by enhancing dense passage retrieval using hierarchical representations in transformer networks. FetcHR integrates retrieval into each layer of a transformer network, leveraging different levels of abstraction to improve the quality of retrieved documents. This method outperforms traditional dense passage retrieval by addressing critical features in questions that are often underrepresented in retrieved documents, improving performance on benchmarks such as Natural Question and WebQuestion datasets.

[[xMoCo]], or Cross Momentum Contrastive Learning, is a novel method designed to enhance dense passage retrieval for open-domain question answering. It leverages a dual-encoder model to separately encode questions and passages into vector representations, facilitating efficient retrieval through vector space search. By maintaining a large pool of negative samples and optimizing question-to-passage and passage-to-question matching tasks, xMoCo demonstrates improved performance over traditional methods. It builds on momentum contrastive learning (MoCo) to address challenges in dense passage retrieval by using two sets of fast/slow encoders, allowing for different encoders for questions and passages.

## Related Concepts
- [[Open-Domain Question Answering]]
- [[Dual-Encoder]]
- [[Cross-Encoder]]
- [[ColBERT]]
- [[ERNIE-Search]]
- [[Self On-the-Fly Distillation]]
- [[Interaction Distillation]]
- [[Cascade Distillation]]
- [[RocketQA]]
- [[Cross-Batch Negatives]]
- [[Denoised Hard Negatives]]
- [[Data Augmentation]]
- [[Hierarchical Representations]]
- [[FetcHR]]
- [[Transformer Networks]]
- [[Retrieval Score]]
- [[Contrastive Training]]
- [[xMoCo]]
- [[Momentum Contrastive Learning]]
- [[Question-Passage Matching]]
- [[Negative Sampling]]
- [[Vector Space Search]]