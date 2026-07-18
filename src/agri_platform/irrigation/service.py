from .models import IrrigationInput
class IrrigationService:
    def evapotranspiration(self,i:IrrigationInput)->float:
        return round(max(0.0,0.12*i.temperature-0.03*i.rainfall_forecast),2)
    def recommendation(self,i:IrrigationInput)->str:
        if i.soil_moisture<25 and i.rainfall_forecast<5: return 'IRRIGATE_NOW'
        if i.rainfall_forecast>=5: return 'DEFER_IRRIGATION'
        return 'MONITOR'
