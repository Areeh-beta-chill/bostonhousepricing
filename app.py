import pickle
from flask import FLask, request, app, jsonify, render_templete
import numpy as np
import pandas as pd

app = Flask(__name__)
## load the model
model = pickle.load(open('rehmodel.pkl', 'rb'))

@app.route('/')
def home():

    return render_templete('home.html')

@app.route('/predict_api', methods=['POST']) ## post means when we request we'll get an output

def predict_api():
    data = request.json['data'] #when we did the request through `request.json['data']` the data will be stored in 'data' variable
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)



