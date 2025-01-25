from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pickle

# Load the machine learning model
model = pickle.load(open('student_placement.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    # Render a simple HTML form to take user input
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input data from the form
        cgpa = float(request.form.get('cgpa'))
        iq = float(request.form.get('iq'))
        profile_score = float(request.form.get('profile_score'))

        # Prepare the input for the ML model
        input_query = np.array([[cgpa, iq, profile_score]])

        # Make the prediction
        result = model.predict(input_query)[0]

        # Interpret the prediction
        if result == 1:
            # Redirect to the 'placed' page
            return redirect(url_for('placed'))
        else:
            # Redirect to the 'not_placed' page
            return redirect(url_for('not_placed'))

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/placed')
def placed():
    # Render the page for students who are placed
    return render_template('placed.html')

@app.route('/not_placed')
def not_placed():
    # Render the page for students who are not placed
    return render_template('not_placed.html')

if __name__ == '__main__':
    app.run(debug=True)
