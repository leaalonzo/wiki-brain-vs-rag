---
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
authors: ["Jason Wei", "Xuezhi Wang", "Dale Schuurmans", "Maarten Bosma", "Brian Ichter", "Fei Xia", "Ed H. Chi", "Quoc Le", "Denny Zhou"]
year: 2022
abstract: "We explore how generating a chain of thought — a series of intermediate reasoning steps — significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier."
source_url: "https://arxiv.org/abs/2201.11903"
pdf_url: "https://arxiv.org/pdf/2201.11903"
doi: "10.48550/arXiv.2201.11903"
query_tag: "chain_of_thought"
license: "CC BY 4.0"
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

Wei et al., 2022 · arXiv:2201.11903

## Abstract

We explore how generating a chain of thought — a series of intermediate reasoning steps — significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.

## Key contributions

- Demonstrates that few-shot prompting with step-by-step reasoning examples (chain of thought) dramatically improves multi-step reasoning.
- Shows this capability is emergent: CoT prompting only helps above a certain model scale (~100B parameters).
- Chain of thought is elicited, not trained — no fine-tuning required, just examples in the prompt.

## Core concepts

- **Chain of thought (CoT)**: a sequence of natural language intermediate reasoning steps leading to a final answer.
- **Few-shot CoT prompting**: include `(input, chain-of-thought, output)` triples as demonstrations in the prompt.
- **Emergent reasoning**: ability that is absent in smaller models but appears at larger scale.
- **Task coverage**: arithmetic (GSM8K, SVAMP), commonsense reasoning, symbolic manipulation.

## Connections

- Extended by zero-shot CoT ("Let's think step by step" — Kojima et al.).
- Plan-and-Solve (PS) prompting addresses missing-step errors in CoT.
- IRCoT interleaves retrieval between CoT steps for multi-hop QA.
- Faithfulness of CoT explanations is questioned (Turpin et al., 2023 — CoT explanations can misrepresent the model's actual reasoning process).
