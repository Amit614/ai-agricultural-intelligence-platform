class KPIService:
    def summarize(self,metrics):
        return {
            "yield": metrics.get("yield",0),
            "profit": metrics.get("profit",0),
            "sustainability": metrics.get("sustainability",0),
            "risk": metrics.get("risk","LOW")
        }
