"""
Day 35 · Task 1 · Engineering: Serve a scikit-learn model in FastAPI

Train, save with joblib, load once at startup, predict from a POST body.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# pip install joblib
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = "day35/model.joblib"
# Step 1 (run once): train your Titanic pipeline from week 4 and joblib.dump(pipeline, MODEL_PATH)

app = FastAPI(title="Survival predictor")
model = None


@app.on_event("startup")
def load_model():
    global model
    # TODO: model = joblib.load(MODEL_PATH)
    pass


class Passenger(BaseModel):
    Pclass: int
    Sex: str
    Age: float | None = None
    Fare: float


@app.post("/predict")
def predict(p: Passenger):
    # TODO: build a one-row DataFrame from p.model_dump(); return {"survived": bool, "probability": float}
    pass
