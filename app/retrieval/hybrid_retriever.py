class HybridRetriever:
    def __init__(self, embedder, vector_store, sparse_index, rrf_k=60): self.embedder=embedder; self.vector_store=vector_store; self.sparse_index=sparse_index; self.rrf_k=rrf_k
    def retrieve(self, query, top_k=5):
        qemb=self.embedder.embed([query])[0]; scores={}
        for results in (self.vector_store.query(qemb,top_k), self.sparse_index.query(query,top_k)):
            for rank,(chunk,score) in enumerate(results,1): scores.setdefault(chunk.chunk_id,[chunk,0.0]); scores[chunk.chunk_id][1]+=1/(self.rrf_k+rank)+float(score)*0.001
        return [{'chunk_id':c.chunk_id,'doc_id':c.doc_id,'text':c.text,'metadata':c.metadata,'score':s} for c,s in sorted(scores.values(), key=lambda x:x[1], reverse=True)[:top_k]]
