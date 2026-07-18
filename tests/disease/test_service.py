from agri_platform.disease.models import DiseaseObservation
from agri_platform.disease.service import DiseaseAssessmentService
def test_risk():
    obs=DiseaseObservation(crop='rice',symptom='leaf lesions',confidence=0.95)
    assert DiseaseAssessmentService().risk_level(obs)=='HIGH'
