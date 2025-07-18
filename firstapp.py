# -*- coding: utf-8 -*-
"""
Salary Prediction Web App
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st
import os

# Load the saved model with error handling
try:
    if not os.path.exists('salary_prediction_model.sav'):
        st.error("Model file not found! Please ensure salary_prediction_model.sav is in the correct directory.")
    else:
        loaded_model = pickle.load(open('salary_prediction_model.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    loaded_model = None

# Prediction function
def salary_prediction(input_data):
    if loaded_model is None:
        return "Model not loaded - cannot make predictions"
    
    # Column order as used during training
    columns = ['Gender', 'Education Level', 'Job Title', 'Age', 'Years of Experience']
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data], columns=columns)

    # Predict
    try:
        prediction = loaded_model.predict(input_df)
        return f'Predicted Salary: ${round(prediction[0], 2)}'
    except Exception as e:
        return f"Prediction error: {str(e)}"

# Streamlit App
def main():
    st.title('Salary Prediction Web App')
    st.write("Enter the following details to predict salary:")

    # Input fields
    gender = st.selectbox('Gender', ['Male', 'Female'])
    education = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
    job_title = st.selectbox('Job Title', ['Software Engineer', 'Data Scientist', 'Manager', 'HR', 'Accountant'])
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
    experience = st.number_input('Years of Experience', min_value=0, max_value=50, step=1)

    diagnosis = ''
    
    if st.button('Predict Salary'):
        diagnosis = salary_prediction([gender, education, job_title, age, experience])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()
