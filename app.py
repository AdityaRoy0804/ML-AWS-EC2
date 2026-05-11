from flask import Flask,render_template, request
import joblib
import numpy as np

## Model Load
model = joblib.load("student_placement_knn_model.pkl")


## Flask App
app = Flask(__name__)

## Routes and Views
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict_placement():
    cgpa = float(request.form["cgpa"])
    iq = int(request.form["iq"])
    profile_score = int(request.form["profile_score"])

    input_data = np.array([[cgpa,iq,profile_score]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "The student is likely to be placed."
    else:
        result = "The student is unlikely to be placed."

    return render_template("index.html", result = result)



## API Hosting
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 8000)