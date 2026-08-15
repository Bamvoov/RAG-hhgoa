import re, math
from collections import Counter
from .base import BaseChunker, Chunk
def cos(a,b):
    keys=set(a)|set(b); dot=sum(a[k]*b[k] for k in keys); na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values())); return dot/(na*nb) if na and nb else 0.0
def vec(s): return Counter(s.lower().split())
class SemanticChunker(BaseChunker):
    name='semantic'
    def __init__(self, threshold=0.55, chunk_size=650): self.threshold=threshold; self.chunk_size=chunk_size
    def chunk(self, doc):
        sents=[s for s in re.split(r'(?<=[.!?])\s+', doc.get('text','').strip()) if s]; chunks=[]; buf=[]; idx=0
        for s in sents:
            if buf and (cos(vec(buf[-1]),vec(s))<self.threshold or sum(map(len,buf))+len(s)>self.chunk_size):
                chunks.append(Chunk(f"{doc.get('id','doc')}:sem:{idx}", str(doc.get('id','doc')), ' '.join(buf), {'chunk_index':idx,'split_reason':'topic_shift'})); idx+=1; buf=[]
            buf.append(s)
        if buf: chunks.append(Chunk(f"{doc.get('id','doc')}:sem:{idx}", str(doc.get('id','doc')), ' '.join(buf), {'chunk_index':idx}))
        return chunks
