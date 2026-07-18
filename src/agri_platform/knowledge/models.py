from pydantic import BaseModel
from typing import Dict

class KnowledgeRecord(BaseModel):
    category:str
    key:str
    title:str
    metadata:Dict[str,str]={}
    content:str
