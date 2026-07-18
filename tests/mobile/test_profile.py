from agri_platform.mobile.profile import FarmerProfileService

def test_profile():
 assert FarmerProfileService().get_profile('F1')['farmer_id']=='F1'
