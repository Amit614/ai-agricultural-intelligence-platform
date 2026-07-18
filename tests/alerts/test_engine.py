from agri_platform.alerts.engine import AlertEngine
def test_alert():
    assert len(AlertEngine().evaluate({'disease_risk':'HIGH'}))==1
