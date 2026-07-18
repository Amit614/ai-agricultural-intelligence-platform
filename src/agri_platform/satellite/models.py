from pydantic import BaseModel

class SatelliteScene(BaseModel):
    scene_id:str
    provider:str
    acquisition_date:str
    cloud_cover:float
