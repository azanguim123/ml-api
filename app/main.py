from fastapi import FastAPI

app = FastAPI(
    title="ML API",
    description="Sentiment analysis API serving a pretrained model.",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}