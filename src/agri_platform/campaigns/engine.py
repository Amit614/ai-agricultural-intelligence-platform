from .models import Campaign
class CampaignEngine:
    def schedule(self,campaign:Campaign):
        return {"campaign_id":campaign.campaign_id,"status":"SCHEDULED"}
