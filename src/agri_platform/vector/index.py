from typing import List
class VectorIndex:
    def __init__(self):
        self.docs=[]
    def add(self,text:str,metadata:dict|None=None):
        self.docs.append({'text':text,'metadata':metadata or {}})
    def search(self,query:str,top_k:int=3)->List[dict]:
        q=query.lower().split()
        scored=[]
        for d in self.docs:
            score=sum(1 for w in q if w in d['text'].lower())
            scored.append((score,d))
        return [d for s,d in sorted(scored,key=lambda x:x[0],reverse=True)[:top_k] if s>0]
