from agri_platform.soil.models import SoilSample
from agri_platform.soil.service import SoilService
def test_fertility():
    s=SoilSample(field_id='F1',ph=6.8,nitrogen=80,phosphorus=60,potassium=70,moisture=50)
    assert SoilService().fertility_index(s)>0
