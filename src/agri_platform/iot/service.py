from .models import SensorReading
class TelemetryService:
    def health(self,r:SensorReading)->str:
        if r.battery<20: return 'LOW_BATTERY'
        if r.moisture<10: return 'DRY'
        return 'OK'
