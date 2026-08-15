import re
from .base import BaseChunker, Chunk
class RecursiveChunker(BaseChunker):
    name='recursive'
    def __init__(self, chunk_size=450, overlap=60): self.chunk_size=chunk_size; self.overlap=overlap
    def chunk(self, doc):
        sents=[s for s in re.split(r'(?<=[.!?])\s+', doc.get('text','').strip()) if s]; chunks=[]; buf=''; idx=0; start=0
        for sent in sents:
            if buf and len(buf)+len(sent)+1>self.chunk_size:
                chunks.append(Chunk(f"{doc.get('id','doc')}:rec:{idx}", str(doc.get('id','doc')), buf.strip(), {'chunk_index':idx,'start':start,'end':start+len(buf)})); idx+=1; start=max(0,start+len(buf)-self.overlap); buf=buf[-self.overlap:]+' '+sent
            else: buf=(buf+' '+sent).strip()
        if buf: chunks.append(Chunk(f"{doc.get('id','doc')}:rec:{idx}", str(doc.get('id','doc')), buf.strip(), {'chunk_index':idx,'start':start,'end':start+len(buf)}))
        return chunks
