from agri_platform.irrigation.models import IrrigationInput
from agri_platform.irrigation.service import IrrigationService
def test_rec():
    i=IrrigationInput(crop='Rice',soil_moisture=20,temperature=30,rainfall_forecast=0)
    assert IrrigationService().recommendation(i)=='IRRIGATE_NOW'
