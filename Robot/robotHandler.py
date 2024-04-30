import socket
import json

from robot import *

class RobotHandler():
    def __init__(self):

        self.robot = Robot(port = 38259)
        return
    
    def startSocket(self):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 12345))  # '0.0.0.0' permette connessioni da qualsiasi indirizzo
        server_socket.listen(1)

        while True:
            client_socket, addr = server_socket.accept()
            print("Connected by", addr)
            while True:
                received = client_socket.recv(1024)
                if not received:
                    break

                received = received.decode('UTF-8')
                received = json.loads(received)
                data = {str(k): str(v) for k, v in received.items()}
                
                response = self.handle(data)

                response = json.dumps(response)
                client_socket.sendall('Done')

            print("Connection closed ", addr)
            client_socket.close()
        return
    
    def handle(self, data):
        print("data: ", data)

        if data['action'] == 'say':
            self.robot.say(data['message'])
            
        if data['action'] == 'shield':
            self.robot.countDown()
            self.robot.shieldPosition()
            self.robot.say(data['action'])

        if data['action'] == 'shoot':
            self.robot.countDown()
            self.robot.shootPosition()
            self.robot.say(data['action'])

        if data['action'] == 'charge':
            self.robot.countDown()
            self.robot.chargePosition()
            self.robot.say(data['action'])


        time.sleep(1)

        return data




if __name__ == "__main__":

    robotHandler = RobotHandler()
    robotHandler.startSocket()

    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.bind(('0.0.0.0', 12345))  # '0.0.0.0' permette connessioni da qualsiasi indirizzo
    # server_socket.listen(1)

    # while True:
    #     client_socket, addr = server_socket.accept()
    #     print "Connected by", addr
    #     while True:
    #         data = client_socket.recv(1024)
    #         if not data:
    #             break
    #         client_socket.sendall(data)
    #     client_socket.close()

