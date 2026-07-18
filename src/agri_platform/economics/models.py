from pydantic import BaseModel
class FarmEconomics(BaseModel):
    crop:str
    area_hectares:float
    production_cost:float
    expected_yield_tonnes:float
    expected_price_per_tonne:float
