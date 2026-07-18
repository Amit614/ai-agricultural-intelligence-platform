def evaluate(metrics:dict,threshold:float=0.9):
    score=metrics.get("accuracy",0)
    return {"accuracy":score,"passed":score>=threshold}
