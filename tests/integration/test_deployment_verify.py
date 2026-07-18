from scripts.verify_deployment import verify
def test_verify():
    assert verify()["bundle"]
