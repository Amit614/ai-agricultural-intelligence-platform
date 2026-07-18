from agri_platform.satellite.service import VegetationIndexService
def test_ndvi():
    assert VegetationIndexService.ndvi(0.8,0.2)==0.6
