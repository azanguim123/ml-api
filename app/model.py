from functools import lru_cache
from pathlib import Path

import joblib


MODEL_PATH = Path(__file__).resolve().parent.parent / "model.joblib"
LABEL_MAP = {0: "positive", 1: "negative"}


@lru_cache(maxsize=1)
def get_model():
    """Load the trained model once and cache it in memory."""
    if not MODEL_PATH.exists():
        raise RuntimeError(
            f"Model file not found at {MODEL_PATH}. "
            "Run `python train.py` first."
        )
    return joblib.load(MODEL_PATH)


def predict_sentiment(text: str) -> dict:
    """Run the model on `text` and return a normalized dict."""
    bundle = get_model()
    pipeline = bundle["pipeline"]

    prediction = pipeline.predict([text])[0]
    probabilities = pipeline.predict_proba([text])[0]
    confidence = float(probabilities[prediction])

    return {
        "label": LABEL_MAP[int(prediction)],
        "score": confidence,
    }
