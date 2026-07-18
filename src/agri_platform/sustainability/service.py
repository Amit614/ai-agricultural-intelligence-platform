from .models import SustainabilityInput
class SustainabilityService:
    def carbon_emissions(self,s):
        return round(s.diesel_liters*2.68 + s.fertilizer_kg*1.5,2)
    def sequestration(self,s):
        return round(s.trees_planted*21.0,2)
    def score(self,s):
        return max(0,100-int(self.carbon_emissions(s)/10)+int(self.sequestration(s)/50))
