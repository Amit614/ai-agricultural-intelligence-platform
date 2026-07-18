from .models import SoilSample
class SoilService:
    def fertility_index(self,s:SoilSample)->float:
        nutrients=(s.nitrogen+s.phosphorus+s.potassium)/3
        return round(nutrients*(s.moisture/100),2)
