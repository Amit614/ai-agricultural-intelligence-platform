from agri_platform.analytics.kpi import KPIService

def test_summary():
 assert KPIService().summarize({'yield':10})['yield']==10
