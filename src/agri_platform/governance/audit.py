from datetime import datetime
class AuditLogger:
    def log(self,user,action,resource):
        return {"timestamp":datetime.utcnow().isoformat(),"user":user,"action":action,"resource":resource}
