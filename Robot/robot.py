import qi
import time
import math
import sys

class Robot():
    def __init__(self, port):
        self.session = self.initConnection(port = port)
        self.motion_service = self.session.service("ALMotion")
        self.tts_service = self.session.service("ALTextToSpeech")

        return
    
    def initConnection(self, ip = '127.0.0.1', port=44255):

        try:
            connection_url = "tcp://" + ip + ":" + str(port)
            app = qi.Application(["Move", "--qi-url=" + connection_url ])
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + ip + "\" on port " + str(port) +".\n"
                "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

        app.start()
        session = app.session

        return session

    def say(self, sentence, language = "English", speed = 1000, volume = 1.0):

        self.tts_service.setLanguage(language)
        self.tts_service.setParameter("speed", speed)
        self.tts_service.setVolume(volume)

        self.tts_service.say(sentence)

        return

    def startPosition(self):
        

        shoulder_pitch_angle = math.radians(85)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        shoulder_roll_angle = math.radians(-6)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        # Impostare l'angolo del giunto RElbowRoll per fare in modo che il braccio punti verso il basso
        elbow_roll_angle = math.radians(0.5)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        elbow_yaw_angle = math.radians(87)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        fractionMaxSpeed = 0.5  # Velocita massima del movimento (da 0.0 a 1.0)

        # Settare gli angoli dei giunti
        self.motion_service.setAngles("RShoulderPitch", shoulder_pitch_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RShoulderRoll", shoulder_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowRoll", elbow_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowYaw", elbow_yaw_angle, fractionMaxSpeed)

        return

    def shootPosition(self):
        

        shoulder_pitch_angle = math.radians(85)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        shoulder_roll_angle = math.radians(-6)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        # Impostare l'angolo del giunto RElbowRoll per fare in modo che il braccio punti verso il basso
        elbow_roll_angle = math.radians(80)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        elbow_yaw_angle = math.radians(87)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        fractionMaxSpeed = 0.5  # Velocita massima del movimento (da 0.0 a 1.0)

        # Settare gli angoli dei giunti
        self.motion_service.setAngles("RShoulderPitch", shoulder_pitch_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RShoulderRoll", shoulder_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowRoll", elbow_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowYaw", elbow_yaw_angle, fractionMaxSpeed)

        return

    def shieldPosition(self):
        

        shoulder_pitch_angle = math.radians(0)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        shoulder_roll_angle = math.radians(-6)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        # Impostare l'angolo del giunto RElbowRoll per fare in modo che il braccio punti verso il basso
        elbow_roll_angle = math.radians(73)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        elbow_yaw_angle = math.radians(10)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        fractionMaxSpeed = 0.5  # Velocita massima del movimento (da 0.0 a 1.0)

        # Settare gli angoli dei giunti
        self.motion_service.setAngles("RShoulderPitch", shoulder_pitch_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RShoulderRoll", shoulder_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowRoll", elbow_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowYaw", elbow_yaw_angle, fractionMaxSpeed)

        return

    def chargePosition(self):
        

        shoulder_pitch_angle = math.radians(0)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        shoulder_roll_angle = math.radians(-6)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        # Impostare l'angolo del giunto RElbowRoll per fare in modo che il braccio punti verso il basso
        elbow_roll_angle = math.radians(73)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)
        elbow_yaw_angle = math.radians(87)  # Angolo in radianti (esempio di angolo, sperimenta con valori diversi)

        fractionMaxSpeed = 0.5  # Velocita massima del movimento (da 0.0 a 1.0)

        # Settare gli angoli dei giunti
        self.motion_service.setAngles("RShoulderPitch", shoulder_pitch_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RShoulderRoll", shoulder_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowRoll", elbow_roll_angle, fractionMaxSpeed)
        self.motion_service.setAngles("RElbowYaw", elbow_yaw_angle, fractionMaxSpeed)

        return
    
    def countDown(self):
        self.say("Rest")
        self.startPosition()
        time.sleep(1)
        self.say("3")
        time.sleep(1)
        self.say("2")
        time.sleep(1)
        self.say("1")
        time.sleep(1)

        return


if __name__ == "__main__":

    robot = Robot(38259)
    robot.say("Hello")
    robot.countDown()
    robot.shieldPosition()
    robot.countDown()
    robot.shootPosition()
    robot.countDown()
    robot.chargePosition()
