import pandas as pd
from sqlalchemy import create_engine
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

DB_URL = os.getenv("DB_URL", "postgresql://user:password@localhost:5432/capiq")

def load_data():
    engine = create_engine(DB_URL)
    df = pd.read_sql("SELECT * FROM company_metrics", engine)
    return df

def main():
    df = load_data()

    # Simple features
    X = df[["close_price", "volume", "sentiment_score"]]
    y = df["target_risk_label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Train score:", model.score(X_train, y_train))
    print("Test score:", model.score(X_test, y_test))

    # Save pickle
    joblib.dump(model, "ml/models/model.pkl")
    print("Saved model to ml/models/model.pkl")

if __name__ == "__main__":
    main()
