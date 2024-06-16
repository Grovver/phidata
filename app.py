# app.py
from flask import Flask, render_template, jsonify
import subprocess
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        script_path = os.path.join(os.getcwd(), 'cookbook', 'assistants', 'basic3.py')
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        response_data = json.loads(result.stdout)
        return jsonify(response_data)
    except subprocess.CalledProcessError as e:
        return jsonify(error=str(e), output=e.output)

if __name__ == '__main__':
    app.run(debug=True)
