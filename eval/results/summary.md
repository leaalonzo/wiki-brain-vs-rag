# Eval Summary

> Generated: 2026-05-22 18:03  |  Questions evaluated: 10

## Score Breakdown (1–5 per category)

| Category | Wiki (A) | RAG (B) |
|---|---|---|
| Accuracy | 4.6 | 4.4 |
| Completeness | 4.6 | 4.3 |
| Citation | 2.5 | 2.7 |
| Synthesis | 4.3 | 4.1 |
| **Overall** | **4.0** | **3.88** |

## Win / Loss / Tie

| | Count | % |
|---|---|---|
| Wiki wins (A) | 3 | 30% |
| RAG wins (B)  | 5 | 50% |
| Ties          | 2   | 20% |

## Cost & Latency

| System | Avg tokens/query | Avg latency |
|---|---|---|
| Wiki | 11,228 | 20,177 ms |
| RAG  | 7,864  | 12,397 ms |

## Most Interesting Cases


**Q7**: What is speculative decoding and how does it accelerate LLM inference without ch...
- Wiki: 17/20  |  RAG: 4/20  |  Winner: A
- System A provides a detailed and accurate explanation of speculative decoding, while System B fails to address the question.

**Q2**: What are the main failure modes of chain-of-thought prompting identified in rese...
- Wiki: 16/20  |  RAG: 9/20  |  Winner: A
- System A provides a more comprehensive and detailed answer with specific failure modes, while System B lacks detail and specificity.

**Q4**: What is RLHF and what are its main limitations when applied to large language mo...
- Wiki: 12/20  |  RAG: 17/20  |  Winner: B
- System B provides a more comprehensive and accurate explanation of RLHF, including detailed stages and additional limitations, while also synthesizing ideas effectively.


## Per-Question Results

| # | Question | Winner | Wiki score | RAG score |
|---|---|---|---|---|
| 1 | What is chain-of-thought prompting and why does it impr... | B | 16/20 | 17/20 |
| 2 | What are the main failure modes of chain-of-thought pro... | A | 16/20 | 9/20 |
| 3 | How does Plan-and-Solve (PS) prompting differ from stan... | B | 14/20 | 18/20 |
| 4 | What is RLHF and what are its main limitations when app... | B | 12/20 | 17/20 |
| 5 | How does ERNIE-Search bridge the gap between cross-enco... | tie | 18/20 | 18/20 |
| 6 | How does AWQ (Activation-aware Weight Quantization) com... | B | 14/20 | 18/20 |
| 7 | What is speculative decoding and how does it accelerate... | A | 17/20 | 4/20 |
| 8 | What problem does FreshLLMs address and what is the Fre... | tie | 19/20 | 19/20 |
| 9 | What is IRCoT and how does it combine retrieval with ch... | A | 18/20 | 17/20 |
| 10 | How does RocketQA improve dense passage retrieval for o... | B | 16/20 | 18/20 |

