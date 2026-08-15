class LocalSmallProvider:
    def generate(self, query, chunks): return 'Based on retrieved context: '+(chunks[0]['text'] if chunks else 'I do not have enough information.')
