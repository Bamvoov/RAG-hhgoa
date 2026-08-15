DOMAIN={'what','who','when','where','how','is','are','the','of','in','for','health','science','history','india','passage','answer','retrieval'}
def check_off_topic(text):
    toks=set(text.lower().split()); score=len(toks & DOMAIN)/max(1,len(toks)); return {'name':'off_topic','allowed':score>=0.05 or len(text.split())<4,'reason':f'domain_score={score:.2f}'}
