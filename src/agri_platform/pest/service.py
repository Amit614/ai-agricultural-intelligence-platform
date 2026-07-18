from .models import PestObservation
class PestRiskService:
    def risk(self,o:PestObservation)->str:
        score=o.severity + (2 if o.humidity>75 else 0)
        return 'HIGH' if score>=6 else 'MEDIUM' if score>=3 else 'LOW'
    def recommendation(self,risk:str)->str:
        return {'HIGH':'Immediate treatment','MEDIUM':'Monitor and inspect','LOW':'Routine monitoring'}[risk]
