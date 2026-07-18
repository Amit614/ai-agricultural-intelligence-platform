from agri_platform.vector.index import VectorIndex
def test_search():
    v=VectorIndex()
    v.add('Rice grows in warm weather')
    assert len(v.search('rice'))==1
