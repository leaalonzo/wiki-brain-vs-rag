## Definition
Program repair refers to the process of identifying and correcting errors or bugs in software code. It aims to improve the functionality, performance, or compatibility of programs without altering their intended behavior.

## Context
The paper "Automated C/C++ Program Repair for High-Level Synthesis via Large Language Models" introduces a framework that utilizes Large Language Models (LLMs) to automate the repair of C/C++ programs for High-Level Synthesis (HLS). This process traditionally requires significant manual effort to convert C/C++ code into HLS-compatible code. The framework reduces this effort by employing a Retrieval-Augmented Generation (RAG) paradigm, which guides LLMs to minimize hallucinations and enhance prompt quality.

Key innovations include a static bit width optimization program, which achieves considerable reductions in area, power, and clock period. Additionally, a joint LLM-script repair mechanism is used to pre-repair simple errors, reducing the cost associated with LLM usage. The framework demonstrates higher repair pass rates compared to traditional methods and direct LLM applications. Successfully repaired HLS-C programs are further optimized for power, performance, and area (PPA) using LLMs.

## Related Concepts
- [[High-Level Synthesis]]
- [[Large Language Models]]
- [[Retrieval-Augmented Generation]]
- [[Bit Width Optimization]]
- [[Circuit Optimization]]
- [[Power-Performance-Area Optimization]]