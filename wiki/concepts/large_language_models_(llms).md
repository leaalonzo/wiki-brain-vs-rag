## Definition
Large Language Models (LLMs) are advanced artificial intelligence systems designed to understand and generate human-like text. They are trained on extensive datasets and can perform various language-related tasks, including translation, summarization, text generation, unit test synthesis, and responding to complex dialogue questions.

## Context
LLMs have applications across diverse fields such as software development, hardware design, and dialogue systems. In software development, LLMs' capabilities in generating unit tests have been enhanced by the UniTSyn dataset, which includes 2.7 million focal-test pairs across Python, Java, Go, C++, and JavaScript, facilitating more effective and scalable testing models. This dataset has demonstrated significant improvements in test generation accuracy and code coverage.

A notable application in hardware design is the automation of C/C++ program repair for High-Level Synthesis (HLS). Traditionally a manual process due to existing HLS tools' limitations, LLMs automate this process, enhancing hardware performance and optimizing circuit design. A novel framework using a Retrieval-Augmented Generation (RAG) paradigm has improved repair accuracy and reduced LLM usage costs, incorporating static bit width optimization and a joint LLM-script repair mechanism.

In dialogue systems, the Cue-CoT method introduces intermediate reasoning steps to identify linguistic cues such as personality, emotion, and psychology, aiming to generate more personalized and engaging responses. Experiments show that Cue-CoT outperforms standard prompting methods in helpfulness and acceptability, with two variants, O-Cue CoT and M-Cue CoT, proposed for advanced reasoning and planning. A benchmark with six datasets in Chinese and English was created to evaluate the method, demonstrating its effectiveness in generating more helpful and acceptable responses.

The Okapi system enhances LLMs through instruction tuning in multiple languages using reinforcement learning from human feedback (RLHF). It addresses the limitations of existing open-source LLMs, which primarily focus on English and a few other languages, by introducing instruction and response-ranked data in 26 diverse languages. Okapi demonstrates the advantages of RLHF over supervised fine-tuning (SFT) for multilingual instruction tuning, providing resources and frameworks for future research.

## Related Concepts
- [[High-Level Synthesis (HLS)]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[Program Repair]]
- [[Circuit Optimization]]
- [[Bit Width Optimization]]
- [[Chain-of-Thought (CoT) Reasoning]]
- [[Multi-Step Question Answering (QA)]]
- [[Unit Test Synthesis]]
- [[UniTSyn]]
- [[Focal-Test Pairs]]
- [[Language Server Protocol (LSP)]]
- [[Cue-CoT]]
- [[Linguistic Cues]]
- [[Dialogue Systems]]
- [[User Status]]
- [[Power-Performance-Area (PPA) Optimization]]
- [[Code Intelligence]]
- [[Program Synthesis]]
- [[Test Case Generation]]
- [[Pass Rate]]
- [[Coverage Rate]]
- [[Instruction Tuning]]
- [[Reinforcement Learning from Human Feedback (RLHF)]]
- [[Supervised Fine-Tuning (SFT)]]
- [[Multilingual Instruction Tuning]]