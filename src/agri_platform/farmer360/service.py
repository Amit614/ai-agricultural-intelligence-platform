from .models import FarmerProfile
class FarmerProfileService:
    def segment(self,p:FarmerProfile)->str:
        if p.land_hectares<2: return 'SMALL'
        if p.land_hectares<10: return 'MEDIUM'
        return 'LARGE'
    def eligible_for_premium(self,p:FarmerProfile)->bool:
        return p.land_hectares>=5
