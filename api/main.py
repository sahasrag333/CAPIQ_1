from fastapi import FastAPI
from api.schemas import RiskRequest, RiskResponse
from api.service import predict_risk

app = FastAPI(title="Capiq-lite ML API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=RiskResponse)
def predict(req: RiskRequest):
    label, proba = predict_risk(req.close_price, req.volume, req.sentiment_score)
    return RiskResponse(risk_label=label, probability=proba)
