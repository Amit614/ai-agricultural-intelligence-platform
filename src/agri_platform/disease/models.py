from pydantic import BaseModel
class DiseaseObservation(BaseModel):
    crop:str
    symptom:str
    confidence:float
    image_uri:str|None=None
