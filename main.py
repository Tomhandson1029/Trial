from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

model = pickle.load(open('Models/heart_d.pkl', 'rb'))
model1 = pickle.load(open('Models/diabetes.pkl', 'rb'))
model2 = pickle.load(open('Models/breast_cancer.pkl', 'rb'))
model3 = pickle.load(open('Models/liver.pkl', 'rb'))
model4 = pickle.load(open('Models/kidney.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Heart')
def heart():
    return render_template('heart.html')


@app.route('/Diabetes')
def diabetes():
    return render_template('diabetes.html')


@app.route('/Breast_Cancer')
def breast_cancer():
    return render_template('breast_cancer.html')


@app.route('/Liver')
def Liver():
    return render_template('liver.html')


@app.route('/Kidney')
def kidney():
    return render_template('kidney.html')


@app.route('/About')
def About():
    return render_template('about-us.html')


@app.route('/ContactUs')
def Contact():
    return render_template('contact.html')


@app.route('/predictheart', methods=['POST', 'GET'])
def predictheart():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ["male", "age", "currentSmoker",
                     "cigsPerDay", "BPMeds", "prevalentStroke",
                     "prevalentHyp", "diabetes", "totChol", "sysBP",
                     "diaBP", "BMI", "heartRate", "glucose"]

    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)

    if output == 1:
        res_val = "a high risk of Heart Disease"
    else:
        res_val = "a low risk of Heart Disease"

    return render_template('heart.html', prediction_text='Patient has {}'.format(res_val))


@app.route('/predict_diabetes', methods=['POST', 'GET'])
def predictd():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ["Pregnancies", "Glucose", "BloodPressure",
                     "SkinThickness", "Insulin", "BMI",
                     "DiabetesPedigreeFunction", "Age"]

    data = pd.DataFrame(features_value, columns=features_name)
    my_prediction = model1.predict(data)

    if my_prediction == 1:
        res = "a high risk of Diabetes"
    else:
        res = "a low risk of Diabetes"

    return render_template('diabetes.html', prediction_text='Patient has {}'.format(res))


@app.route('/predict_breastcancer', methods=['POST', 'GET'])
def predictbc():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ["radius", "texture", "perimeter", "area", "smoothness"]

    data1 = pd.DataFrame(features_value, columns=features_name)
    my_prediction1 = model2.predict(data1)

    if my_prediction1 == 1:
        res1 = "a high risk of Breast Cancer"
    else:
        res1 = "a low risk of Breast Cancer"

    return render_template('breast_cancer.html', prediction_text='Patient has {}'.format(res1))


@app.route('/predict_liver', methods=['POST', 'GET'])
def predictl():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ["Age", "Gender", "Total_Bilirubin", "Direct_Bilirubin", "Alkaline_Phosphotase",
                     "Alamine_Aminotransferase", "Aspartate_Aminotransferase", "Total_Protiens",
                     "Albumin", "Albumin_and_Globulin_Ratio"]

    data2 = pd.DataFrame(features_value, columns=features_name)
    my_prediction2 = model3.predict(data2)

    if my_prediction2 == 2:
        res2 = "a high risk of Liver Disease"
    else:
        res2 = "a low risk of Liver Disease"

    return render_template('liver.html', prediction_text='Patient has {}'.format(res2))


@app.route('/predict_kidney', methods=['POST', 'GET'])
def predictk():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ['age', 'bp', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu', 'sc',
                     'pot', 'wc', 'htn', 'dm', 'cad', 'pe', 'ane']

    data3 = pd.DataFrame(features_value, columns=features_name)
    my_prediction3 = model4.predict(data3)

    if my_prediction3 == 1:
        res3 = "a high risk of Kidney Disease"
    else:
        res3 = "a low risk of Kidney Disease"

    return render_template('kidney.html', prediction_text='Patient has {}'.format(res3))


if __name__ == "__main__":
    app.run(debug=True)
