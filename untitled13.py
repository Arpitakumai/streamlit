import streamlit as st
import joblib
import pandas as pd

model = joblib.load("tips_model.pkl")

st.title("Tip Prediction App")

total_bill = st.number_input("Total Bill")
size = st.number_input("Size")

sex = st.selectbox("Sex", ["male","female"])
smoker = st.selectbox("Smoker", ["yes","no"])
day = st.selectbox("Day", ["thur","fri","sat","sun"])
time = st.selectbox("Time", ["lunch","dinner"])

input_data = pd.DataFrame({
    "total_bill":[total_bill],
    "size":[size],
    "sex":[sex],
    "smoker":[smoker],
    "day":[day],
    "time":[time]
})

if st.button("Predict Tip"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Tip: {prediction[0]:.2f}")
