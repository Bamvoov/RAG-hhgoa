class LocalVectorStore:
    def __init__(self): self.items=[]
    def add(self,chunks): self.items.extend(chunks)
    def query(self, embedding, top_k=5): return sorted([(c, sum(a*b for a,b in zip(embedding,c.embedding or []))) for c in self.items], key=lambda x:x[1], reverse=True)[:top_k]
