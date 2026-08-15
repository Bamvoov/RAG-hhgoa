from app.schemas import QueryResponse
from app.observability.timing import TimingLog
from app.indexing.embedder import Embedder
from app.indexing.vector_store import LocalVectorStore
from app.indexing.sparse_index import BM25Index
from app.chunking.metadata_aware import MetadataAwareChunker
from app.retrieval.hybrid_retriever import HybridRetriever
from app.cache.semantic_cache import SemanticCache
from app.generation.router import GenerationRouter
from app.generation.local_small_provider import LocalSmallProvider
from app.generation.openai_provider import OpenAIProvider
from app.guardrails.input_safety import check_input_safety
from app.guardrails.off_topic import check_off_topic
from app.guardrails.grounding_check import check_grounding
class Pipeline:
    def __init__(self):
        self.timing=TimingLog(); self.embedder=Embedder(); self.cache=SemanticCache(self.embedder); self.router=GenerationRouter(); self.small=LocalSmallProvider(); self.large=OpenAIProvider()
        docs=[{'id':'sample-1','text':'India is a country in South Asia. Its capital is New Delhi and it has many languages.','language':'en'},{'id':'sample-2','text':'Retrieval augmented generation answers questions by grounding responses in retrieved passages.','language':'en'}]
        chunks=[]; ch=MetadataAwareChunker()
        for d in docs: chunks += ch.chunk(d)
        for c,e in zip(chunks,self.embedder.embed([c.text for c in chunks])): c.embedding=e
        self.vector=LocalVectorStore(); self.vector.add(chunks); self.sparse=BM25Index(); self.sparse.build(chunks); self.retriever=HybridRetriever(self.embedder,self.vector,self.sparse)
    def run(self, text=None, audio=None):
        self.timing=TimingLog(); guards=[]; path='unknown'; cache_state='miss'
        try:
            with self.timing.stage('transcribe'): query=text or 'transcribed audio query'
            for fn in (check_input_safety, check_off_topic):
                with self.timing.stage(fn.__name__): verdict=fn(query); guards.append(verdict)
                if not verdict['allowed']: return self._resp('Out of scope or unsafe request.', 'blocked', cache_state, guards)
            with self.timing.stage('semantic_cache'): cached=self.cache.lookup(query)
            if cached: return self._resp(cached, 'cache', 'hit', guards)
            with self.timing.stage('retrieve'):
                chunks=self.retriever.retrieve(query); top=chunks[0]['score'] if chunks else 0.0
            path=self.router.route(top)
            with self.timing.stage('generate'):
                answer=chunks[0]['text'] if path=='fast' else self.small.generate(query,chunks) if path=='slow-small' else self.large.generate(query,chunks)
            with self.timing.stage('guardrail_output'):
                g=check_grounding(answer,chunks); guards.append(g)
                if not g['allowed']: answer="I don't have enough information to answer that."
            self.cache.add(query, answer); return self._resp(answer,path,cache_state,guards)
        except Exception as e:
            return self._resp('Pipeline failed.', path, cache_state, guards, {'stage':getattr(e,'stage','pipeline'),'message':str(e)})
    def _resp(self, answer, path, cache_state, guards, error=None):
        m=self.cache.metrics
        return QueryResponse(answer=answer,path=path,cache=cache_state,latencies=self.timing.events,guardrails=guards,cache_metrics={'hit_rate':m.hit_rate,'average_cache_hit_latency_ms':m.average_hit_latency_ms,'llm_calls_saved':m.llm_calls_saved},error=error)
