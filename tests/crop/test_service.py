from agri_platform.crop.models import CropProfile
from agri_platform.crop.service import CropRecommendationService
def test_temperature():
    p=CropProfile(crop_name='rice',growth_stage='vegetative',optimal_temp_min=20,optimal_temp_max=35,water_requirement_mm=120)
    assert CropRecommendationService().is_temperature_suitable(p,28)
