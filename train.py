"""
Train a simple sentiment classifier and save it to disk.

Run once with:  python train.py
The trained model will be written to model.joblib.
"""

import joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def build_pipeline() -> Pipeline:
    """TF-IDF features → Logistic Regression classifier."""
    return Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
        ("clf", LogisticRegression(max_iter=1000)),
    ])


def main() -> None:
    # Use two opposing newsgroups as a stand-in for positive/negative.
    # "rec.autos" → positive, "sci.med" → negative (purely arbitrary).
    categories = ["rec.autos", "sci.med"]
    data = fetch_20newsgroups(
        subset="train",
        categories=categories,
        remove=("headers", "footers", "quotes"),
    )

    pipeline = build_pipeline()
    pipeline.fit(data.data, data.target)

    accuracy = pipeline.score(data.data, data.target)
    print(f"Training accuracy: {accuracy:.3f}")

    joblib.dump({"pipeline": pipeline, "labels": categories}, "model.joblib")
    print("Saved model to model.joblib")


if __name__ == "__main__":
    main()
