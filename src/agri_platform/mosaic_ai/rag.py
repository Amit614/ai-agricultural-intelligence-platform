class RAGService:
    def __init__(self, vector_index):
        self.vector_index = vector_index
    def retrieve(self, query:str, top_k:int=3):
        return self.vector_index.search(query, top_k)
