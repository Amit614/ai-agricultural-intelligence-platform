from pydantic import BaseModel
class SoilSample(BaseModel):
    field_id:str
    ph:float
    nitrogen:float
    phosphorus:float
    potassium:float
    moisture:float
