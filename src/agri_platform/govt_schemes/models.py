from pydantic import BaseModel
class SchemeEligibility(BaseModel):
    farmer_id:str
    land_hectares:float
    crop:str
    state:str
