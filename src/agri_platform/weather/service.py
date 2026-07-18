from .models import WeatherObservation
class WeatherService:
    def validate(self,obs:WeatherObservation)->bool:
        return -80<=obs.temperature<=70 and 0<=obs.humidity<=100
