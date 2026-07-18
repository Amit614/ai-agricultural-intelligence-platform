from .models import InsuranceProfile
class InsuranceService:
    def premium(self,p:InsuranceProfile)->float:
        return round(p.insured_amount*(0.02+p.weather_risk*0.01),2)
    def risk_band(self,p:InsuranceProfile)->str:
        return 'HIGH' if p.weather_risk>=0.7 else 'MEDIUM' if p.weather_risk>=0.4 else 'LOW'
