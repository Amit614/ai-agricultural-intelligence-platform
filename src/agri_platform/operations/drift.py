class DriftMonitor:
    def check(self,baseline,current,threshold=0.1):
        return abs(current-baseline)>threshold
