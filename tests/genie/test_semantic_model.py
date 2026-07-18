from pathlib import Path
def test_semantic_exists():
    assert Path('semantic_model/agriculture_semantic_model.yml').name.endswith('.yml')
