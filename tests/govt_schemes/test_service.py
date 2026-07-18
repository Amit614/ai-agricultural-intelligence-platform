from agri_platform.govt_schemes.models import SchemeEligibility
from agri_platform.govt_schemes.service import SchemeService
def test_eligible():
 e=SchemeEligibility(farmer_id='F1',land_hectares=1.5,crop='Rice',state='KA')
 assert 'PM-KISAN' in SchemeService().eligible(e)
