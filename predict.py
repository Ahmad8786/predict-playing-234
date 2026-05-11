import joblib
import pandas as pd

model = joblib.load("model.joblib")
encoders = joblib.load("encoders.joblib")

def predict(data_dict):
    df = pd.DataFrame([data_dict])

    for col in df.columns:
        df[col] = encoders[col].transform(df[col])

    prediction = model.predict(df)[0]
    prob = model.predict_proba(df).max()

    result = encoders["play"].inverse_transform([prediction])[0]

    return result, prob