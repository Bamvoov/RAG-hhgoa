import time
from contextlib import contextmanager
class TimingLog:
    def __init__(self): self.events=[]
    @contextmanager
    def stage(self,name):
        s=time.perf_counter(); ev={'stage':name,'start_ts':s,'success':False}
        try: yield ev; ev['success']=True
        finally:
            e=time.perf_counter(); ev.update({'end_ts':e,'latency_ms':(e-s)*1000}); self.events.append(ev)
