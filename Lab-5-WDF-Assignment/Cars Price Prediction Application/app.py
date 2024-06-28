from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import sklearn

app = Flask(__name__)

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
    # Extract data from form
        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        owner = int(request.form['Owner'])
        fuel_type = request.form['Fuel_Type']
        Age_of_the_car = request.form['Age_of_the_car']
        seller_type = request.form['Seller_Type']
        transmission = request.form['Transmission']


        prediction=model.predict([[present_price, kms_driven,owner,fuel_type, Age_of_the_car, seller_type, transmission]])
        output= round(prediction[0], 2)
        return render_template('index.html', prediction_text="you can sell you car at {} lakhs".format(output))


if __name__ == '__main__':
    app.run(debug=True)
