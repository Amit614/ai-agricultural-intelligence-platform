from .models import Farm
class FarmTwinService:
    def total_area(self,farm:Farm)->float:
        return round(sum(f.area_hectares for f in farm.fields),2)
