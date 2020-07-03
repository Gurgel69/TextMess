import socket

print("Start")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
print(s)
if False:
    message = s.recv(1024)
    print(message.decode("utf-8"))
    message = s.recv(1024)
    print(message.decode("utf-8"))
appended_message = ""
while True:
    message = s.recv(8)
    print(len(message))
    if len(message) <=0:
        break
    appended_message += message.decode('utf-8')
print(appended_message)
print("Stop")