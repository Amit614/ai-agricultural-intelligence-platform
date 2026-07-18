from .models import Alert
class AlertEngine:
    def evaluate(self,signals:dict):
        alerts=[]
        if signals.get('disease_risk')=='HIGH':
            alerts.append(Alert(category='Disease',severity='HIGH',message='Disease outbreak risk detected'))
        if signals.get('rainfall_mm',0)>75:
            alerts.append(Alert(category='Weather',severity='MEDIUM',message='Heavy rainfall forecast'))
        return alerts
