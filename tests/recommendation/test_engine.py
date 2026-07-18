from agri_platform.recommendation.engine import RecommendationEngine
def test_generate():
    recs=RecommendationEngine().generate({'soil_moisture':20})
    assert len(recs)==1
