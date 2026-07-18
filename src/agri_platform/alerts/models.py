from pydantic import BaseModel
class Alert(BaseModel):
    category:str
    severity:str
    message:str
    channel:str='SMS'
