from pydantic import BaseModel

class RiskRequest(BaseModel):
    close_price: float
    volume: float
    sentiment_score: float

class RiskResponse(BaseModel):
    risk_label: int
    probability: float
