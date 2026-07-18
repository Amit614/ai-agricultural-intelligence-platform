from pydantic import BaseModel
from typing import List
class FarmerProfile(BaseModel):
    farmer_id:str
    name:str
    village:str
    land_hectares:float
    preferred_language:str
    crops:List[str]=[]
