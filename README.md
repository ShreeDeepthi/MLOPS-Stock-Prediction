# MLOPS Stock Price Prediction

This project demonstrates a machine learning workflow for predicting the next day's closing price of a stock (default: AAPL) using historical data. It includes model training, prediction via a Flask API, Docker containerization, and optional CI/CD with GitHub Actions.

## Features

- Data fetching from Yahoo Finance via `yfinance`
- Linear Regression model using `scikit-learn`
- Flask REST API to serve predictions
- Dockerfile for containerized deployment
- GitHub repository for version control
- Easily extendable for MLOps pipelines

## Project Structure

```
MLOPS-Stock-Prediction/
│
├── app/                        # Core application code
│   ├── fetcher.py              # Fetches stock data
│   ├── model.py                # Trains model and saves it
│   ├── predictor.py            # Loads model and performs prediction
│   └── __init__.py             # (Optional) Package initializer
│
├── data/                       # Stores downloaded stock CSVs
│   └── stock_data.csv
│
├── docker/                     # Docker setup
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── main.yml            # GitHub Actions CI/CD (optional)
│
├── app.py                      # Flask API for predictions
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ShreeDeepthi/MLOPS-Stock-Prediction.git
cd MLOPS-Stock-Prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python app/model.py
```

### 5. Run the Flask App

```bash
python app.py
```

### 6. Make a Prediction

Send a POST request using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"price\": 201.08}"
```

## Docker Usage

### 1. Build Docker Image

```bash
docker build -t stock-predictor .
```

### 2. Run Container

```bash
docker run -p 5000:5000 stock-predictor
```

## API Endpoint

### POST `/predict`

**Request Body:**
```json
{
  "price": 201.08
}
```

**Response:**
```json
{
  "ticker": "AAPL",
  "latest_close": 201.08,
  "predicted_next_close": 200.88
}
```

## Author

Developed by Shree Deepthi
