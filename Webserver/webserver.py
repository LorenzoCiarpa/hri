from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Memory.queries import *
from Knowledge.tris import *

app = Flask(__name__)
CORS(app)

@app.route('/api/loginUser', methods=['POST'])
def get_data():
    data = request.json  # Get JSON data sent to the server
    username = data['username']
    result = createUser(username)

    message = f"Welcome {username}"

    print(result)

    if result['new_account'] is False:
        message = f"Welcome back {username}"

    
    return jsonify({'success': True, 'message': message})  # Return JSON response

@app.route('/api/makeMove', methods=['POST'])
def makeMove():
    data = request.json
    boardGame = data['boardGame']

    aiMove = find_best_move(boardGame)
    
    return jsonify({'success': True, 'boardGame': boardGame, 'aiMove': aiMove})  # Return JSON response

@app.route('/api/setResultMatch', methods=['POST'])
def setResultMatch():
    data = request.json  # Get JSON data sent to the server
    username = data['username']
    winner = data['winner']

    result = setWinner(username, winner)

    return jsonify(result)  # Return JSON response



if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run the server
