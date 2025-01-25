# Student Placement Prediction

This is a simple Flask web application that predicts whether a student will be placed based on their academic performance. The model uses three features: CGPA, IQ, and Profile Score, to make predictions. The model was built using machine learning and is deployed as a Flask web app.

## Features

- **User Input**: The user can input their CGPA, IQ, and Profile Score through a simple HTML form.
- **Prediction**: Based on the input values, the application predicts whether the student will be placed or not.
- **Result Pages**: After making the prediction, the user is redirected to a page showing whether they are placed or not.

## Requirements

- Python 3.x
- Flask
- Scikit-learn
- Numpy

## Files
app.py: The main Flask application file, which loads the model and handles the user requests.
student_placement.pkl: The trained machine learning model used for predictions.
templates/: Contains HTML files for rendering the form and result pages.
index.html: The form where users input their data.
placed.html: The page shown when the student is predicted to be placed.
not_placed.html: The page shown when the student is predicted not to be placed.

## How It Works
The user visits the home page and enters their CGPA, IQ, and Profile Score.
When the user submits the form, the data is sent to the /predict endpoint via a POST request.
The model is loaded using pickle, and the input data is passed to the model for prediction.
If the model predicts that the student is placed, they are redirected to the placed.html page. Otherwise, they are redirected to the not_placed.html page.
License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Flask for the web framework
Scikit-learn for building the machine learning model
Numpy for handling numerical operations
You can install the required dependencies using `pip`:

pip install flask scikit-learn numpy
## Setup
Clone this repository to your local machine.

git clone https://github.com/your-username/student-placement-prediction.git
Download the machine learning model (student_placement.pkl) and place it in the same directory as app.py.

## Run the application:
python app.py
Visit http://127.0.0.1:5000/ in your browser to interact with the application.

