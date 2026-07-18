from agri_platform.weather.service import WeatherService
from agri_platform.weather.models import WeatherObservation
from datetime import datetime
def test_validate():
    s=WeatherService()
    assert s.validate(WeatherObservation(station_id='A',timestamp=datetime.now(),temperature=25,humidity=60))
