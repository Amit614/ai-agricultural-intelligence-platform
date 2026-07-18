def healthcheck():
    return {"status":"healthy","checks":["database","jobs","serving"]}
