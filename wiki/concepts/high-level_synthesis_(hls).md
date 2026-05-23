## Definition
High-Level Synthesis (HLS) is a process in electronic design automation that converts a high-level algorithmic description of a digital circuit, typically written in C/C++, into a register-transfer level (RTL) design. This transformation allows designers to work at a higher abstraction level, improving productivity and enabling more complex designs.

## Context
Traditionally, converting C/C++ programs into HLS-compatible code requires significant manual effort due to the limitations of existing HLS tools. The process involves optimizing the code to meet hardware constraints and performance goals, such as area, power, and clock period. Recent advancements have explored the use of Large Language Models (LLMs) to automate this conversion process. 

The paper "Automated C/C++ Program Repair for High-Level Synthesis via Large Language Models" introduces a framework that leverages LLMs to automate program repair. This framework employs a Retrieval-Augmented Generation (RAG) paradigm to guide LLMs, reducing hallucinations and improving prompt quality. It includes a static bit width optimization program, achieving significant reductions in area, power, and clock period. A joint LLM-script repair mechanism is used to pre-repair simple errors, reducing the cost of using LLMs. Successfully repaired HLS-C programs are further optimized for power, performance, and area (PPA) design using LLMs. The framework achieves higher repair pass rates compared to traditional methods and direct LLM applications.

## Related Concepts
- [[Large Language Models (LLMs)]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[Bit Width Optimization]]
- [[Program Repair]]
- [[Circuit Optimization]]
- [[Power-Performance-Area (PPA) Optimization]]