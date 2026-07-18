from agri_platform.knowledge.registry import KnowledgeRegistry
from agri_platform.knowledge.models import KnowledgeRecord
def test_registry():
    r=KnowledgeRegistry()
    rec=KnowledgeRecord(category='crop',key='rice',title='Rice',content='x')
    r.register(rec)
    assert r.get('crop','rice').title=='Rice'
