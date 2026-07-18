from .models import NutrientProfile
class FertilizerService:
    def npk_gap(self,p:NutrientProfile):
        return {"N":max(0,120-p.nitrogen),"P":max(0,60-p.phosphorus),"K":max(0,40-p.potassium)}
    def recommendation(self,p:NutrientProfile):
        g=self.npk_gap(p)
        return f"Apply N:{g['N']} P:{g['P']} K:{g['K']} kg/ha"
