class DataQualityChecker:
    def check_nulls(self,records,key):
        return sum(1 for r in records if r.get(key) is None)
