from sklearn.linear_model import LinearRegression
import joblib
from fetcher import fetch_stock_data

def train_model():
    df = fetch_stock_data()
    if df.empty:
        raise ValueError("DataFrame is empty")
    df["Close_t-1"] = df["Close"].shift(1)
    df = df.dropna()
    X = df[["Close_t-1"]]
    y = df["Close"]

    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "model.pkl")

if __name__ == "__main__":
    train_model()
