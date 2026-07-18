from agri_platform.sustainability.models import SustainabilityInput
from agri_platform.sustainability.service import SustainabilityService
def test_emissions():
 s=SustainabilityInput(diesel_liters=10,fertilizer_kg=20,trees_planted=5)
 assert SustainabilityService().carbon_emissions(s)>0
