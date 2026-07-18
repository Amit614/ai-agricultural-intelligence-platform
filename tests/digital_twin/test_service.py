from agri_platform.digital_twin.models import Farm,Field
from agri_platform.digital_twin.service import FarmTwinService
def test_total_area():
    f=Farm(farm_id='1',name='Demo',location='BLR',fields=[Field(field_id='A',name='A',area_hectares=10)])
    assert FarmTwinService().total_area(f)==10
