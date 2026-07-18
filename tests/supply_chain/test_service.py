from agri_platform.supply_chain.models import Shipment
from agri_platform.supply_chain.service import LogisticsService
def test_cost():
 s=Shipment(shipment_id='S1',source='A',destination='B',distance_km=100,quantity_tonnes=10)
 assert LogisticsService().transport_cost(s)==4500.0
