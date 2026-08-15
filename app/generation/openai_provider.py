class OpenAIProvider:
    def generate(self, query, chunks): return 'I do not have enough information to answer that.' if not chunks else 'Answer from context: '+chunks[0]['text']
