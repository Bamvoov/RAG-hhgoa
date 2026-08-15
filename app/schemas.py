from dataclasses import dataclass, field
from typing import Any
@dataclass
class QueryRequest: text: str | None = None
@dataclass
class ErrorResponse: stage: str; message: str
@dataclass
class QueryResponse:
    answer: str
    path: str
    cache: str
    latencies: list[dict[str, Any]] = field(default_factory=list)
    guardrails: list[dict[str, Any]] = field(default_factory=list)
    cache_metrics: dict[str, Any] = field(default_factory=dict)
    error: dict[str, str] | None = None
