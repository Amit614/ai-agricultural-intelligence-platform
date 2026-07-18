from deploy.healthcheck import healthcheck
def test_health():
    assert healthcheck()["status"]=="healthy"
