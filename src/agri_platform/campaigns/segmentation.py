class FarmerSegmentation:
    def segment(self,profile):
        return "HIGH_VALUE" if profile.get("land_size",0)>=5 else "STANDARD"
