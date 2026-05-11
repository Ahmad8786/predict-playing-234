import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("data.csv")

encoders = {}

for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

X = data.drop("play", axis=1)
y = data["play"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.joblib")
joblib.dump(encoders, "encoders.joblib")

print("Model trained successfully!")