# -*- coding: utf-8 -*-
"""
Salary Prediction Web App - Version Compatible
"""

import numpy as np
import pandas as pd
import streamlit as st
from joblib import load
import sklearn

# Set page config
st.set_page_config(page_title="Salary Predictor", layout="wide")

@st.cache_resource
def load_model():
    try:
        # First try with joblib (recommended for scikit-learn)
        model = load('salary_prediction_model.sav')
        st.success("Model loaded successfully with joblib!")
        return model
    except Exception as e:
        st.warning(f"Joblib load failed: {str(e)}. Trying pickle...")
        try:
            import pickle
            # Handle version compatibility for pickle
            if not hasattr(sklearn.compose._column_transformer, '_RemainderColsList'):
                sklearn.compose._column_transformer._RemainderColsList = type(
                    '_RemainderColsList', (), {}
                )
            with open('salary_prediction_model.sav', 'rb') as f:
                model = pickle.load(f)
            st.success("Model loaded successfully with pickle!")
            return model
        except Exception as e2:
            st.error(f"Failed to load model: {str(e2)}")
            return None

# Load model
loaded_model = load_model()

def salary_prediction(input_data):
    if loaded_model is None:
        return "Model not loaded - cannot make predictions"
    
    columns = ['Gender', 'Education Level', 'Job Title', 'Age', 'Years of Experience']
    input_df = pd.DataFrame([input_data], columns=columns)
    
    try:
        prediction = loaded_model.predict(input_df)
        return round(prediction[0], 2)
    except Exception as e:
        return f"Prediction error: {str(e)}"

def main():
    st.title('💰 Salary Prediction App')
    st.markdown("Predict salaries based on employee characteristics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Employee Details")
        gender = st.selectbox('Gender', ['Male', 'Female'], key='gender')
        education = st.selectbox('Education Level', 
                               ['High School', 'Bachelor', 'Master', 'PhD'], 
                               key='education')
        job_title = st.selectbox('Job Title', 
                               ['Software Engineer', 'Data Scientist', 
                                'Manager', 'HR', 'Accountant'],
                               key='job_title')
    
    with col2:
        st.subheader("Experience Details")
        age = st.slider('Age', 18, 65, 30, key='age')
        experience = st.slider('Years of Experience', 0, 40, 5, key='experience')
    
    if st.button('Predict Salary', key='predict'):
        with st.spinner('Calculating...'):
            result = salary_prediction([gender, education, job_title, age, experience])
        
        if isinstance(result, float):
            st.success(f"### Predicted Salary: ${result:,.2f}")
            st.balloons()
        else:
            st.error(result)

if __name__ == '__main__':
    main()
