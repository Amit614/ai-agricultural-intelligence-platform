from agri_platform.governance.data_quality import DataQualityChecker

def test_nulls():
 assert DataQualityChecker().check_nulls([{'a':1},{'a':None}],'a')==1
