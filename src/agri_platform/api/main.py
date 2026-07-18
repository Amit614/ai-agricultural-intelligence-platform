from fastapi import FastAPI
app = FastAPI(title="AI Agricultural Intelligence API")

@app.get("/health")
def health():
    return {"status":"ok"}
