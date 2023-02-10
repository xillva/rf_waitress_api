from flask import Flask, request
import numpy as np
import pickle as pk
import pandas as pd
from flasgger import Swagger
import os
from waitress import serve

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
dir_path = dir_path.replace("\\", "/")


with open(dir_path + "/rf.sav", "rb") as model_file :
    model = pk.load(model_file)
    
app = Flask(__name__)
swagger = Swagger(app)

@app.route("/predict")
def predict_iris():
    """Example File Endpoint Returning a Prediction of Iris Dataset
    ---
    parameters:
        - name: s_l
          in: query
          required: true
          type: number
        - name: s_w
          in: query
          required: true
          type: number
        - name: p_l
          in: query
          required: true
          type: number
        - name: p_w
          in: query
          required: true
          type: number
    responses:
        200:
          description: ok
    """
    s_l = request.args.get("s_l")
    s_w = request.args.get("s_w")
    p_l = request.args.get("p_l")
    p_w = request.args.get("p_w")
    
    prediction = model.predict(np.array([[s_l,s_w,p_l, p_w]]))
    
    return str(prediction)

@app.route("/predict_file", methods = ["POST"])
def predict_iris_file():
    """Example Endpoint Returning a Prediction of Iris Dataset
    ---
    parameters:
        - name: input_file
          in: formData
          required: true
          type: file
    responses:
        200:
          description: ok
    """
    data_pred =  pd.read_csv(request.files.get("input_file"), header=None)
    print(data_pred)
    prediction = model.predict(data_pred)
    
    return str(list(prediction))

if __name__ == "__main__":
    serve(app, listen = "*:5000", threads = 5)
    