from pydantic import BaseModel
class IrrigationInput(BaseModel):
    crop:str
    soil_moisture:float
    temperature:float
    rainfall_forecast:float
