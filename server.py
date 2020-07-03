import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 1234))
serversocket.listen()

print("Waiting for someone to connect...")
while True:
    clientsocket, address = serversocket.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes(f"The server {socket.gethostname()} salutes you for wanting to communicate ", "utf-8"))
    clientsocket.send(bytes(socket.gethostname(), "utf-8"))
    clientsocket.send(bytes(".", "utf-8"))
    clientsocket.close()