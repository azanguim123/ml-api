from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ML API",
    description="Sentiment analysis API serving a pretrained model.",
    version="0.1.0",
)


# --- Request and response schemas ---

class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    label: str
    score: float


# --- Fake model (placeholder, replaced in the next step) ---

def predict_sentiment(text: str) -> PredictResponse:
    return PredictResponse(label="positive", score=0.99)


# --- Endpoints ---

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    return predict_sentiment(request.text)
