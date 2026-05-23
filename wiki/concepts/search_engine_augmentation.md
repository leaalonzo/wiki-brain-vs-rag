## Definition
Search engine augmentation refers to the enhancement of large language models (LLMs) by integrating real-time data from search engines. This approach aims to improve the accuracy and relevance of LLM-generated responses, particularly in scenarios requiring up-to-date information.

## Context
Search engine augmentation addresses the limitations of LLMs in adapting to rapidly changing world knowledge. Traditional LLMs often struggle with questions involving fast-changing information or false premises. By incorporating search engine data, models can access the latest information, thereby improving their performance on dynamic question-answering tasks.

The study "FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation" introduces FreshQA, a dynamic QA benchmark, and FreshPrompt, a method that leverages search engine data to significantly enhance LLM accuracy. FreshQA evaluates LLMs on correctness and hallucination through RELAXED and STRICT modes, revealing that concise answers reduce hallucination. FreshPrompt outperforms other methods and commercial systems, highlighting the importance of the number and order of retrieved evidences. FreshQA consists of 600 questions categorized into never-changing, slow-changing, fast-changing, and false-premise types. Human evaluations indicate that LLMs struggle with fast-changing and false-premise questions, regardless of model size.

## Related Concepts
- [[FreshQA]]
- [[FreshPrompt]]
- [[Hallucination]]
- [[In-context learning]]
- [[Dynamic QA benchmark]]
- [[Factuality of LLMs]]