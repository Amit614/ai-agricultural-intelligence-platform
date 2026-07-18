from agri_platform.farmer360.models import FarmerProfile
from agri_platform.farmer360.service import FarmerProfileService
def test_segment():
 p=FarmerProfile(farmer_id='F1',name='A',village='X',land_hectares=1.5,preferred_language='en')
 assert FarmerProfileService().segment(p)=='SMALL'
