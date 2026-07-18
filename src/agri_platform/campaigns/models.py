from pydantic import BaseModel
class Campaign(BaseModel):
    campaign_id:str
    name:str
    channel:str
    segment:str
