from pydantic import BaseModel
from datetime import datetime
class WeatherObservation(BaseModel):
    station_id:str
    timestamp:datetime
    temperature:float
    humidity:float
    rainfall_mm:float=0
