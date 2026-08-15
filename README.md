# Voice-Enabled RAG

A FastAPI voice/text RAG scaffold with local vector retrieval, BM25 hybrid search, guardrails, semantic cache, path routing, streaming hooks, and latency reporting. The <200ms target is scoped to retrieval (chunking/index lookup/context assembly), while STT and LLM generation are reported separately.

## Setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python data/prepare_dataset.py
python -m app.indexing.build_index
uvicorn app.main:app --reload
```

## Configuration

Edit `config.yaml` to switch chunking strategy, embedding model, retrieval top-k, semantic cache TTL/threshold, and fast/slow routing thresholds without code changes.

## Chunking strategies

- FixedSizeChunker: baseline fixed character windows with overlap.
- RecursiveChunker: sentence-aware recursive chunking.
- SemanticChunker: sentence topic-shift chunking using cosine similarity.
- MetadataAwareChunker: recursive chunks plus doc id, offsets, language, source query, and length bucket metadata.

## Latency report

Run `python scripts/run_latency_suite.py` to write `reports/latency_results.csv` and `reports/latency_report.md` with P50/P70/P100, cache hit rate, LLM calls saved, and per-path data.
