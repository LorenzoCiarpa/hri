import os
import sys
import socket
import json

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

class RobotCommunicator():
    def __init__(self):
        self.initSocket()
        return
    
    def initSocket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))  # Assicurati che la porta 12345 sia esposta dal Docker
        return

    def closeSocketConnection(self):
        self.client_socket.close()
        return

    def sendMessageSocket(self, message):
        self.client_socket.sendall(bytes(json.dumps(message).encode('UTF-8')))
        return

    def readMessageSocket(self):
        response = self.client_socket.recv(1024)
        return response.decode()
    
    def say(self, message):
        socketMessage = {
            'action': 'say',
            'message': message
        }

        self.sendMessageSocket(socketMessage)
        self.readMessageSocket()

        return
    
    def move(self, action):
        socketMessage = {
            'action': action
        }

        self.sendMessageSocket(socketMessage)
        self.readMessageSocket()

        return
    
robotCommunicator = RobotCommunicator() 