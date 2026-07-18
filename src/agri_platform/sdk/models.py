from pydantic import BaseModel
class Dataset(BaseModel):
    name:str
    source:str
    enabled:bool=True
