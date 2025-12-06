import json
import boto3
from datetime import datetime

s3 = boto3.client("s3")
BUCKET = "sahasra_bucket"   # move to env in real setup

def fetch_company_data(symbol: str):
    # TODO: real scraping/API call
    return {
        "symbol": symbol,
        "date": datetime.fromtimestamp().strftime("%Y-%m-%d"),
        "close_price": 100.5,
        "volume": 123456,
        "headline": f"Sample news headline for {symbol}",
        "sentiment_score": 0.5
    }

def lambda_handler(event, context):
    symbols = ["AAPL", "MSFT", "GOOGL"]
    data = [fetch_company_data(s) for s in symbols]

    key = f"raw/raw_{datetime.fromtimestamp().strftime('%Y%m%d_%H%M%S')}.json"
    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(data)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Scrape success", "s3_key": key})
    }
