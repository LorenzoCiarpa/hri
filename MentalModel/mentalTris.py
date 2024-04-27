import os
import sys
import time

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Utils.constants import *
from Memory.queries import *
from Robot.say import *
from Peripherals.camera import getInstantShot
from EmotionRecognition.imageEmotionRecognition import getEmotionFromImg, getEmotionFromImgFer

class TrisInteractionHandler():

    def __init__(self) -> None:
        pass

    def levelChange(self, curr_level, new_level):
        
        message = ''
        if LEVELS[curr_level] < LEVELS[new_level]:
            message = "Great you are improving a lot! \n I will try to be better!"
        elif LEVELS[curr_level] > LEVELS[new_level]:
            message = "It seems like you still have to learn a lot... \n I will try to be softer!"
        else:
            # message = "Still a draw... Let's do another match!"
            message = ""

        say(message)
        print(message)
        return
    
    def endMatch(self, winner, username): 
        emotion = self.handleEmotion()
        print(f'emotion: {emotion}')
        message = ''
        if emotion == 'sad':
            message = "Oh no my friend, don't be sad, we can do a re-match! I will be softer."
            self.decreaseLevel(username)
        elif emotion == 'happy':
            message = "Are you fooling me?! let's see if you are able to beat me now!"
            self.increaseLevel(username)
        elif emotion == 'angry':
            message = self.handleAnger(username)
            if message == '':
                message = "Don't be angry, we can still play!"
        else: #could be neutral, fear, surprise, disgust
            message = ""

        say(message)
        print(message)

        if winner == 'AI':
            message = "I won!"
        elif winner == 'HUMAN':
            message = "Oh no i lost!"
        else:
            message = "Another Draw..."

        say(message)
        print(message)
        return
    
    def decreaseLevel(self, username):
        level = getLevel(username)[0]['level']
        new_level_idx = LEVELS[level] - 1 if LEVELS[level] > 0 else 0
        new_level = IDX_TO_LEVELS[new_level_idx]

        ratio = LEVELS_TO_RATIO[new_level]
        ratio = ratio if ratio > 0 else 1
        
        deleteRecordForNewLevel(username, ratio)
        setLevel(username, new_level)

        return
    
    def increaseLevel(self, username):
        level = getLevel(username)[0]['level']
        new_level_idx = LEVELS[level] + 1 if LEVELS[level] < 2 else 2
        new_level = IDX_TO_LEVELS[new_level_idx]

        ratio = LEVELS_TO_RATIO[new_level]
        
        createRecordForNewLevel(username, ratio)
        setLevel(username, new_level)

        return
    
    def handleAnger(self, username):
        message = ''

        angerCounter = getAngerLevel(username)[0]['angerCounter']
        newAngerCounter = angerCounter + 1
        if newAngerCounter >= MAX_ANGER_LEVEL:
            self.decreaseLevel(username)
            newAngerCounter = 0
            message = 'Calm down! I will play softer!'
        
        setAngerCounter(username, newAngerCounter)

        return message
    
    def newUser(self, username):
        say(f"Welcome {username}, these are the rules of the game...")
        return
    
    def handleEmotion(self):
        
        getInstantShot(PATH_FACE)
        # emotion = getEmotionFromImg(PATH_FACE) #OLD VERSION(deepface)
        emotion = getEmotionFromImgFer(PATH_FACE)
        return emotion

if __name__ == '__main__':
    trisHandler = TrisInteractionHandler()
    # emotion = trisHandler.handleEmotion()
    # print(f'emotion: {emotion}')

    trisHandler.endMatch('AI')