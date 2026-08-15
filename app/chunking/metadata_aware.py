from .recursive import RecursiveChunker
class MetadataAwareChunker(RecursiveChunker):
    name='metadata_aware'
    def chunk(self, doc):
        chunks=super().chunk(doc); length=len(doc.get('text','')); bucket='short' if length<500 else 'medium' if length<1500 else 'long'
        for c in chunks: c.metadata.update({'original_doc_id':c.doc_id,'passage_length_bucket':bucket,'source_query_id':doc.get('source_query_id'),'language':doc.get('language','unknown')})
        return chunks
