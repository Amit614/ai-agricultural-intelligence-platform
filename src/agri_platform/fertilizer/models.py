from pydantic import BaseModel
class NutrientProfile(BaseModel):
    crop:str
    nitrogen:float
    phosphorus:float
    potassium:float
    soil_ph:float
