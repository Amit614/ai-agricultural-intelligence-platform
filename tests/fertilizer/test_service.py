from agri_platform.fertilizer.models import NutrientProfile
from agri_platform.fertilizer.service import FertilizerService
def test_gap():
    p=NutrientProfile(crop='Rice',nitrogen=100,phosphorus=50,potassium=30,soil_ph=6.5)
    assert FertilizerService().npk_gap(p)['N']==20
