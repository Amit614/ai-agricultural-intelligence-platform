class KnowledgeTool:
    def __init__(self, registry):
        self.registry=registry
    def lookup(self, category,key):
        return self.registry.get(category,key)
