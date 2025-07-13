import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker="AAPL", period="30d", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval, progress=False, auto_adjust=True)

    if df.empty:
        raise ValueError("❌ No data fetched. Check the ticker or internet connection.")

    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Save data to CSV
    df.to_csv("data/stock_data.csv")

    return df

