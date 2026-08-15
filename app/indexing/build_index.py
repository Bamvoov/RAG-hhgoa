import json
from pathlib import Path
from app.chunking import get_chunker
from app.indexing.embedder import Embedder
def build(passages_path='data/processed/passages.jsonl', strategy='metadata_aware'):
    chunker=get_chunker(strategy); embedder=Embedder(); chunks=[]
    for line in Path(passages_path).read_text().splitlines(): chunks.extend(chunker.chunk(json.loads(line)))
    for c,e in zip(chunks, embedder.embed([c.text for c in chunks])): c.embedding=e
    return chunks
if __name__=='__main__': print(f'built {len(build())} chunks')
