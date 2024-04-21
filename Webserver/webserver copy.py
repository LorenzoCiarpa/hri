from flask import Flask, request, jsonify
import os
import sys

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Memory.queries import *

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    print("Entrato")
    return "ciao"
    # data = request.json  # Get JSON data sent to the server
    # return jsonify(data)  # Return JSON response

@app.route('/api/loginUser', methods=['GET'])
def get_data():
    print("Entrato")
    return "ciao"
    # data = request.json  # Get JSON data sent to the server
    # return jsonify(data)  # Return JSON response

@app.route('/api/query')
def get_query():
    query = request.args.get('query')
    return f"ciao {query}"

@app.route('/api/data/<username>')
def get_username(username):
    print(f"Entrato {username}")
    return f"ciao {username}"
    # data = request.json  # Get JSON data sent to the server
    # return jsonify(data)  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run the server
