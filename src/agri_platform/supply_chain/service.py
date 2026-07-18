from .models import Shipment
class LogisticsService:
    def transport_cost(self,s:Shipment,cost_per_km=45.0):
        return round(s.distance_km*cost_per_km,2)
    def utilization(self,s:Shipment,capacity=20.0):
        return round((s.quantity_tonnes/capacity)*100,2)
