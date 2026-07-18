class YieldBaselineModel:
    def predict(self,features:dict)->float:
        return round(2.0 + features['rainfall']*0.01 + features['humidity']*0.005,2)
