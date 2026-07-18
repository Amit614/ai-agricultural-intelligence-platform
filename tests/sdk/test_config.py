from agri_platform.sdk.config import Settings
def test_settings():
    s=Settings()
    assert s.catalog=='agri'
