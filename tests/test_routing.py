from app.generation.router import GenerationRouter
def test_routes():
    r=GenerationRouter(); assert r.route(0.96)=='fast'; assert r.route(0.8)=='slow-small'; assert r.route(0.1)=='slow-large'
