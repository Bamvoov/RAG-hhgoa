import time
from app.indexing.embedder import Embedder
from app.cache.semantic_cache import SemanticCache
def test_cache_hit_and_miss():
    c=SemanticCache(Embedder(), ttl_minutes=10, similarity_threshold=0.5); c.add('india capital', 'New Delhi'); assert c.lookup('india capital')=='New Delhi'; assert c.lookup('quantum banana') is None
def test_cache_ttl():
    c=SemanticCache(Embedder(), ttl_minutes=0, similarity_threshold=0.5); c.add('india capital', 'New Delhi'); time.sleep(0.01); assert c.lookup('india capital') is None
