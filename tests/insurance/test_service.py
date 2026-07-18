from agri_platform.insurance.models import InsuranceProfile
from agri_platform.insurance.service import InsuranceService
def test_premium():
 p=InsuranceProfile(farmer_id='F1',crop='Rice',area_hectares=2,weather_risk=0.5,insured_amount=100000)
 assert InsuranceService().premium(p)>0
