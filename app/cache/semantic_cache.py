import time, math
from .cache_metrics import CacheMetrics
class SemanticCache:
    def __init__(self, embedder, ttl_minutes=10, similarity_threshold=0.92): self.embedder=embedder; self.ttl=ttl_minutes*60; self.th=similarity_threshold; self.entries=[]; self.metrics=CacheMetrics()
    def _cos(self,a,b): return sum(x*y for x,y in zip(a,b))/(math.sqrt(sum(x*x for x in a))*math.sqrt(sum(y*y for y in b)) or 1)
    def lookup(self, query):
        start=time.perf_counter(); now=time.time(); self.entries=[e for e in self.entries if now-e['timestamp']<=self.ttl]; emb=self.embedder.embed([query])[0]
        best=max(self.entries, key=lambda e:self._cos(emb,e['embedding']), default=None)
        if best and self._cos(emb,best['embedding'])>=self.th:
            best['hit_count']+=1; self.metrics.hits+=1; self.metrics.llm_calls_saved+=1; self.metrics.total_hit_latency_ms+=(time.perf_counter()-start)*1000; return best['answer']
        self.metrics.misses+=1; return None
    def add(self, query, answer): self.entries.append({'query':query,'embedding':self.embedder.embed([query])[0],'answer':answer,'timestamp':time.time(),'hit_count':0})
