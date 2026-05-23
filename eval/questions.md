# Benchmark Q&A Pairs

10 questions drawn from the papers in this knowledge base.
Used to evaluate RAG vs Wiki-compiler answering quality.

---

1. **Q**: What is chain-of-thought prompting and why does it improve reasoning in large language models?
   **A**: Chain-of-thought (CoT) prompting elicits step-by-step intermediate reasoning from LLMs before producing a final answer. It improves performance on multi-step tasks because breaking a problem into reasoning steps reduces errors at each step and makes the reasoning process transparent. It can be applied few-shot (with worked examples) or zero-shot (e.g., "Let's think step by step").
   **Source**: towards_understanding_chain-of-thought_prompting_an_empirical_study_of_what_matt.md

2. **Q**: What are the main failure modes of chain-of-thought prompting identified in research?
   **A**: Key failure modes include calculation errors (arithmetic mistakes in intermediate steps), missing-step errors (skipping a necessary reasoning step), and semantic misunderstanding errors (misinterpreting the problem). CoT also fails on tasks that don't benefit from decomposition, and can produce plausible-sounding but unfaithful reasoning chains that don't actually reflect the model's computation.
   **Source**: language_models_dont_always_say_what_they_think_unfaithful_explanations_in_chain.md

3. **Q**: How does Plan-and-Solve (PS) prompting differ from standard zero-shot chain-of-thought prompting?
   **A**: Plan-and-Solve (PS) prompting adds an explicit planning step before the reasoning chain: the model first devises a plan to solve the problem, then executes the steps. Unlike "Let's think step by step," PS prompting reduces missing-step errors by forcing the model to outline the full solution strategy before computing. PS+ extends this by also instructing the model to extract relevant variables and compute carefully.
   **Source**: plan-and-solve_prompting_improving_zero-shot_chain-of-thought_reasoning_by_large.md

4. **Q**: What is RLHF and what are its main limitations when applied to large language models?
   **A**: Reinforcement Learning from Human Feedback (RLHF) fine-tunes LLMs using a reward model trained on human preference comparisons, then optimizes the policy with PPO. Key limitations include reward hacking (the model exploits the reward model's weaknesses), reduced output diversity, potential degradation of out-of-distribution generalization, and the high cost of collecting human preference data at scale.
   **Source**: understanding_the_effects_of_rlhf_on_llm_generalisation_and_diversity.md

5. **Q**: How does ERNIE-Search bridge the gap between cross-encoders and dual-encoders for dense retrieval?
   **A**: ERNIE-Search uses self on-the-fly distillation: during training, the dual-encoder student learns from a cross-encoder teacher without requiring the teacher to be pre-trained separately. The cross-encoder provides interaction-based scores as soft labels that guide the dual-encoder to approximate full query-document interaction. This avoids the expensive cascade pipeline while retaining much of the cross-encoder's accuracy.
   **Source**: ernie-search_bridging_cross-encoder_with_dual-encoder_via_self_on-the-fly_distil.md

6. **Q**: How does AWQ (Activation-aware Weight Quantization) compress LLMs with minimal accuracy loss?
   **A**: AWQ identifies a small fraction of weights (salient weights) that are critical based on activation magnitudes rather than weight magnitudes alone. These salient weights are protected from aggressive quantization while the remaining weights are quantized to low bit-widths (e.g., 4-bit). This activation-aware selection allows near-lossless 4-bit quantization without requiring gradient-based training or large calibration datasets.
   **Source**: awq_activation-aware_weight_quantization_for_llm_compression_and_acceleration.md

7. **Q**: What is speculative decoding and how does it accelerate LLM inference without changing outputs?
   **A**: Speculative decoding uses a small draft model to generate several candidate tokens quickly, then verifies them in parallel with the large target model. Because the target model can score a batch of tokens in one forward pass (similar cost to scoring one), accepted tokens are generated faster. Rejected tokens fall back to the target model's distribution, so the output distribution is mathematically identical to autoregressive decoding from the large model alone.
   **Source**: fast_inference_from_transformers_via_speculative_decoding.md

8. **Q**: What problem does FreshLLMs address and what is the FreshPrompt approach?
   **A**: FreshLLMs addresses the knowledge staleness problem: LLMs trained on static snapshots give outdated answers to time-sensitive questions. FreshPrompt retrieves up-to-date search engine results for a query and injects them into the prompt context before the LLM answers. This allows a frozen LLM to answer questions about recent events without retraining, at the cost of retrieval latency.
   **Source**: freshllms_refreshing_large_language_models_with_search_engine_augmentation.md

9. **Q**: What is IRCoT and how does it combine retrieval with chain-of-thought reasoning?
   **A**: Interleaved Retrieval with Chain-of-Thought (IRCoT) interleaves retrieval steps with CoT reasoning steps: after each reasoning sentence, the system retrieves new supporting passages, which in turn guide the next reasoning step. This iterative loop outperforms retrieving all passages upfront, because later reasoning steps can identify information gaps not anticipated by the original query.
   **Source**: interleaving_retrieval_with_chain-of-thought_reasoning_for_knowledge-intensive_m.md

10. **Q**: How does RocketQA improve dense passage retrieval for open-domain question answering?
    **A**: RocketQA introduces three training strategies: cross-batch negatives (using all passages in a training batch as negatives without extra memory), denoised hard negative sampling (using a cross-encoder to filter false negatives from retrieved hard negatives), and data augmentation with unlabeled passages scored by the cross-encoder. Together these improve the dual-encoder's ability to distinguish relevant from irrelevant passages.
    **Source**: rocketqa_an_optimized_training_approach_to_dense_passage_retrieval_for_open-doma.md
