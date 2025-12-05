import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "ml" / "models" / "model.pkl"
model = joblib.load(MODEL_PATH)

def predict_risk(close_price: float, volume: float, sentiment_score: float):
    X = np.array([[close_price, volume, sentiment_score]])
    proba = model.predict_proba(X)[0][1]
    label = int(proba > 0.5)
    return label, float(proba)
