from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    data = pd.read_csv(file)
    # Perform analysis or prediction
    results = data.describe()  # Example: descriptive statistics
    return render_template('results.html', tables=[results.to_html()])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
