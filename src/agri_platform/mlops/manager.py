class ModelLifecycleManager:
    def register_model(self,name,version):
        return {"name":name,"version":version,"status":"REGISTERED"}
    def promote(self,name,stage="Champion"):
        return {"name":name,"stage":stage}
