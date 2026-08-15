from fastapi import FastAPI, UploadFile, File, Form
from app.pipeline.orchestrator import Pipeline
app=FastAPI(title='Voice Enabled RAG')
pipeline=Pipeline()
@app.post('/query')
async def query(text: str | None = Form(default=None), audio: UploadFile | None = File(default=None)):
    audio_bytes=await audio.read() if audio else None
    return pipeline.run(text=text, audio=audio_bytes)
