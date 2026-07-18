from datetime import datetime
from agri_platform.iot.models import SensorReading
from agri_platform.iot.service import TelemetryService
def test_health():
    r=SensorReading(sensor_id='1',field_id='F1',timestamp=datetime.now(),temperature=25,moisture=30,battery=90)
    assert TelemetryService().health(r)=='OK'
