from fastapi import FastAPI
from pydantic import BaseModel # BaseModel, la classe de Pydantic qui permet de définir des « formes » de données. 

from app.model import predict_sentiment

app = FastAPI(
    title="ML API",
    description="Sentiment analysis API serving a pretrained model.",
    version="0.1.0",
)


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    label: str
    score: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(**predict_sentiment(request.text))

