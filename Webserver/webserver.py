from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Memory.queries import *
from Knowledge.tris import *
from Utils.constants import *

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

@app.route('/api/checkLevel', methods=['POST'])
def checkLevel():
    data = request.json  # Get JSON data sent to the server
    username = data['username']

    levels = checkLevelQuery(username)


    result = {
        'success': True
    }
    print(levels)

    if len(levels) == 0:
        result['level'] = 'beginner'
        return result
    
    ai_wins = levels[0]['AI_wins']
    human_wins = levels[0]['human_wins']
    ratio = human_wins / ai_wins

    if ratio >=PRO_RATIO:
        setLevel(username, 'PRO')
    elif ratio >= INTERMEDIATE_RATIO:
        setLevel(username, 'INTERMEDIATE')
    else:
        setLevel(username, 'BEGINNER')

    return jsonify(result)  # Return JSON response


if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run the server
