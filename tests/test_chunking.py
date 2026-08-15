from app.chunking.fixed_size import FixedSizeChunker
from app.chunking.recursive import RecursiveChunker
from app.chunking.semantic import SemanticChunker
from app.chunking.metadata_aware import MetadataAwareChunker
DOC={'id':'d1','text':'This is sentence one. This is sentence two about India. This is sentence three about retrieval.','language':'en'}
def test_chunkers_no_data_loss():
    for cls in (FixedSizeChunker,RecursiveChunker,SemanticChunker,MetadataAwareChunker):
        chunks=cls().chunk(DOC); assert chunks; assert 'sentence' in ' '.join(c.text for c in chunks); assert chunks[0].doc_id=='d1'
