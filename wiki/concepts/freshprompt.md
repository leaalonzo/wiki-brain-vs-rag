## Definition
FreshPrompt is a method designed to enhance the performance of large language models (LLMs) by incorporating up-to-date information from search engines. It improves the accuracy of LLM-generated text, particularly for questions requiring current world knowledge.

## Context
FreshPrompt was introduced in the study "FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation." This method addresses the limitations of LLMs in adapting to rapidly changing information and debunking false premises. FreshPrompt employs a few-shot prompting approach, integrating search engine data to significantly boost LLM performance. It has demonstrated superior results compared to other search-augmented methods and commercial systems like Perplexity.AI.

The method is evaluated using FreshQA, a dynamic question-answering benchmark with 600 questions categorized into never-changing, slow-changing, fast-changing, and false-premise. FreshQA assesses LLMs on correctness and hallucination through RELAXED and STRICT evaluation modes. Human evaluations, involving over 50,000 judgments, indicate that LLMs struggle with fast-changing knowledge and false-premise questions. FreshPrompt significantly enhances LLM factuality, with notable improvements in accuracy for models like GPT-4, yielding improvements of 32.6% and 49.0% accuracy over the vanilla GPT-4 on FreshQA under RELAXED and STRICT, respectively.

## Related Concepts
[[FreshQA]], [[Hallucination]], [[In-context Learning]], [[Search Engine Augmentation]], [[Dynamic QA Benchmark]]