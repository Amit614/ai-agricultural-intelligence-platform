from pydantic import BaseModel
from datetime import datetime
class SensorReading(BaseModel):
    sensor_id:str
    field_id:str
    timestamp:datetime
    temperature:float
    moisture:float
    battery:float
