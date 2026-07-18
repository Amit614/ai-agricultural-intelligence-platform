from pydantic import BaseModel
class SustainabilityInput(BaseModel):
    diesel_liters:float
    fertilizer_kg:float
    trees_planted:int
