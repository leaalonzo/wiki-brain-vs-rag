"""
Phase 4 — Evaluation harness: Wiki vs RAG, judged by gpt-4o.

For each question in eval/questions.md:
  1. Run Wiki system  → {answer, articles_used, token_count, latency_ms}
  2. Run RAG system   → {answer, sources_used, chunks_retrieved, token_count, latency_ms}
  3. Run Judge        → pairwise scores on accuracy/completeness/citation/synthesis + winner
  4. Save             → eval/results/{question_id}.json

Final output: eval/results/summary.md

Usage:
    python -m eval.run_eval
    python -m eval.run_eval --system rag
    python -m eval.run_eval --system wiki
    python -m eval.run_eval --no-judge       # skip LLM judge, record answers only
"""

import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

import click
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

QUESTIONS_FILE = Path("eval/questions.md")
RESULTS_DIR = Path("eval/results")
JUDGE_MODEL = os.getenv("QA_MODEL", "gpt-4o")

JUDGE_PROMPT = """You are evaluating two AI systems answering a research question.
Question: {question}
System A answer: {wiki_answer}
System B answer: {rag_answer}

Rate each answer from 1-5 on:
- Accuracy (is it factually correct based on learning science?)
- Completeness (does it fully address the question?)
- Citation quality (does it properly reference sources?)
- Synthesis (does it connect ideas across multiple sources?)

Output JSON:
{{
  "systemA": {{"accuracy": 1-5, "completeness": 1-5, "citation": 1-5, "synthesis": 1-5}},
  "systemB": {{"accuracy": 1-5, "completeness": 1-5, "citation": 1-5, "synthesis": 1-5}},
  "winner": "A" or "B" or "tie",
  "reasoning": "one sentence explaining the winner decision"
}}"""


# ── Question parsing ──────────────────────────────────────────────────────────

def parse_questions(md_text: str) -> list[dict]:
    """Parse Q/A/Source entries from questions.md, skipping placeholders."""
    entries = []
    for block in re.split(r"\n(?=\d+\.\s)", md_text):
        num_match = re.match(r"(\d+)\.", block.strip())
        q_match = re.search(r"\*\*Q\*\*:\s*(.+)", block)
        a_match = re.search(r"\*\*A\*\*:\s*(.+)", block)
        s_match = re.search(r"\*\*Source\*\*:\s*(.+)", block)
        if not (q_match and a_match):
            continue
        q = q_match.group(1).strip()
        a = a_match.group(1).strip()
        if "_Replace with" in q or "_Replace with" in a:
            continue
        entries.append({
            "id": num_match.group(1) if num_match else str(len(entries) + 1),
            "question": q,
            "reference": a,
            "source": s_match.group(1).strip() if s_match else "",
        })
    return entries


# ── System runners ────────────────────────────────────────────────────────────

def run_wiki(question: str) -> dict:
    from wiki_compiler.query import answer
    t0 = time.time()
    result = answer(question)
    # answer() already tracks latency internally, but we re-measure for consistency
    result.setdefault("latency_ms", int((time.time() - t0) * 1000))
    return result


def run_rag(question: str) -> dict:
    from rag.qa import answer
    t0 = time.time()
    result = answer(question, top_k=10)
    result["latency_ms"] = int((time.time() - t0) * 1000)
    # Normalise: extract top similarity scores from chunks
    chunks = result.get("chunks_retrieved", [])
    result["top_scores"] = [round(c["score"], 4) for c in chunks[:5]]
    return result


# ── Judge ─────────────────────────────────────────────────────────────────────

def run_judge(client: OpenAI, question: str, wiki_answer: str, rag_answer: str) -> dict:
    """Pairwise evaluation: Wiki=A, RAG=B. Returns scores + winner."""
    response = client.chat.completions.create(
        model=JUDGE_MODEL,
        messages=[
            {
                "role": "user",
                "content": JUDGE_PROMPT.format(
                    question=question,
                    wiki_answer=wiki_answer,
                    rag_answer=rag_answer,
                ),
            }
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        return {}


# ── Per-question result ───────────────────────────────────────────────────────

def eval_question(
    entry: dict,
    client: OpenAI,
    run_systems: set[str],
    no_judge: bool,
) -> dict:
    q = entry["question"]
    result: dict = {
        "id": entry["id"],
        "question": q,
        "reference": entry["reference"],
        "source": entry["source"],
        "timestamp": datetime.now(tz=None).isoformat(),
    }

    wiki_result = rag_result = None

    if "wiki" in run_systems:
        print("    [wiki] answering...")
        try:
            wiki_result = run_wiki(q)
            result["wiki"] = {
                "answer": wiki_result["answer"],
                "articles_used": wiki_result.get("articles_used", []),
                "token_count": wiki_result.get("token_count", 0),
                "latency_ms": wiki_result.get("latency_ms", 0),
            }
        except Exception as exc:
            print(f"    [wiki] ERROR: {exc}")
            result["wiki"] = {"answer": f"ERROR: {exc}", "articles_used": [], "token_count": 0, "latency_ms": 0}

    if "rag" in run_systems:
        print("    [rag]  answering...")
        try:
            rag_result = run_rag(q)
            result["rag"] = {
                "answer": rag_result["answer"],
                "sources_used": rag_result.get("sources_used", []),
                "top_scores": rag_result.get("top_scores", []),
                "token_count": rag_result.get("token_count", 0),
                "latency_ms": rag_result.get("latency_ms", 0),
            }
        except Exception as exc:
            print(f"    [rag]  ERROR: {exc}")
            result["rag"] = {"answer": f"ERROR: {exc}", "sources_used": [], "top_scores": [], "token_count": 0, "latency_ms": 0}

    if not no_judge and wiki_result and rag_result:
        print("    [judge] evaluating...")
        try:
            verdict = run_judge(
                client, q,
                result["wiki"]["answer"],
                result["rag"]["answer"],
            )
            result["judge"] = verdict
            winner = verdict.get("winner", "?")
            print(f"    winner: {winner} — {verdict.get('reasoning', '')[:80]}")
        except Exception as exc:
            print(f"    [judge] ERROR: {exc}")

    return result


# ── Summary generation ────────────────────────────────────────────────────────

def _avg(values: list[float]) -> float:
    return round(sum(values) / len(values), 2) if values else 0.0


def generate_summary(all_results: list[dict], systems: set[str]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    n = len(all_results)

    judged = [r for r in all_results if "judge" in r]
    wins_a = sum(1 for r in judged if r["judge"].get("winner") == "A")
    wins_b = sum(1 for r in judged if r["judge"].get("winner") == "B")
    ties   = sum(1 for r in judged if r["judge"].get("winner") == "tie")

    # Per-category averages
    cats = ["accuracy", "completeness", "citation", "synthesis"]
    a_scores: dict[str, list[float]] = {c: [] for c in cats}
    b_scores: dict[str, list[float]] = {c: [] for c in cats}
    for r in judged:
        for c in cats:
            sa = r["judge"].get("systemA", {}).get(c)
            sb = r["judge"].get("systemB", {}).get(c)
            if sa is not None:
                a_scores[c].append(sa)
            if sb is not None:
                b_scores[c].append(sb)

    def score_table() -> str:
        header = "| Category | Wiki (A) | RAG (B) |\n|---|---|---|"
        rows = [
            f"| {c.capitalize()} | {_avg(a_scores[c])} | {_avg(b_scores[c])} |"
            for c in cats
        ]
        a_overall = _avg([v for vals in a_scores.values() for v in vals])
        b_overall = _avg([v for vals in b_scores.values() for v in vals])
        rows.append(f"| **Overall** | **{a_overall}** | **{b_overall}** |")
        return header + "\n" + "\n".join(rows)

    # Token + latency averages
    wiki_tokens  = _avg([r["wiki"]["token_count"]  for r in all_results if "wiki" in r])
    rag_tokens   = _avg([r["rag"]["token_count"]   for r in all_results if "rag"  in r])
    wiki_latency = _avg([r["wiki"]["latency_ms"]   for r in all_results if "wiki" in r])
    rag_latency  = _avg([r["rag"]["latency_ms"]    for r in all_results if "rag"  in r])

    # Most interesting cases: largest score gap between A and B
    def total_score(r: dict, system: str) -> float:
        return sum(r["judge"].get(system, {}).get(c, 0) for c in cats)

    interesting = sorted(
        judged,
        key=lambda r: abs(total_score(r, "systemA") - total_score(r, "systemB")),
        reverse=True,
    )[:3]

    interesting_md = ""
    for r in interesting:
        sa = total_score(r, "systemA")
        sb = total_score(r, "systemB")
        winner = r["judge"].get("winner", "?")
        reasoning = r["judge"].get("reasoning", "")
        interesting_md += (
            f"\n**Q{r['id']}**: {r['question'][:80]}...\n"
            f"- Wiki: {sa}/20  |  RAG: {sb}/20  |  Winner: {winner}\n"
            f"- {reasoning}\n"
        )

    per_question_rows = "".join(
        "| {} | {}... | {} | {}/20 | {}/20 |\n".format(
            r["id"],
            r["question"][:55],
            r["judge"].get("winner", "—") if "judge" in r else "—",
            total_score(r, "systemA") if "judge" in r else "—",
            total_score(r, "systemB") if "judge" in r else "—",
        )
        for r in all_results
    )

    return f"""# Eval Summary

> Generated: {now}  |  Questions evaluated: {n}

## Score Breakdown (1–5 per category)

{score_table() if judged else "_No judge results._"}

## Win / Loss / Tie

| | Count | % |
|---|---|---|
| Wiki wins (A) | {wins_a} | {round(wins_a/max(len(judged),1)*100)}% |
| RAG wins (B)  | {wins_b} | {round(wins_b/max(len(judged),1)*100)}% |
| Ties          | {ties}   | {round(ties/max(len(judged),1)*100)}% |

## Cost & Latency

| System | Avg tokens/query | Avg latency |
|---|---|---|
| Wiki | {wiki_tokens:,.0f} | {wiki_latency:,.0f} ms |
| RAG  | {rag_tokens:,.0f}  | {rag_latency:,.0f} ms |

## Most Interesting Cases

{interesting_md or "_None._"}

## Per-Question Results

| # | Question | Winner | Wiki score | RAG score |
|---|---|---|---|---|
{per_question_rows}"""


# ── CLI ───────────────────────────────────────────────────────────────────────

@click.command()
@click.option(
    "--system",
    type=click.Choice(["rag", "wiki", "both"]),
    default="both",
    show_default=True,
    help="Which system(s) to run.",
)
@click.option("--no-judge", is_flag=True, help="Skip LLM judge (record answers only).")
@click.option("--question-id", default=None, help="Run only question with this ID.")
def main(system: str, no_judge: bool, question_id: str | None) -> None:
    """Evaluate Wiki and/or RAG systems on eval/questions.md."""
    client = OpenAI()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if not QUESTIONS_FILE.exists():
        print(f"Questions file not found: {QUESTIONS_FILE}")
        return

    questions = parse_questions(QUESTIONS_FILE.read_text(encoding="utf-8"))
    if not questions:
        print("No real questions found in eval/questions.md.")
        return

    if question_id:
        questions = [q for q in questions if q["id"] == question_id]
        if not questions:
            print(f"Question id {question_id!r} not found.")
            return

    run_systems = {"rag", "wiki"} if system == "both" else {system}
    if no_judge or len(run_systems) < 2:
        no_judge = True

    print(f"Evaluating {len(questions)} question(s)  |  systems: {', '.join(sorted(run_systems))}  |  judge: {'no' if no_judge else 'yes'}\n")

    all_results = []
    for i, entry in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] Q{entry['id']}: {entry['question'][:70]}...")
        result = eval_question(entry, client, run_systems, no_judge)
        all_results.append(result)

        out = RESULTS_DIR / f"q{entry['id']}.json"
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"    Saved → {out}\n")

    summary_md = generate_summary(all_results, run_systems)
    summary_path = RESULTS_DIR / "summary.md"
    summary_path.write_text(summary_md, encoding="utf-8")
    print(f"Summary → {summary_path}")


if __name__ == "__main__":
    main()
