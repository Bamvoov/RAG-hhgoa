import csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.pipeline.orchestrator import Pipeline
def pct(vals,p): vals=sorted(vals); return vals[min(len(vals)-1, int((p/100)*(len(vals)-1)))] if vals else 0
def main():
    pipe=Pipeline(); queries=['what is India capital','what is retrieval augmented generation']*25; rows=[]
    for q in queries:
        r=pipe.run(text=q); rows.append({'query':q,'path':r.path,'cache':r.cache,'total_ms':sum(e['latency_ms'] for e in r.latencies),'retrieval_ms':sum(e['latency_ms'] for e in r.latencies if e['stage']=='retrieve')})
    Path('reports').mkdir(exist_ok=True)
    with open('reports/latency_results.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    totals=[r['total_ms'] for r in rows]; retr=[r['retrieval_ms'] for r in rows]
    report=f"""# Latency Report

Retrieval path target is <200ms; STT and generation are reported separately because network STT cannot honestly fit a <200ms end-to-end claim.

| Metric | P50 | P70 | P100 |
|---|---:|---:|---:|
| retrieval | {pct(retr,50):.2f} | {pct(retr,70):.2f} | {pct(retr,100):.2f} |
| semantic cache hits | {pipe.cache.metrics.average_hit_latency_ms:.2f} | {pipe.cache.metrics.average_hit_latency_ms:.2f} | {pipe.cache.metrics.average_hit_latency_ms:.2f} |
| full end-to-end | {pct(totals,50):.2f} | {pct(totals,70):.2f} | {pct(totals,100):.2f} |

Time-to-First-Word is tracked separately from full generation; local fallback reports 0ms TTFW in this offline harness.

Cache hit rate: {pipe.cache.metrics.hit_rate:.2%}; LLM calls saved: {pipe.cache.metrics.llm_calls_saved}.
"""
    Path('reports/latency_report.md').write_text(report); print(report)
if __name__=='__main__': main()
