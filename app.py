import numpy as np
from flask import Flask, request,render_template
import pickle

flask_app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@flask_app.route('/')
def Home():
    return render_template('index.html')

@flask_app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the request
    float_features = [float(x) for x in request.form.values()]
    
    features = [np.array(float_features)]

    # Make a prediction using the loaded model
    prediction = model.predict(features)
    
    return render_template('index.html', prediction_text='The predicted crop is {}'.format(prediction[0]))

if __name__ == "__main__":
    flask_app.run(debug=True)
    