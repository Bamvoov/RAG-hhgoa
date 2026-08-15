from app.pipeline.orchestrator import Pipeline
def test_known_query_returns_relevant_chunk():
    r=Pipeline().retriever.retrieve('India capital', top_k=1); assert 'India' in r[0]['text']
