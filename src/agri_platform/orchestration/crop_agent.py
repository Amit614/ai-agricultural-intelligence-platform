class CropAgent:
    def advise(self,c):
        if c.get('crop_stage')=='FLOWERING':
            return [{'priority':1,'category':'Crop','message':'Increase field monitoring during flowering'}]
        return []
