from datetime import datetime
from etl.s3_utils import read_json_from_s3
from etl.db_utils import insert_company_metrics

BUCKET = "sahasra"


def build_rows(raw_data):
    rows = []
    for item in raw_data:
        rows.append({
            "symbol": item["symbol"],
            "date": item["date"],
            "close_price": item["close_price"],
            "volume": item["volume"],
            "headline": item["headline"],
            "sentiment_score": item["sentiment_score"],
            # Simple fake label: > 0.1 sentiment = high risk
            "target_risk_label": 1 if item["sentiment_score"] > 0.1 else 0
        })
    return rows

def run(bucket, key):
    raw_data = read_json_from_s3(bucket, key)
    rows = build_rows(raw_data)
    insert_company_metrics(rows)
    print(f"Inserted {len(rows)} rows into Postgres")

if __name__ == "__main__":
    # For local testing, hardcode a key
    test_key = "raw/raw_20250101_120000.json"
    run(BUCKET, test_key)
