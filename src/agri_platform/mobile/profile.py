class FarmerProfileService:
    def get_profile(self, farmer_id):
        return {"farmer_id":farmer_id,"language":"en","notifications":True}
