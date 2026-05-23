## Definition
Open-domain question answering (QA) refers to the task of answering questions posed in natural language, where the questions can be about any topic, and the system must retrieve and present accurate answers from a large, unstructured collection of texts.

## Context
Open-domain QA systems are designed to handle a wide range of questions without being limited to a specific domain. These systems often rely on dense passage retrieval techniques to efficiently search through vast amounts of data. Recent advancements in open-domain QA involve the use of pre-trained language models (PLMs) to enhance the retrieval and answering process.

ERNIE-Search is a novel approach that improves dense passage retrieval by integrating cross-encoder and dual-encoder architectures through self on-the-fly distillation. This method allows the transfer of knowledge from more expressive models like ColBERT and cross-encoders to dual-encoders, enhancing their performance on large-scale QA datasets such as MS MARCO Passage Ranking and Natural Question (NQ). ERNIE-Search introduces interaction distillation from ColBERT to dual-encoders and cascade distillation from cross-encoders to dual-encoders, addressing the structural differences between teacher and student models in cross-architecture distillation.

An encoder attribution analysis for Dense Passage Retriever (DPR) has highlighted the individual contributions of the question encoder and passage encoder to the overall performance of DPR. Using a probabilistic framework called encoder marginalization, the study found that the passage encoder plays a more significant role in retrieval accuracy. The analysis suggests that data-efficient training regimes can be developed based on these insights, such as training a passage encoder on SQuAD using 60% less data without losing accuracy.

RocketQA is an optimized training approach designed to enhance dense passage retrieval in open-domain question answering systems. It addresses key challenges in training dual-encoder architectures, such as discrepancies between training and inference, the presence of unlabeled positives, and limited training data. RocketQA introduces three innovative techniques—cross-batch negatives, denoised hard negatives, and data augmentation—to significantly improve retrieval performance over state-of-the-art models. It demonstrates significant performance improvements on MS-MARCO and Natural Questions datasets and enhances end-to-end QA performance using the RocketQA retriever.

xMoCo introduces a novel contrastive learning method tailored for open-domain QA systems. By leveraging cross momentum contrastive learning, xMoCo enhances the dual-encoder model's ability to match questions with relevant passages efficiently. This approach addresses the challenge of maintaining a large pool of negative samples, optimizing both question-to-passage and passage-to-question matching. xMoCo is evaluated on various open-domain QA datasets, demonstrating its effectiveness in improving dense passage retrieval.

## Related Concepts
- [[Dense Passage Retrieval]]
- [[Pre-trained Language Models]]
- [[Cross-encoder]]
- [[Dual-encoder]]
- [[ColBERT]]
- [[Self On-the-fly Distillation]]
- [[Interaction Distillation]]
- [[Cascade Distillation]]
- [[ERNIE-Search]]
- [[Encoder Attribution]]
- [[Encoder Marginalization]]
- [[Data-efficient Training]]
- [[RocketQA]]
- [[Cross-batch Negatives]]
- [[Denoised Hard Negatives]]
- [[Data Augmentation]]
- [[xMoCo]]
- [[Cross Momentum Contrastive Learning]]
- [[Negative Sampling]]
- [[Vector Space Search]]
- [[Momentum Contrastive Learning]]