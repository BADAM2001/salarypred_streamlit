import numpy as np
import pandas as pd
import streamlit as st
from joblib import load
import sklearn

# Handle version compatibility
try:
    loaded_model = load('salary_prediction_model.sav')
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.info("Trying pickle with compatibility fix...")
    try:
        import sklearn.compose
        if not hasattr(sklearn.compose._column_transformer, '_RemainderColsList'):
            sklearn.compose._column_transformer._RemainderColsList = type(
                '_RemainderColsList', (), {}
            )
        import pickle
        loaded_model = pickle.load(open('salary_prediction_model.sav', 'rb'))
    except Exception as e2:
        st.error(f"Failed to load model: {str(e2)}")
        loaded_model = None

def salary_prediction(input_data):
    if loaded_model is None:
        return "Model not loaded - cannot make predictions"
    
    columns = ['Gender', 'Education Level', 'Job Title', 'Age', 'Years of Experience']
    input_df = pd.DataFrame([input_data], columns=columns)
    
    try:
        prediction = loaded_model.predict(input_df)
        return f'Predicted Salary: ${round(prediction[0], 2)}'
    except Exception as e:
        return f"Prediction error: {str(e)}"

def main():
    st.title('Salary Prediction Web App')
    st.write("Enter the following details to predict salary:")

    gender = st.selectbox('Gender', ['Male', 'Female'])
    education = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
    job_title = st.selectbox('Job Title', ['Software Engineer', 'Data Scientist', 'Manager', 'HR', 'Accountant'])
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
    experience = st.number_input('Years of Experience', min_value=0, max_value=50, step=1)

    if st.button('Predict Salary'):
        result = salary_prediction([gender, education, job_title, age, experience])
        st.success(result)

if __name__ == '__main__':
    main()
