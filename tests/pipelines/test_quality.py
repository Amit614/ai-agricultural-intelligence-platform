def validate_temperature(v): return -80<=v<=70
def test_validate(): assert validate_temperature(25)
