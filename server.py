import socket

HEADERSIZE = 4
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 1234))
serversocket.listen()
print(f"Listenning at: {serversocket}")
print("Waiting for someone to connect...")
while True:
    clientsocket, address = serversocket.accept()
    print(f"Connection from {address} has been established!")
    msg = f"The server {socket.gethostname()} salutes you for wanting to communicate."
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    print(f"len(msg) is {len(msg)} msg = '{msg}'")
    clientsocket.send(bytes(msg, "utf-8"))
    #clientsocket.send(bytes(f"The server {socket.gethostname()} salutes you for wanting to communicate ", "utf-8"))
    #msg = f"The server {socket.gethostname()} is closing its socket."
    #msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #print(msg)
    #clientsocket.send(bytes(msg, "utf-8"))
    #clientsocket.send(bytes(f"The server {socket.gethostname()} is closing its socket.", "utf-8"))
    clientsocket.close()