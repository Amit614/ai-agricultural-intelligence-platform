from agri_platform.pest.models import PestObservation
from agri_platform.pest.service import PestRiskService
def test_risk():
    o=PestObservation(crop='Rice',pest='BPH',severity=5,humidity=80)
    assert PestRiskService().risk(o)=='HIGH'
