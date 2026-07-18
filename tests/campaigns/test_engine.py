from agri_platform.campaigns.engine import CampaignEngine
from agri_platform.campaigns.models import Campaign
def test_schedule():
    c=Campaign(campaign_id='C1',name='Advice',channel='SMS',segment='STANDARD')
    assert CampaignEngine().schedule(c)['status']=='SCHEDULED'
