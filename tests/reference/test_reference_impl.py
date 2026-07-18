from mlflow.train_and_register import train_and_register
def test_reference():
    assert train_and_register("crop_model")["status"]=="TRAINED_AND_REGISTERED"
