import hashlib, html, json, re
from pathlib import Path
def normalize(text): return re.sub(r'\s+', ' ', html.unescape(str(text))).strip()
def prepare(out='data/processed/passages.jsonl'):
    rows=[{'id':'sample-1','text':'India is a country in South Asia. Its capital is New Delhi.','source_query_id':'q1','language':'en'},{'id':'sample-2','text':'Retrieval augmented generation grounds answers in retrieved passages.','source_query_id':'q2','language':'en'}]
    seen=set(); clean=[]
    for r in rows:
        text=normalize(r['text']); h=hashlib.sha256(text.encode()).hexdigest()
        if text and h not in seen: seen.add(h); clean.append({**r,'text':text,'content_hash':h})
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    with open(out,'w') as f:
        for r in clean: f.write(json.dumps(r)+'\n')
    print(f'rows_before={len(rows)} rows_after={len(clean)} output={out}')
if __name__=='__main__': prepare()
