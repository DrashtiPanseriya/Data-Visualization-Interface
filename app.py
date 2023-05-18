from flask import Flask, render_template, request
from data_visualization import generate_visuals
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

import datetime

# ...

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        # Save the uploaded file to a temporary location
        file.save('temp.csv')
        # Call the generate_visuals function from data_visualization.py
        generate_visuals('temp.csv')
        return render_template('result.html')
    else:
        return "Invalid file format. Please upload a CSV file."


if __name__ == '__main__':
    app.run(debug=True)