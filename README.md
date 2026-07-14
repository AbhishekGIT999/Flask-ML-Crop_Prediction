# Flask-ML-Crop_Prediction


A machine learning web application built with Flask that recommends the most suitable crop based on soil nutrient values and environmental conditions. The project uses a trained Random Forest classification model to generate predictions through a simple and interactive web interface.

---

## Overview

Selecting the right crop plays an important role in improving agricultural productivity. This project demonstrates how machine learning can assist in crop recommendation by analyzing soil nutrients and environmental factors. Users enter the required input values through a web interface, and the application predicts the most suitable crop.

---

## Features

* Crop recommendation using machine learning
* Flask-based web application
* User-friendly interface
* Random Forest classification model
* Fast prediction results
* Simple and easy-to-understand project structure

---

## Technologies Used

* Python
* Flask
* NumPy
* Pandas
* Scikit-learn
* HTML
* CSS
* JavaScript
* Pickle

---

## Project Structure

```text
Flask-ML-Crop_Prediction/
│
├── app.py
├── model.py
├── model.pkl
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
└── dataset/
```

---

## Input Parameters

The prediction model uses the following parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH Value
* Rainfall

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AbhishekGIT999/Flask-ML-Crop_Prediction.git
```

Move into the project directory:

```bash
cd Flask-ML-Crop_Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## Machine Learning Model

* Algorithm: Random Forest Classifier
* Library: Scikit-learn
* Model Serialization: Pickle (.pkl)

---

## Dataset

The model is trained using a crop recommendation dataset containing soil nutrient values and environmental factors used for supervised classification.

---

## Future Improvements

* Improve the user interface
* Add input validation
* Compare multiple machine learning algorithms
* Deploy the application to a cloud platform
* Add prediction history
* Expose predictions through a REST API

---

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

---

## Author

**Abhishek Jha**

GitHub: https://github.com/AbhishekGIT999

---

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub.
