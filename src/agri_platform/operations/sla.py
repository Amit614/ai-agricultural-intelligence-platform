class SLATracker:
    def evaluate(self,actual,target):
        return {"met":actual<=target,"actual":actual,"target":target}
