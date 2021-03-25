from flask import Flask, render_template, request, jsonify
import util
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root,'./')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("app.html")

@app.route("/hello")
def hello():
    return "Hi"

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedroom = int(request.form['bedroom'])
    bath = int(request.form['bath'])
    
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bedroom,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
