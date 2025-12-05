import requests
from datetime import datetime
import json
from pathlib import Path

def fetch_company_data(symbol: str):
    # Example placeholder – later change to real API/scrape logic
    # For start, just mock some data
    return {
        "symbol": symbol,
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "close_price": 100.5,
        "volume": 123456,
        "headline": f"Sample news headline for {symbol}",
        "sentiment_score": 0.2
    }

def main():
    symbols = ["AAPL", "MSFT", "GOOGL"]
    data = [fetch_company_data(s) for s in symbols]

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / f"raw_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

    with out_file.open("w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved raw data to {out_file}")

if __name__ == "__main__":
    main()
