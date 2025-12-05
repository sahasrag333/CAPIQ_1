from sqlalchemy import create_engine, text
import os

DB_URL = os.getenv("DB_URL", "postgresql://user:password@localhost:5432/capiq")

engine = create_engine(DB_URL)

def insert_company_metrics(rows):
    insert_sql = text("""
        INSERT INTO company_metrics
        (symbol, date, close_price, volume, headline, sentiment_score, target_risk_label)
        VALUES (:symbol, :date, :close_price, :volume, :headline, :sentiment_score, :target_risk_label)
    """)
    with engine.begin() as conn:
        conn.execute(insert_sql, rows)
