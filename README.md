# Predictive Analysis of Various Diseases Risk Readmission :microscope: :hospital:

![Python](https://img.shields.io/badge/Python-black.svg?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-blue.svg?style=flat&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-green.svg?style=flat&logo=)
![Data Science](https://img.shields.io/badge/Data%20Science-orange.svg?style=flat&logo=chart-line)

This project is a comprehensive Flask application designed to predict the risk of various diseases, including heart disease, diabetes, breast cancer, liver disease, and kidney disease, using machine learning models. Powered by Python and Flask, the application provides a user-friendly web interface for easy interaction with the predictive models.

## ⚙️ Technologies Used
- **Python:** Primary programming language used.

- **Flask:** Web framework for the application.

- **Random Forest Algorithm:** Machine learning algorithm for predictions.

- **Pickle:** For saving and loading machine learning models.

## ⭐: Features

- **Multi-Disease Prediction:** Predict the risk for multiple diseases including:
  - Heart Disease
  - Diabetes
  - Breast Cancer
  - Liver Disease
  - Kidney Disease
- **User-Friendly Interface:** Easy to navigate web interface built with Flask.
- **Accuracy:** Utilizes Random Forest algorithm for high prediction accuracy.
- **Data Analysis:** Comprehensive data analysis and model training documentation.

## 🔧: Installation

To set up the project environment, follow these steps:

**1. Clone the repository**

       git clone https://github.com/ChinmayBitne/Predictive-Analysis-of-Various-Diseases-Risk-Readmission.git

       cd Predictive-Analysis-of-Various-Diseases-Risk-Readmission

**2. Set Up Environment (Optional)**
    
        python -m venv venv
    
**3. Activate Enviroment (Optional)**

       venv\Scripts\activate
    
### Install the requirements 🗃️

    pip install -r requirements.txt
    
**Run the application**

    python main.py
    
_The application should now be running on http://localhost:5000._


## 📐: How It Works

- **Choose Disease Prediction:** Navigate to the disease prediction page you are interested in from the home page.

- **Input Data:** Fill in the required information in the form and submit.

- **View Prediction:** The application will display the predicted risk based on the input data.

## 📁: Project Structure

- main.py : The Flask application's entry point.

- models/ : Directory containing the trained model pickle files for each disease.

- templates/ : HTML files for the web interface.

- static/ : CSS and JavaScript files for the web design.

- data_analysis/ : Jupyter notebooks for data analysis and model training.

- requirements.txt : Project dependencies.
