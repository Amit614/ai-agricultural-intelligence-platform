from pydantic import BaseModel
from datetime import date
class CommodityPrice(BaseModel):
    commodity:str
    market:str
    price:float
    trade_date:date
