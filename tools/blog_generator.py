"""
Phase 5 — Blog Generator.

Reads eval/results/summary.md, wiki/_lint_report.md, and wiki/_compilation_log.json,
then generates 4 Substack post drafts and 4 LinkedIn posts to content/drafts/.

Usage:
    python -m tools.blog_generator                     # all Substack posts
    python -m tools.blog_generator --post 4            # one Substack post
    python -m tools.blog_generator --linkedin          # all LinkedIn posts
    python -m tools.blog_generator --linkedin --post 2 # one LinkedIn post
"""

import json
import os
import glob
from pathlib import Path

import click
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

EVAL_SUMMARY   = Path("eval/results/summary.md")
LINT_REPORT    = Path("wiki/_lint_report.md")
COMPILE_LOG    = Path("wiki/_compilation_log.json")
RESULTS_DIR    = Path("eval/results")
DRAFTS_DIR     = Path("content/drafts")
BLOG_MODEL     = os.getenv("QA_MODEL", "gpt-4o")

TONE_GUIDE = """
Tone and style rules (follow strictly):
- First-person, direct, technically honest
- Accessible to a technical reader who isn't necessarily an ML researcher
- No hype, no claims the system is "revolutionary" or "state-of-the-art"
- Acknowledge failures and limitations plainly
- No company-specific references, no financial or market claims
- Use concrete numbers from the data provided
- Markdown formatting suitable for Substack
- Length: 800–1200 words per post
"""

LINKEDIN_TONE_GUIDE = """
LinkedIn post rules (follow strictly):
- First-person, conversational, technically credible
- ≤300 words — every word earns its place
- No hype, no buzzwords like "game-changing" or "revolutionary"
- No company-specific references, no financial or market claims
- Hook on line 1 — make it a provocation or a concrete fact, not a question
- Short paragraphs: 1–3 lines, plenty of white space
- End with 1 clear takeaway or call to action, not a question
- No hashtag spam — 2–3 relevant tags maximum, at the end
"""


# ── Data loaders ──────────────────────────────────────────────────────────────

def load_eval_data() -> dict:
    results = [
        json.load(open(f))
        for f in sorted(glob.glob(str(RESULTS_DIR / "q*.json")))
    ]
    cats = ["accuracy", "completeness", "citation", "synthesis"]

    def total(r, sys):
        return sum(r["judge"].get(sys, {}).get(c, 0) for c in cats)

    judged = [r for r in results if "judge" in r]
    divergent = sorted(
        judged,
        key=lambda r: abs(total(r, "systemA") - total(r, "systemB")),
        reverse=True,
    )[:3]

    wiki_tokens = sum(r.get("wiki", {}).get("token_count", 0) for r in results)
    rag_tokens  = sum(r.get("rag",  {}).get("token_count", 0) for r in results)
    wiki_lat    = [r["wiki"]["latency_ms"] for r in results if "wiki" in r]
    rag_lat     = [r["rag"]["latency_ms"]  for r in results if "rag"  in r]

    # gpt-4o pricing estimate: 80% input @ $2.50/1M, 20% output @ $10/1M
    def cost(tokens): return (tokens * 0.8 * 2.50 + tokens * 0.2 * 10.0) / 1_000_000

    qa_pairs = []
    for r in divergent:
        qa_pairs.append({
            "id": r["id"],
            "question": r["question"],
            "wiki_answer": r["wiki"]["answer"][:800],
            "rag_answer":  r["rag"]["answer"][:800],
            "wiki_score":  total(r, "systemA"),
            "rag_score":   total(r, "systemB"),
            "winner":      r["judge"].get("winner", "?"),
            "reasoning":   r["judge"].get("reasoning", ""),
        })

    return {
        "n_questions": len(results),
        "n_judged": len(judged),
        "wiki_wins": sum(1 for r in judged if r["judge"].get("winner") == "A"),
        "rag_wins":  sum(1 for r in judged if r["judge"].get("winner") == "B"),
        "ties":      sum(1 for r in judged if r["judge"].get("winner") == "tie"),
        "wiki_overall": round(sum(total(r,"systemA") for r in judged) / max(len(judged),1) / 20 * 5, 2),
        "rag_overall":  round(sum(total(r,"systemB") for r in judged) / max(len(judged),1) / 20 * 5, 2),
        "summary_md": EVAL_SUMMARY.read_text() if EVAL_SUMMARY.exists() else "",
        "wiki_tokens_total": wiki_tokens,
        "rag_tokens_total":  rag_tokens,
        "wiki_cost": cost(wiki_tokens),
        "rag_cost":  cost(rag_tokens),
        "wiki_avg_latency_ms": int(sum(wiki_lat) / max(len(wiki_lat), 1)),
        "rag_avg_latency_ms":  int(sum(rag_lat)  / max(len(rag_lat),  1)),
        "qa_pairs": qa_pairs,
    }


def load_compile_data() -> dict:
    if not COMPILE_LOG.exists():
        return {}
    log = json.load(open(COMPILE_LOG))
    phases: dict[str, int] = {}
    for e in log["entries"]:
        p = e.get("phase", "unknown")
        phases[p] = phases.get(p, 0) + e["total_tokens"]
    total = sum(phases.values())
    def cost(t): return (t * 0.8 * 2.50 + t * 0.2 * 10.0) / 1_000_000
    return {
        "entries": len(log["entries"]),
        "phases": phases,
        "total_tokens": total,
        "total_cost": cost(total),
        "summarize_tokens": phases.get("summarize", 0),
        "concept_tokens":   phases.get("concept", 0),
    }


def load_lint_data() -> str:
    return LINT_REPORT.read_text() if LINT_REPORT.exists() else ""


# ── Post generators ───────────────────────────────────────────────────────────

def generate_post(client: OpenAI, post_num: int, system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=BLOG_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


def build_post_1(client: OpenAI) -> str:
    system = f"You are writing a Substack post about building a personal AI knowledge base.\n{TONE_GUIDE}"
    user = """Write Post 1 of a 4-part series titled "Building a Personal Research Wiki with LLMs".

Post 1 topic: **The Ingestion Problem — turning PDFs into a queryable knowledge base**

Cover:
- Why reading papers accumulates debt (you can't recall what you've read)
- The decision to build something instead of using existing tools, and why
- How the fetch pipeline works: Semantic Scholar API → PDF download → pymupdf4llm → Markdown
- The messy reality: rate limits, corrupt PDFs, missing abstracts, 621 chunks from 36 papers
- The YAML frontmatter approach for tracking metadata per document
- What "semantic chunking" means in practice (paragraph → sentence → overlap)

Data to include:
- 36 papers ingested
- 621 chunks indexed in ChromaDB
- Chunking parameters: 800 tokens max, 50-token overlap

End with a preview of what comes next (compiling the wiki).
"""
    return generate_post(client, 1, system, user)


def build_post_2(client: OpenAI) -> str:
    compile_data = load_compile_data()
    lint_data = load_lint_data()
    system = f"You are writing a Substack post about building a personal AI knowledge base.\n{TONE_GUIDE}"
    user = f"""Write Post 2 of a 4-part series titled "Building a Personal Research Wiki with LLMs".

Post 2 topic: **The Wiki Compiler — turning summaries into a living knowledge graph**

Cover:
- Phase 2a: summarizing each paper with a structured prompt (Summary, Key Claims, Concepts, Connections, Questions Raised)
- Phase 2b: writing concept articles that synthesize across papers — one article per concept, with evidence from all relevant papers
- Phase 2c: the health linter — 5 automated checks (consistency, coverage, orphans, gap finder, imputation)
- Phase 2d: the master index and backlink map
- The Obsidian integration — browsing the wiki as a graph

Compilation stats (use these):
- Summarization: {compile_data.get('summarize_tokens', 0):,} tokens
- Concept writing: {compile_data.get('concept_tokens', 0):,} tokens
- Total compilation cost: ${compile_data.get('total_cost', 0):.2f}
- 259 concept articles generated from 36 papers

Lint report findings (include honestly):
{lint_data[:1200]}

Discuss: what surprised you about the concept graph, what the linter caught, what it missed.
"""
    return generate_post(client, 2, system, user)


def build_post_3(client: OpenAI) -> str:
    system = f"You are writing a Substack post about building a personal AI knowledge base.\n{TONE_GUIDE}"
    user = """Write Post 3 of a 4-part series titled "Building a Personal Research Wiki with LLMs".

Post 3 topic: **Two Ways to Query — RAG vs Wiki-grounded Q&A**

Cover:
- The two querying approaches and their architectural difference:
  - RAG: embed query → cosine similarity → top-k chunks → gpt-4o
  - Wiki: LLM reads index → selects relevant concept articles → gpt-4o
- Why you built both instead of just one
- The bug that ruined the first wiki eval run (8,000 char index truncation cutting off half the articles)
- How the retrieval.py works: cosine similarity scores, what "0.57" actually means
- ChromaDB as a local vector store — what you gain and what you give up vs a hosted service
- A worked example of a query that RAG handled well and one where it failed completely

Be honest: RAG is simpler to build and often faster. The wiki approach adds latency and cost for synthesis benefits that aren't always realized.
"""
    return generate_post(client, 3, system, user)


def build_post_4(client: OpenAI) -> str:
    eval_data = load_eval_data()

    qa_pairs_text = ""
    for pair in eval_data["qa_pairs"]:
        qa_pairs_text += f"""
### Q{pair['id']}: {pair['question']}

**Wiki (score: {pair['wiki_score']}/20):**
{pair['wiki_answer'][:500]}...

**RAG (score: {pair['rag_score']}/20):**
{pair['rag_answer'][:500]}...

**Judge verdict:** {pair['winner'].upper()} — {pair['reasoning']}

---
"""

    system = f"You are writing a Substack post about building a personal AI knowledge base.\n{TONE_GUIDE}"
    user = f"""Write Post 4 of a 4-part series titled "Building a Personal Research Wiki with LLMs".

Post 4 topic: **The Results — Wiki vs RAG, judged by GPT-4o**

This is the results post. Be direct and data-driven. Include the actual numbers.

Evaluation setup:
- 10 questions drawn from the ingested papers
- Both systems answered every question
- GPT-4o judged each answer pair on: Accuracy, Completeness, Citation quality, Synthesis (each 1-5)
- Winner picked per question

Score table to include verbatim:
{eval_data['summary_md'][eval_data['summary_md'].find('## Score'):eval_data['summary_md'].find('## Win')]}

Win/loss:
- Wiki wins: {eval_data['wiki_wins']}/10
- RAG wins:  {eval_data['rag_wins']}/10
- Ties:      {eval_data['ties']}/10

Cost & latency:
- Wiki: {eval_data['wiki_tokens_total']:,} tokens total across 10 queries ≈ ${eval_data['wiki_cost']:.4f} | avg {eval_data['wiki_avg_latency_ms']:,}ms/query
- RAG:  {eval_data['rag_tokens_total']:,} tokens total across 10 queries ≈ ${eval_data['rag_cost']:.4f} | avg {eval_data['rag_avg_latency_ms']:,}ms/query

3 most divergent Q&A pairs (include these side-by-side):
{qa_pairs_text}

Discuss:
1. Why wiki won on synthesis but lost on citation
2. Why RAG catastrophically failed Q7 (speculative decoding — the paper wasn't indexed until mid-run)
3. The index truncation bug that gave wiki a 4/20 on Q8 before the fix
4. What this means for actually using these systems day-to-day
5. Your honest take: would you use this, and in what situation would you reach for wiki vs RAG?

End with what you'd do differently if starting over.
"""
    return generate_post(client, 4, system, user)


# ── LinkedIn post generators ──────────────────────────────────────────────────

def build_linkedin_1(client: OpenAI) -> str:
    system = f"You are writing a LinkedIn post about building a personal AI knowledge base.\n{LINKEDIN_TONE_GUIDE}"
    user = """Write LinkedIn Post 1 of a 4-part series.

Topic: Hook + Karpathy quote + thesis — why build a brain wiki instead of just a RAG pipeline?

The Karpathy quote to work in naturally (paraphrase or quote directly):
"I don't read papers anymore, I have Claude read them for me."
(attributed to Andrej Karpathy; use as a provocation to frame the problem)

Cover these ideas in ≤300 words:
- The actual problem: you've read dozens of papers but can't recall or connect them
- Why RAG alone isn't the answer (retrieval without synthesis)
- The thesis: LLMs can compile a structured wiki from raw papers, and that wiki becomes a better knowledge base than a vector index
- One-line preview of the experiment (36 papers, two systems, GPT-4o as judge)

Do NOT start with "I". Hook first line must be a concrete observation or provocation.
"""
    return generate_post(client, 1, system, user)


def build_linkedin_2(client: OpenAI) -> str:
    compile_data = load_compile_data()
    system = f"You are writing a LinkedIn post about building a personal AI knowledge base.\n{LINKEDIN_TONE_GUIDE}"
    user = f"""Write LinkedIn Post 2 of a 4-part series.

Topic: Compilation stats + Obsidian wiki visual — what the LLM-compiled wiki looks like.

Data to include (use exact numbers):
- 36 papers → 259 concept articles, zero manual edits
- Compilation token cost: ${compile_data.get('total_cost', 0):.2f} total
- Summarization: {compile_data.get('summarize_tokens', 0):,} tokens
- Concept writing: {compile_data.get('concept_tokens', 0):,} tokens
- Output browsable as an Obsidian graph (wikilink syntax [[concept]])

Describe what the Obsidian graph looks like when you open it — concepts as nodes, links between them, clusters forming around topics like "chain-of-thought", "quantization", "retrieval".

Note that a visual/GIF of the graph will accompany this post.

Cover: what surprised you about the graph structure (unexpected connections, isolated nodes, concept clusters that formed naturally).

≤300 words. Hook on line 1.
"""
    return generate_post(client, 2, system, user)


def build_linkedin_3(client: OpenAI) -> str:
    system = f"You are writing a LinkedIn post about building a personal AI knowledge base.\n{LINKEDIN_TONE_GUIDE}"
    user = """Write LinkedIn Post 3 of a 4-part series.

Topic: Key design decisions in building the RAG baseline — chunking, embeddings, retrieval.

Cover these 3 concrete decisions (briefly, ≤2 lines each):
1. Chunk size: 800 tokens max with 50-token overlap (why: preserves paragraph context without over-fragmenting)
2. Embeddings: text-embedding-3-small via direct API, not ChromaDB wrapper (why: reproducibility, explicit batching)
3. Retrieval: top-10 chunks by cosine similarity, score threshold none (why: let the LLM filter irrelevance)

Then: the one thing you got wrong first (describe the ChromaDB schema mismatch bug from mixing old and new chunk formats — had to delete the DB and re-ingest).

Note that a chunking diagram will accompany this post.

≤300 words. Start with a concrete claim about chunking being underrated.
"""
    return generate_post(client, 3, system, user)


def build_linkedin_4(client: OpenAI) -> str:
    eval_data = load_eval_data()

    # Pick the single most surprising example (largest divergence)
    top_pair = eval_data["qa_pairs"][0] if eval_data["qa_pairs"] else {}

    system = f"You are writing a LinkedIn post about building a personal AI knowledge base.\n{LINKEDIN_TONE_GUIDE}"
    user = f"""Write LinkedIn Post 4 of a 4-part series.

Topic: The eval results — score table + one surprising example.

Include this score table verbatim (markdown):

| Category | Wiki | RAG |
|---|---|---|
| Accuracy | 4.6 | 4.4 |
| Completeness | 4.6 | 4.3 |
| Citation | 2.5 | 2.7 |
| Synthesis | 4.3 | 4.1 |
| **Overall** | **4.0** | **3.88** |

Win/loss: Wiki 3, RAG 5, Ties 2 (out of 10 questions)

Cost: Wiki ${eval_data['wiki_cost']:.4f} vs RAG ${eval_data['rag_cost']:.4f} per 10 queries

The surprising example to feature (Q{top_pair.get('id','7')}):
- Question: {top_pair.get('question', 'What is speculative decoding?')}
- Wiki scored {top_pair.get('wiki_score', 17)}/20, RAG scored {top_pair.get('rag_score', 4)}/20
- Why: {top_pair.get('reasoning', 'The paper was not indexed in RAG at query time')}

Takeaway: RAG won overall but had one catastrophic failure; wiki was more consistent.
What this means: for a personal corpus you control, a compiled wiki is worth the extra cost.

≤300 words. Open with the score table or the surprising result — not a preamble.
"""
    return generate_post(client, 4, system, user)


# ── CLI ───────────────────────────────────────────────────────────────────────

POST_BUILDERS = {
    1: build_post_1,
    2: build_post_2,
    3: build_post_3,
    4: build_post_4,
}

LINKEDIN_BUILDERS = {
    1: build_linkedin_1,
    2: build_linkedin_2,
    3: build_linkedin_3,
    4: build_linkedin_4,
}

@click.command()
@click.option("--post", default=0, type=int, help="Generate a single post (1-4). Default: all.")
@click.option("--linkedin", is_flag=True, default=False, help="Generate LinkedIn posts instead of Substack posts.")
def main(post: int, linkedin: bool) -> None:
    """Generate Substack or LinkedIn draft posts from eval and wiki data."""
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    client = OpenAI()

    builders = LINKEDIN_BUILDERS if linkedin else POST_BUILDERS
    label = "LinkedIn" if linkedin else "Substack"
    prefix = "linkedin_" if linkedin else "post_"

    posts_to_run = [post] if post in builders else list(builders.keys())

    for num in posts_to_run:
        print(f"Generating {label} Post {num}...")
        content = builders[num](client)
        out = DRAFTS_DIR / f"{prefix}{num}.md"
        out.write_text(content, encoding="utf-8")
        print(f"  Wrote {out} ({len(content):,} chars)")

    print(f"\nDone. Drafts in {DRAFTS_DIR}/")


if __name__ == "__main__":
    main()
