from pydantic import BaseModel
from typing import List
class Recommendation(BaseModel):
    category:str
    recommendation:str
    confidence:float
    reasons:List[str]=[]
