def check_grounding(answer, chunks):
    ctx=' '.join(c.get('text','').lower() for c in chunks); words=[w for w in answer.lower().split() if len(w)>4]
    ok=not words or any(w in ctx for w in words) or 'not have enough' in answer.lower(); return {'name':'grounding','allowed':ok,'reason':'answer overlaps retrieved context' if ok else 'answer unsupported by chunks'}
