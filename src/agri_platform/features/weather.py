def weather_features(temp:float,humidity:float,rainfall:float)->dict:
    return {
        'temp':temp,
        'humidity':humidity,
        'rainfall':rainfall,
        'heat_index':round(temp+(humidity*0.05),2)
    }
