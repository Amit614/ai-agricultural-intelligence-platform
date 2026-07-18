from pydantic import BaseModel
class Shipment(BaseModel):
    shipment_id:str
    source:str
    destination:str
    distance_km:float
    quantity_tonnes:float
