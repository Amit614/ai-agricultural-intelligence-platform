from pydantic import BaseModel
class PestObservation(BaseModel):
    crop:str
    pest:str
    severity:int
    humidity:float
