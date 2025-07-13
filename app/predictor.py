import os
import joblib
import numpy as np

def load_model():
    # Get the absolute path to model.pkl inside the app directory
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    return joblib.load(model_path)

def predict_next_close(model, latest_close):
    # Ensure latest_close is reshaped as a 2D array
    input_data = np.array(latest_close).reshape(1, -1)
    return float(model.predict(input_data)[0])

