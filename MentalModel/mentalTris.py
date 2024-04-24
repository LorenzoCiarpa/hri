import os
import sys
import time

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Utils.constants import *
from Robot.say import *

class TrisInteractionHandler():

    def __init__(self) -> None:
        pass

    def levelChange(self, curr_level, new_level):

        if LEVELS[curr_level] < LEVELS[new_level]:
            #leveled up
            print()
            say("Great you are improving a lot! \n I will try to be better!")

        elif LEVELS[curr_level] > LEVELS[new_level]:
            #leveled down
            print()
            say("It seems like you still have to learn a lot... \n I will try to be softer!")

        else:
            #not changed
            print()
            say("Still a draw... Let's do another match!")
        return
    
    def endMatch(self, winner): 
        emotion = self.handleEmotion()

        if emotion == 'sad':
            say("Oh no my friend, don't be sad, we can do a re-match!")
            #decreaseLevel(username)
        elif emotion == 'happy':
            say("Are you fooling me?! let's see if you are able to beat me now!")
            #increaseLevel(username)
        elif emotion == 'angry':
            say("Don't be angry, we can still play!")
        elif emotion == 'neutral':
            say("")

        if winner == 'AI':
            say("I won!")
        elif winner == 'HUMAN':
            say("Oh no i lost!")
        else:
            say("Another Draw...")
        return
    
    def newUser(self, username):
        say(f"Welcome {username}, these are the rules of the game...")
        return
    
    def handleEmotion(self):
        return

