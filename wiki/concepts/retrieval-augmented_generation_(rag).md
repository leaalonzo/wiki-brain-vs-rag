## Definition
Retrieval-Augmented Generation (RAG) is a paradigm that integrates retrieval mechanisms with generative models to enhance the accuracy and reliability of generated outputs. It is particularly effective in reducing hallucinations—incorrect or nonsensical outputs—by providing generative models with relevant external information.

## Context
RAG is utilized to improve the performance of Large Language Models (LLMs) by supplementing them with pertinent information retrieved from external sources. This approach is especially beneficial in tasks such as automating C/C++ program repair for High-Level Synthesis (HLS), where precision is crucial. The RAG paradigm helps mitigate errors and increase the repair pass rate by guiding LLMs with accurate and contextually relevant data. In this context, RAG is used to optimize bit widths, significantly reducing area, power, and clock period, thereby enhancing hardware performance. The framework also introduces a joint LLM-script repair mechanism to pre-repair simple errors, reducing the cost associated with LLM usage.

## Related Concepts
[[High-Level Synthesis (HLS)]], [[Large Language Models (LLMs)]], [[Program Repair]], [[Circuit Optimization]], [[Bit Width Optimization]], [[Power-Performance-Area (PPA) Optimization]]