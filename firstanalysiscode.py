# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 12:16:51 2025

@author: manid
"""



# loading the saved model
import pandas as pd
import pickle

# Load the saved model
loaded_model = pickle.load(open('D:/machinelearning files/salary_prediction_model.sav', 'rb'))

# Example input data
# Format: (Gender, Education Level, Job Title, Age, Years of Experience)
input_data = ('Male', 'Bachelor', 'Software Engineer', 28, 4)

# Define column names in the same order as training data
columns = ['Gender', 'Education Level', 'Job Title', 'Age', 'Years of Experience']

# Convert to DataFrame
input_df = pd.DataFrame([input_data], columns=columns)

# Predict salary
predicted_salary = loaded_model.predict(input_df)

# Output
print("Predicted Salary:", round(predicted_salary[0], 2))
