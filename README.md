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

## Directory Structure

student-placement-prediction/
├── app.py                    # Flask application script
├── student_placement.pkl      # Pre-trained model file
├── templates/                 # Folder for HTML templates
│   ├── index.html            # Form for user input
│   ├── placed.html           # Page shown for placed students
│   └── not_placed.html       # Page shown for non-placed students
└── requirements.txt           # List of Python dependencies

### Install Dependencies

First, clone the repository:

```bash
git clone https://github.com/your-username/student-placement-prediction.git
cd student-placement-prediction
Then, install the required dependencies:
```bash
pip install -r requirements.txt
This will install Flask, Scikit-learn, Numpy, and other necessary dependencies.


## Acknowledgments
Flask: For the web framework to build the application.
Scikit-learn: For the machine learning library used to build and deploy the model.
Numpy: For numerical operations during model prediction.

## Future Enhancements
Add additional features for prediction, such as previous internship experience or extracurricular activities.
Improve the machine learning model by exploring different algorithms and techniques.
Implement user authentication for personalized experiences.
