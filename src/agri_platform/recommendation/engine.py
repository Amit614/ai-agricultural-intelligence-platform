from .models import Recommendation
class RecommendationEngine:
    def generate(self,signals:dict):
        recs=[]
        if signals.get('disease_risk')=='HIGH':
            recs.append(Recommendation(category='Disease',recommendation='Inspect crop immediately',confidence=0.95,reasons=['High disease risk']))
        if signals.get('soil_moisture',100)<25:
            recs.append(Recommendation(category='Irrigation',recommendation='Start irrigation',confidence=0.90,reasons=['Low soil moisture']))
        if signals.get('market_signal')=='SELL':
            recs.append(Recommendation(category='Market',recommendation='Sell harvest',confidence=0.80,reasons=['Favorable market price']))
        return recs
