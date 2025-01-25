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
├── app.py                    
├── student_placement.pkl      
├── templates/                 
│   ├── index.html           
│   ├── placed.html          
│   └── not_placed.html      
├── static/                   
│   └── style.css             
└── requirements.txt          
               


### Install Dependencies

First, clone the repository:

git clone https://github.com/your-username/student-placement-prediction.git
cd student-placement-prediction
Then, install the required dependencies:


## Acknowledgments
Flask: For the web framework to build the application.
Scikit-learn: For the machine learning library used to build and deploy the model.
Numpy: For numerical operations during model prediction.

## Future Enhancements
Add additional features for prediction, such as previous internship experience or extracurricular activities.
Improve the machine learning model by exploring different algorithms and techniques.
Implement user authentication for personalized experiences.
