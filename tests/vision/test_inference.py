from agri_platform.vision.inference import VisionInference
def test_predict():
    assert VisionInference().predict('img1').label=='healthy'
