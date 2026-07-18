from .models import SchemeEligibility
class SchemeService:
    def eligible(self,e:SchemeEligibility):
        schemes=[]
        if e.land_hectares<=2: schemes.append("PM-KISAN")
        if e.crop.lower()=="rice": schemes.append("Crop Insurance")
        return schemes
