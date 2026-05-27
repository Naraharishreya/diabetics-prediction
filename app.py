
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("Diabetes Prediction App")

age = st.number_input("Age")
sex = st.number_input("Sex")
bmi = st.number_input("BMI")
bp = st.number_input("Blood Pressure")
s1 = st.number_input("S1")
s2 = st.number_input("S2")
s3 = st.number_input("S3")
s4 = st.number_input("S4")
s5 = st.number_input("S5")
s6 = st.number_input("S6")

if st.button("Predict"):
    features = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    prediction = model.predict(features)

    st.success(f"Prediction: {prediction[0]:.2f}")
