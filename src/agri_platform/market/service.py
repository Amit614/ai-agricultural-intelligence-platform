from .models import CommodityPrice
class MarketService:
    def recommendation(self,p:CommodityPrice)->str:
        return 'SELL' if p.price>5000 else 'HOLD'
