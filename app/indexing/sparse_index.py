from collections import Counter
class BM25Index:
    def __init__(self): self.chunks=[]; self.counts=[]
    def build(self,chunks): self.chunks=list(chunks); self.counts=[Counter(c.text.lower().split()) for c in self.chunks]
    def query(self,q,top_k=5): return sorted([(c,sum(cnt[t] for t in q.lower().split())) for c,cnt in zip(self.chunks,self.counts)], key=lambda x:x[1], reverse=True)[:top_k]
