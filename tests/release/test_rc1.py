from pathlib import Path

def test_manifest():
    assert Path('release/MANIFEST.yml').name=='MANIFEST.yml'
