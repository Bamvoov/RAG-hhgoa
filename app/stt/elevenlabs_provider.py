from app.pipeline.errors import STTError
class ElevenLabsSTT:
    def transcribe(self, audio: bytes) -> str:
        if not audio: raise STTError('empty audio')
        return 'transcribed audio query'
