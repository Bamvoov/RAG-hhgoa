from .fixed_size import FixedSizeChunker
from .recursive import RecursiveChunker
from .semantic import SemanticChunker
from .metadata_aware import MetadataAwareChunker
def get_chunker(name, **cfg): return {'fixed_size':FixedSizeChunker,'recursive':RecursiveChunker,'semantic':SemanticChunker,'metadata_aware':MetadataAwareChunker}[name](**cfg)
