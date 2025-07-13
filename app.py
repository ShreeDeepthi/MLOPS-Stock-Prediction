from flask import Flask, request, jsonify
from app.predictor import load_model, predict_next_close  # adjust if needed

app = Flask(__name__)

@app.route('/predict', methods=['POST'])  # ✅ POST, not GET
def predict():
    try:
        data = request.get_json()
        price = float(data['price'])
        model = load_model()
        prediction = predict_next_close(model, price)
        return jsonify({
            "ticker": "AAPL",
            "latest_close": round(price, 2),
            "predicted_next_close": round(prediction, 2)
        })
    except Exception as e:
        import traceback
        return jsonify({"error": str(e), "trace": traceback.format_exc()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
