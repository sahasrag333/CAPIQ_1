CREATE TABLE IF NOT EXISTS company_metrics (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    date DATE NOT NULL,
    close_price NUMERIC,
    volume NUMERIC,
    headline TEXT,
    sentiment_score NUMERIC,
    target_risk_label INT
);


