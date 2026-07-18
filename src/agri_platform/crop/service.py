from .models import CropProfile
class CropRecommendationService:
    def is_temperature_suitable(self, profile:CropProfile, temp:float)->bool:
        return profile.optimal_temp_min <= temp <= profile.optimal_temp_max
