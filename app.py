import streamlit as st
from predict import predict

st.set_page_config(page_title="PlayWise AI", layout="centered")

st.title("🏏 PlayWise AI - Match Predictor")

sport = st.selectbox("Select Sport", ["cricket", "hockey"])
weather = st.selectbox("Weather", ["sunny", "rainy", "cloudy"])
wind = st.selectbox("Wind", ["low", "strong"])
humidity = st.selectbox("Humidity", ["low", "high"])
rain = st.selectbox("Rain Chances", ["no", "yes"])
sky = st.selectbox("Sky Condition", ["clear", "cloudy"])
time = st.selectbox("Time", ["afternoon", "evening"])
temperature = st.selectbox("Temperature", ["hot", "mild", "cold"])
ground = st.selectbox("Ground Condition", ["dry", "wet"])

if st.button("Predict"):
    data = {
        "sport": sport,
        "weather": weather,
        "wind": wind,
        "humidity": humidity,
        "rain": rain,
        "sky": sky,
        "time": time,
        "temperature": temperature,
        "ground": ground
    }

    result, prob = predict(data)

    if result == "yes":
        st.success(f"✅ Match should be played! ({prob*100:.2f}%)")
    else:
        st.error(f"❌ Match should NOT be played! ({prob*100:.2f}%)")