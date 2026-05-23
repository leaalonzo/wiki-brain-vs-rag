## Definition
Question-passage matching is a process in natural language processing and information retrieval that involves determining the relevance or similarity between a given question and a set of text passages. This task is crucial for systems like open-domain question answering, where the goal is to retrieve the most relevant passage that contains the answer to a user's query.

## Context
The task of question-passage matching is central to open-domain question answering systems, which aim to provide accurate answers by retrieving relevant information from large corpora. Traditional methods often struggle with efficiently matching questions to passages due to the vast amount of data and the need for precise understanding of both the question and the content of the passages.

Recent advancements, such as xMoCo (Cross Momentum Contrastive Learning), have introduced innovative approaches to enhance this process. xMoCo utilizes a dual-encoder model to independently encode questions and passages into vector representations, allowing for efficient retrieval through vector space search. By incorporating a large pool of negative samples and optimizing both question-to-passage and passage-to-question tasks, xMoCo significantly improves the performance of dense passage retrieval. The method employs separate encoders for questions and passages, enhancing the flexibility and effectiveness of the retrieval process.

## Related Concepts
- [[Dense Passage Retrieval]]
- [[Dual-Encoder Model]]
- [[Contrastive Learning]]
- [[Momentum Contrastive Learning]]
- [[Open-Domain Question Answering]]