##accensione del robot
import os
import sys
project_folder = os.path.dirname(os.path.abspath(__file__))
print("Current folder:", project_folder)
sys.path.append(project_folder)
from Peripherals.video_audio import *
import time
status="STAND BY"
human_here=False
lets_play=True
selected_game=None
user=None
stop_playing=False
while True:
    if status is "STAND BY":
        # catturo audio e video
        # mando questi audio e video da qualche parte per capire se c'è qualcuno
        # se sì:
        human_here= False #oppure viene messo a true se c'è qualcuno
        if human_here:
            status="HAND SHAKING"
    
    if status is "HAND SHAKING":
        #viene chiesto se vuole giocare
        lets_play=True #segno a seconda della risposta
        if lets_play:
            status="LOGGING"
        else:
            status="STAND BY"
            time.sleep(10)

    if status is "LOGGING":
        user="io" #viene chiesto di loggarsi
        status="SELECTING GAME"
    if status is "SELECTING GAME":
        selected_game="TRIS" #viene chiesto a cosa vuole giocare
        status= "PLAYING"
    
    if status is "PLAYING":
        if selected_game is "TRIS":
            #qua come lo gestiamo?
        if selected_game is "SHOOT":
            #qua come lo gestiamo?

        if stop_playing:
            #il robot saluta e torna in stand by
            status="SALUTANDO"
            lets_play=False
    if status is "SALUTANDO":
        status="STAND BY"
        human_here=False
        selected_game=None
        user=None
        stop_playing=False
        time.sleep(10)    