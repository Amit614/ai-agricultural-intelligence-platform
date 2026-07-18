from pydantic import BaseModel
class ImagePrediction(BaseModel):
    image_id:str
    label:str
    confidence:float
