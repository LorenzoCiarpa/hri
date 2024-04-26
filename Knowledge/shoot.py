import random
import os
import sys

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Memory.shootQueries import *
from MentalModel.mentalShoot import *
from Peripherals.camera import getInstantShot
from EmotionRecognition.imageEmotionRecognition import getEmotionFromImg
from ImageClassification.moveClassifier import moveClassifier

MOVES = [
    'shield',
    'charge', 
    'shoot'
]

class Actor():
    def __init__(self, name) -> None:
        self.name = name
        self.life = 3
        self.bullets = 0
        return

    def __str__(self) -> str:
        return f"{self.name}: life: {self.life}, bullets: {self.bullets}"

class ShootGame():
    def __init__(self, username) -> None:

        self.username = username

        self.match = {
            'ai': Actor('ai'),
            'human': Actor('human')
        }  

        self.moves = []

        self.mentalModel = ShootInteractionHandler()

        return

    def game(self):
        winner = self.checkWinner()
        while winner is None:
            turn = self.turn()
            self.moves.append(turn)
            print(f"turn: {turn}, {self.match['ai']}, {self.match['human']} ")

            winner = self.checkWinner()

        print(f'winner: {winner}')
        self.mentalModel.endMatch(winner)
        self.setWinner(winner)

        return self.moves

    def turn(self):
        humanMove = self.getHumanMove()
        aiMove = self.getAiMove()

        aiActor = {
            'name': 'ai',
            'move': aiMove
        }

        humanActor = {
            'name': 'human',
            'move': humanMove
        }
        
        self.checkCharge(humanActor)
        self.checkCharge(aiActor)
        
        self.checkHit(humanActor, aiActor)
        self.checkHit(aiActor, humanActor)
        
        
        return (aiActor, humanActor)

    def getHumanMove(self):
        # CORRECT FINAL VERSION
        # getInstantShot(PATH_MOVE)
        # index = moveClassifier(PATH_MOVE)

        index = random.randint(0, 2)
        return MOVES[index]
    
    def getAiMove(self):
        index = random.randint(0, 2)
        return MOVES[index]
    
    def setWinner(self, winner):
        setWinnerShoot(self.username, winner)
        return
    
    def checkWinner(self):
        if self.match['ai'].life == 0 and self.match['human'].life == 0:
            return 'draw'

        if self.match['ai'].life == 0:
            return 'human'
        
        if self.match['human'].life == 0:
            return 'ai'
        

        return None
    
    def checkCharge(self, actor):
        if actor['move'] == 'charge':
            self.match[actor['name']].bullets += 1

        return 
    
    def checkHit(self, attacker, defender):
        #TODO handle if action shoot chosen and no bullet available??
        if attacker['move'] == 'shoot' and self.match[attacker['name']].bullets > 0:
            self.match[attacker['name']].bullets -= 1
            if defender['move'] != 'shield':
                self.match[defender['name']].life -= 1
        return
    

if __name__ == '__main__':
    game = ShootGame('b')
    game.game()