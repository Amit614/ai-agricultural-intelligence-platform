from pydantic import BaseModel
from typing import List

class Sensor(BaseModel):
    sensor_id:str
    sensor_type:str
    status:str="ACTIVE"

class Field(BaseModel):
    field_id:str
    name:str
    area_hectares:float
    sensors:List[Sensor]=[]

class Farm(BaseModel):
    farm_id:str
    name:str
    location:str
    fields:List[Field]=[]
