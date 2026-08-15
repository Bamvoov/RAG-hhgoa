from .base import BaseChunker, Chunk
class FixedSizeChunker(BaseChunker):
    name='fixed_size'
    def __init__(self, chunk_size=450, overlap=60): self.chunk_size=chunk_size; self.overlap=overlap
    def chunk(self, doc):
        text=doc.get('text',''); out=[]; step=max(1,self.chunk_size-self.overlap)
        for i,start in enumerate(range(0,len(text),step)):
            part=text[start:start+self.chunk_size]
            if part: out.append(Chunk(f"{doc.get('id','doc')}:fixed:{i}", str(doc.get('id','doc')), part, {'chunk_index':i,'start':start,'end':start+len(part)}))
            if start+self.chunk_size>=len(text): break
        return out
