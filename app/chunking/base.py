from dataclasses import dataclass, field
from typing import Any
@dataclass
class Chunk:
    chunk_id: str; doc_id: str; text: str; metadata: dict[str, Any] = field(default_factory=dict); embedding: list[float] | None = None
class BaseChunker:
    name='base'
    def chunk(self, doc: dict) -> list[Chunk]: raise NotImplementedError
