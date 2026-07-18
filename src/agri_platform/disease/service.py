from .models import DiseaseObservation
class DiseaseAssessmentService:
    def risk_level(self,o:DiseaseObservation)->str:
        if o.confidence>=0.9: return "HIGH"
        if o.confidence>=0.7: return "MEDIUM"
        return "LOW"
