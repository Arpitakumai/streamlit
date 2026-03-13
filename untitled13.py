import streamlit as st
import pickle
import pandas as pd

# Load model safely
with open("tips_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Tip Prediction App")

total_bill = st.number_input("Total Bill", min_value=0.0)
size = st.number_input("Size", min_value=1, step=1)

sex = st.selectbox("Sex", ["Male","Female"])
smoker = st.selectbox("Smoker", ["Yes","No"])
day = st.selectbox("Day", ["Thur","Fri","Sat","Sun"])
time = st.selectbox("Time", ["Lunch","Dinner"])

# Create dataframe for prediction
input_data = pd.DataFrame({
    "total_bill":[total_bill],
    "size":[size],
    "sex":[sex],
    "smoker":[smoker],
    "day":[day],
    "time":[time]
})

# Prediction
if st.button("Predict Tip"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Tip: {prediction[0]:.2f}")
