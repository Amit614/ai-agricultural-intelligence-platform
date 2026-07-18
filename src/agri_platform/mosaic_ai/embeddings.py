class EmbeddingProvider:
    def embed(self, text:str):
        # Placeholder until Databricks embedding endpoint is configured
        return [float((ord(c) % 31))/31.0 for c in text[:64]]
