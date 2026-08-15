from app.pipeline.orchestrator import Pipeline
def test_pipeline_happy_path():
    r=Pipeline().run(text='what is India capital'); assert r.answer; assert r.error is None
def test_pipeline_forced_generation_failure():
    p=Pipeline(); p.large.generate=lambda q,c: (_ for _ in ()).throw(RuntimeError('down')); r=p.run(text='zzzz weak query'); assert r.error or r.answer
