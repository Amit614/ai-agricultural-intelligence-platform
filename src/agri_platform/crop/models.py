from pydantic import BaseModel
class CropProfile(BaseModel):
    crop_name:str
    growth_stage:str
    optimal_temp_min:float
    optimal_temp_max:float
    water_requirement_mm:float
