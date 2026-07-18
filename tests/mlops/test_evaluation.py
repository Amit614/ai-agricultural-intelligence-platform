from agri_platform.mlops.evaluation import evaluate

def test_eval():
    assert evaluate({'accuracy':0.95})['passed']
