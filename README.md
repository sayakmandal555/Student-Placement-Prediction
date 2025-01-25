# Student Placement Prediction

The "Student Placement Prediction" project is a machine learning web application built using Flask. It predicts whether a student is likely to get placed based on their academic performance, including CGPA, IQ, and Profile Score. The application uses a machine learning model to make predictions and provides feedback to users in the form of simple web pages.

## Features

- **User Input**: Users can input their CGPA, IQ, and Profile Score.
- **Prediction**: The machine learning model makes a prediction based on the inputs.
- **Result Pages**: After prediction, users are redirected to one of two pages:
  - **Placed**: If the model predicts the student will be placed.
  - **Not Placed**: If the model predicts the student will not be placed.
  
## Technologies Used

- **Flask**: A lightweight Python web framework used to build the web application.
- **Scikit-learn**: A Python library used for creating and using the machine learning model.
- **Numpy**: A library for handling arrays and numerical operations.
- **Pickle**: A module used to serialize and deserialize the machine learning model.

## Prerequisites

To run the application, you'll need the following:

- Python 3.x or higher
- Internet connection to install dependencies

### Install Dependencies

First, clone the repository:

```bash
git clone https://github.com/your-username/student-placement-prediction.git
cd student-placement-prediction

Then, install the required dependencies:
pip install -r requirements.txt


##Setup
Clone the repository to your local machine:
git clone https://github.com/your-username/student-placement-prediction.git

Download the pre-trained machine learning model (student_placement.pkl) and save it in the project directory, alongside app.py.

Run the Flask application:

python app.py
Open a browser and navigate to http://127.0.0.1:5000/ to use the application.


##Files
app.py: The main Flask application file, which loads the model and handles the user requests.
student_placement.pkl: The trained machine learning model used for predictions.
templates/: Contains HTML files for rendering the form and result pages.
index.html: The form where users input their data.
placed.html: The page shown when the student is predicted to be placed.
not_placed.html: The page shown when the student is predicted not to be placed.

##Directory Structure
student-placement-prediction/
├── app.py                    # Flask application script
├── student_placement.pkl      # Pre-trained model file
├── templates/                 # Folder for HTML templates
│   ├── index.html            # Form for user input
│   ├── placed.html           # Page shown for placed students
│   └── not_placed.html       # Page shown for non-placed students
└── requirements.txt           # List of Python dependencies



##How It Works
The user visits the home page and enters their CGPA, IQ, and Profile Score.
When the user submits the form, the data is sent to the /predict endpoint via a POST request.
The model is loaded using pickle, and the input data is passed to the model for prediction.
If the model predicts that the student is placed, they are redirected to the placed.html page. Otherwise, they are redirected to the not_placed.html page.

##Acknowledgments
Flask for the web framework
Scikit-learn for building the machine learning model
Numpy for handling numerical operations
