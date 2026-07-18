from agri_platform.agents.advisor import FarmAdvisorAgent
from agri_platform.knowledge.registry import KnowledgeRegistry
from agri_platform.knowledge.models import KnowledgeRecord
def test_agent():
    reg=KnowledgeRegistry()
    reg.register(KnowledgeRecord(category='crop',key='rice',title='Rice',content='Grow in warm conditions'))
    assert 'warm' in FarmAdvisorAgent(reg).run('Tell me about rice')
