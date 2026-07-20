# ML API

A REST API built with FastAPI that serves a sentiment analysis model.

This is a hands-on learning project that walks through a full DevOps
deployment workflow, step by step:
**Docker → Kubernetes → Terraform → Cloud (AWS/Azure).**

## Status

🚧 Work in progress. API containerized with Docker  - moving on to docker-compose with PostgreSQL. 

## Tech stack

- **Python 3.13**
- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **Pydantic** — request/response validation
- **scikit-learn** - sentiment cliassification model(TF-IDF + Logistic Regression)
- **Docker** - containerization
- _Coming next:_ Hugging Face Transformers(via Docker), docker-compose, PostgreSQL, Kubernetes, Terraform, AWS/Azure

## Endpoints

|Method|Path      |Description                                 |
|------|----------|--------------------------------------------|
|GET   |`/health` |Health check, returns `{"status": "ok"}`    |
|POST  |`/predict`|Predicts the sentiment of a given text      |
|GET   |`/docs`   |Auto-generated interactive API documentation|

### Example

### Example

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "The patient is suffering from severe migraines."}'
```

Response:

```json
{ "label": "negative", "score": 0.629 }
```
Note: the current model is a lightweight scikit-learn classifier trained
on a proxy dataset (not true sentiment data). Labels/scores illustrate the
API contract; a production-grade model (Hugging Face Transformers) will be
introduced in the Docker image.


## Run locally

Requirements: Python 3.13+, [Colima](https://github.com/abiosoft/colima) (for the Docker step, later).

```bash
# Clone the repo
git clone https://github.com/azanguim123/ml-api.git
cd ml-api

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the API
python -m uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive docs: `http://127.0.0.1:8000/docs`.


## Run with Docker

```bash
docker build -t ml-api:v1 .
docker run -d -p 8000:8000 --name ml-api-container ml-api:v1
```

The API will be available at `http://127.0.0.1:8000`.

## Project structure

```
ml-api/
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI app and endpoints
├── .gitignore
├── README.md
└── requirements.txt
```

## Roadmap

- [x] Step 1 — FastAPI app with `/health` and `/predict`
- [x] Step 2 — Real sentiment model (scikit-learn)
- [x] Step 3 — Dockerize the API
- [ ] Step 4 — `docker-compose` with PostgreSQL
- [ ] Step 5 — Deploy on Kubernetes (kind/minikube + Helm)
- [ ] Step 6 — Infrastructure as Code with Terraform
- [ ] Step 7 — Deploy to AWS (or Azure) with CI/CD