from agri_platform.economics.models import FarmEconomics
from agri_platform.economics.service import EconomicsService
def test_profit():
 e=FarmEconomics(crop='Rice',area_hectares=2,production_cost=10000,expected_yield_tonnes=5,expected_price_per_tonne=3000)
 assert EconomicsService().profit(e)==5000
