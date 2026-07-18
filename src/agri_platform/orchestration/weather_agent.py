class WeatherAgent:
    def advise(self,c):
        if c.get('rainfall_forecast',0)>20:
            return [{'priority':2,'category':'Weather','message':'Delay irrigation due to expected rainfall'}]
        return []
