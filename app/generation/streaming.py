import time
def stream_text(text):
    first=None; start=time.perf_counter()
    for token in text.split():
        if first is None: first=time.perf_counter()
        yield token
