# Salary Prediction Web App
[deployment link](https://salarypredapp-rz5ccuqks5spbgdwjbxjqq.streamlit.app/#salary-prediction-app)

![App Screenshot](https://github.com/BADAM2001/salarypred_streamlit/blob/fc7dc65b8e56e17c6f2d7f9654eef35738055b23/Screenshot%20(255).png)

![App working](https://github.com/BADAM2001/salarypred_streamlit/blob/fc7dc65b8e56e17c6f2d7f9654eef35738055b23/Screenshot%20(255).png)

## 📌 Overview
A Streamlit web application that predicts employee salaries based on characteristics like education level, job title, experience, etc. The app uses a pre-trained machine learning model (scikit-learn) to make predictions.

## ✨ Features
- User-friendly interface with interactive input controls
- Handles version compatibility issues with scikit-learn models
- Displays formatted salary predictions with visual feedback
- Responsive layout that works on different screen sizes
- Robust error handling and user feedback

## 🛠️ Technical Stack
- **Framework**: Streamlit (v1.2.0)
- **Machine Learning**: scikit-learn (v1.0.1)
- **Data Processing**: pandas (v1.3.4), numpy (v1.21.4)
- **Model Serialization**: joblib (v1.1.0) and pickle

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### 1. Clone the repository
git clone https://github.com/yourusername/salary-prediction-app.git
cd salary-prediction-app

### 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
streamlit run app.py
📂 Project Structure
text
salary-prediction-app/
├── app.py                # Main application code
├── salary_prediction_model.sav  # Pre-trained ML model
├── requirements.txt      # Dependency specifications
└── README.md            # This documentation
🧠 Model Details
Algorithm: [Specify if known -  Linear Regression]
Features Used:
Gender (Male/Female)
Education Level (High School, Bachelor, Master, PhD)
Job Title (Software Engineer, Data Scientist, etc.)
Age
Years of Experience

Performance: [Add metrics if available - e.g., R² score:0.87]

🌐 Deployment
The app can be deployed on:
Streamlit Community Cloud
Example deployment to Streamlit Cloud:
Push your code to GitHub
Go to Streamlit Community Cloud
Connect your GitHub repository
Set main file path to app.py
Deploy!

🐛 Troubleshooting
If you encounter the _RemainderColsList error:
Ensure you're using scikit-learn v1.0.1
Try clearing cache with streamlit cache clear
Verify the model file exists in the project root
