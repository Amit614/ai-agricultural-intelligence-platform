from agri_platform.vector.index import VectorIndex
from agri_platform.mosaic_ai.rag import RAGService
def test_retrieve():
    idx=VectorIndex()
    idx.add('rice requires warm weather')
    assert len(RAGService(idx).retrieve('rice'))==1
