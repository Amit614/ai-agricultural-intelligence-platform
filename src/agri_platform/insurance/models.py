from pydantic import BaseModel
class InsuranceProfile(BaseModel):
    farmer_id:str
    crop:str
    area_hectares:float
    weather_risk:float
    insured_amount:float
