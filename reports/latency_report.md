# Latency Report

Retrieval path target is <200ms; STT and generation are reported separately because network STT cannot honestly fit a <200ms end-to-end claim.

| Metric | P50 | P70 | P100 |
|---|---:|---:|---:|
| retrieval | 0.00 | 0.00 | 0.05 |
| semantic cache hits | 0.05 | 0.05 | 0.05 |
| full end-to-end | 0.05 | 0.05 | 0.34 |

Time-to-First-Word is tracked separately from full generation; local fallback reports 0ms TTFW in this offline harness.

Cache hit rate: 96.00%; LLM calls saved: 48.
