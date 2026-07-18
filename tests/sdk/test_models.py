from agri_platform.sdk.models import Dataset
def test_dataset():
    d=Dataset(name='weather',source='api')
    assert d.enabled
