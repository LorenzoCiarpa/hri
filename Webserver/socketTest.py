import socket
import json

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
        
        print(f"received: {data}")

        response = data

        response = json.dumps(response)
        client_socket.sendall(b'Done')

    print("Connection closed ", addr)
    client_socket.close()