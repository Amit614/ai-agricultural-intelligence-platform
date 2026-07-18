from datetime import date
from agri_platform.market.models import CommodityPrice
from agri_platform.market.service import MarketService

def test_rec():
 p=CommodityPrice(commodity='Rice',market='BLR',price=6000,trade_date=date.today())
 assert MarketService().recommendation(p)=='SELL'
