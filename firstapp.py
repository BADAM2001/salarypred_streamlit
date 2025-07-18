# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 12:30:39 2025

@author: manid
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open('D:/machinelearning files/salary_prediction_model.sav', 'rb'))

# Prediction function
def salary_prediction(input_data):
    # Column order as used during training
    columns = ['Gender', 'Education Level', 'Job Title', 'Age', 'Years of Experience']
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data], columns=columns)

    # Predict
    prediction = loaded_model.predict(input_df)

    return f'Predicted Salary: ${round(prediction[0], 2)} '

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

    
    
    
    
    
    
