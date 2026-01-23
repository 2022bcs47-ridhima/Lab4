from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("trained_model.pkl")

# 👇 Define input schema
class WineFeatures(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: WineFeatures):
    X = np.array(data.features).reshape(1, -1)
    prediction = model.predict(X)
    return {
        "predicted_wine_quality": float(prediction[0])
    }
