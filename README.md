# Disease Risk Prediction Application

![Python](https://img.shields.io/badge/Python-3.8-blue.svg?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-1.1.2-lightgrey.svg?style=flat&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green.svg?style=flat)
![Data Science](https://img.shields.io/badge/Data%20Science-Numpy%20|%20Pandas-orange.svg?style=flat)

This project is a web-based application that utilizes machine learning to predict the risk of various diseases including heart disease, diabetes, breast cancer, liver disease, and kidney disease. It's built using Flask, a micro web framework written in Python, and employs machine learning models trained on relevant datasets. These models have been serialized into pickle files for easy loading and prediction.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Predictive modeling for various diseases:
  - Heart Disease
  - Diabetes
  - Breast Cancer
  - Liver Disease
  - Kidney Disease
- User-friendly web interface for submitting risk factors.
- Instant display of prediction results.

## Installation

Ensure you have Python 3.8 or later installed on your machine.

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
Navigate to the project directory:
cd your-repository-name
Install the required dependencies:
pip install -r requirements.txt
Usage
To run the application, execute the following command from the root directory of the project:

flask run
Then, navigate to http://127.0.0.1:5000/ in your web browser to start using the application.

Project Structure
your-repository-name/

│
├── models/                   # Directory for saved model pickle files

│
├── templates/                # HTML files for the web interface

│
├── static/                   # CSS/JS and other static files

│
├── main.py                   # Flask application main file

│
├── requirements.txt          # List of dependencies

│
├── README.md                 # Project README file

│
└── .git/                     # Git source repository
