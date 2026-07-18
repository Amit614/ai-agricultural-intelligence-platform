from .models import KnowledgeRecord

class KnowledgeRegistry:
    def __init__(self):
        self._records={}
    def register(self,record:KnowledgeRecord):
        self._records[(record.category,record.key)] = record
    def get(self,category,key):
        return self._records.get((category,key))
    def list_category(self,category):
        return [r for (c,_),r in self._records.items() if c==category]
