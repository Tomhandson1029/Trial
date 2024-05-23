# :microscope: Predictive Analysis of Various Diseases Risk Readmission :hospital:

![Python](https://img.shields.io/badge/Python-grey.svg?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-blue.svg?style=flat&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-gren.svg?style=flat)
![Data Science](https://img.shields.io/badge/Data%20Science-darkorange.svg?style=flat)

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

- **Data Analysis & Model Training:** Our models are trained using the Random Forest algorithm, selected for its high accuracy. The training process involves extensive data analysis, ensuring reliable predictions.
- **Flask Application:** The web interface is built with Flask, providing a seamless experience for users to input their data and receive disease risk predictions.
- **Machine Learning Models:** Models are saved as pickle files and integrated into the Flask application for real-time predictions.

## 📁: Project Structure

- [main.py](main.py): Flask application entry point.
- [Models](Models): Directory containing the trained models as pickle files.
- [templates](templates): HTML templates for the web interface.
- [static](static): CSS/JS and other static files for the web interface.
- [Analyzing-Data](Anazyzing_Data.ipynb) & [Model-Training](Model_Training.ipynb): Jupyter notebooks for data analysis and model training.
- [Heart Disease Dataset EDA](Heart-EDA.html): Exploratory data analysis report for heart disease dataset
- [Dataset](Dataset): Contains the datasets used for training
