class GenerationRouter:
    def __init__(self, fast_path_threshold=0.95, slow_path_threshold=0.75): self.fast=fast_path_threshold; self.slow=slow_path_threshold
    def route(self, score): return 'fast' if score>self.fast else 'slow-small' if score>=self.slow else 'slow-large'
