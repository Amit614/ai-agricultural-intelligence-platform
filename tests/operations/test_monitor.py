from agri_platform.operations.monitor import OperationsMonitor

def test_health():
 assert OperationsMonitor().health()['status']=='GREEN'
