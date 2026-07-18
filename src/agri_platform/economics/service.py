from .models import FarmEconomics
class EconomicsService:
    def revenue(self,e): return round(e.expected_yield_tonnes*e.expected_price_per_tonne,2)
    def profit(self,e): return round(self.revenue(e)-e.production_cost,2)
    def roi(self,e):
        return round((self.profit(e)/e.production_cost)*100,2) if e.production_cost else 0
