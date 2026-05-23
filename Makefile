PYTHON := python3
SHELL  := /bin/bash

.PHONY: help install ingest compile-wiki lint-wiki run-rag run-wiki-qa run-eval search fetch-papers

help:
	@echo "wiki-brain targets:"
	@echo "  install          Install dependencies into the active venv"
	@echo "  fetch-papers     Fetch open-access PDFs from Semantic Scholar"
	@echo "  ingest           Chunk + embed raw/ docs into ChromaDB"
	@echo "  compile-wiki     LLM-compile raw/ → wiki/ (incremental)"
	@echo "  lint-wiki        LLM health-check wiki/ articles"
	@echo "  run-rag          Interactive RAG Q&A (ChromaDB-backed)"
	@echo "  run-wiki-qa      Interactive wiki Q&A (wiki/ as context)"
	@echo "  run-eval         Run both systems on eval/questions.md"
	@echo "  search Q=...     Naive wiki search  (e.g. make search Q='attention')"
	@echo "  generate-posts   Generate all 4 Substack drafts"
	@echo "  generate-linkedin Generate all 4 LinkedIn drafts"
	@echo "  generate-linkedin-post N=2  Generate one LinkedIn post"

install:
	pip install -r requirements.txt

ingest:
	$(PYTHON) -m rag.ingest

ingest-force:
	$(PYTHON) -m rag.ingest --force

compile-wiki:
	$(PYTHON) -m wiki_compiler.compile

compile-wiki-force:
	$(PYTHON) -m wiki_compiler.compile --force

lint-wiki:
	$(PYTHON) -m wiki_compiler.lint

lint-wiki-fix:
	$(PYTHON) -m wiki_compiler.lint --fix

lint-wiki-fast:
	$(PYTHON) -m wiki_compiler.lint --skip-llm

run-rag:
	$(PYTHON) -m rag.qa --interactive

run-wiki-qa:
	$(PYTHON) -m wiki_compiler.query --interactive

run-eval:
	$(PYTHON) -m eval.run_eval

run-eval-rag:
	$(PYTHON) -m eval.run_eval --system rag

run-eval-wiki:
	$(PYTHON) -m eval.run_eval --system wiki

search:
	@if [ -z "$(Q)" ]; then echo "Usage: make search Q='your query'"; exit 1; fi
	$(PYTHON) -m tools.search "$(Q)"

generate-posts:
	$(PYTHON) -m tools.blog_generator

generate-post:
	@if [ -z "$(N)" ]; then echo "Usage: make generate-post N=4"; exit 1; fi
	$(PYTHON) -m tools.blog_generator --post $(N)

generate-linkedin:
	$(PYTHON) -m tools.blog_generator --linkedin

generate-linkedin-post:
	@if [ -z "$(N)" ]; then echo "Usage: make generate-linkedin-post N=2"; exit 1; fi
	$(PYTHON) -m tools.blog_generator --linkedin --post $(N)

fetch-papers:
	$(PYTHON) -m tools.fetch_papers

fetch-papers-dry:
	$(PYTHON) -m tools.fetch_papers --dry-run

fetch-papers-tag:
	@if [ -z "$(TAG)" ]; then echo "Usage: make fetch-papers-tag TAG=rag_retrieval"; exit 1; fi
	$(PYTHON) -m tools.fetch_papers --tag $(TAG)
