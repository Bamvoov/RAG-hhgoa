from dataclasses import dataclass
@dataclass
class CacheMetrics:
    hits:int=0; misses:int=0; llm_calls_saved:int=0; total_hit_latency_ms:float=0.0
    @property
    def hit_rate(self): return self.hits/(self.hits+self.misses) if self.hits+self.misses else 0.0
    @property
    def average_hit_latency_ms(self): return self.total_hit_latency_ms/self.hits if self.hits else 0.0
