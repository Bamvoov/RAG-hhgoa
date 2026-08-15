import hashlib, math
class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2', dim=64): self.model_name=model_name; self.dim=dim
    def embed(self, texts): return [self._one(t) for t in texts]
    def _one(self,text):
        v=[0.0]*self.dim
        for tok in text.lower().split(): v[int(hashlib.sha1(tok.encode()).hexdigest(),16)%self.dim]+=1.0
        n=math.sqrt(sum(x*x for x in v)) or 1.0; return [x/n for x in v]
