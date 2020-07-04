import socket

HEADERSIZE = 4
print("Start")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
print(s)

appended_message = ""
new_message = True
i = 0
while i < 100:
    i += 1
    #print(i)
    frame = s.recv(HEADERSIZE)
    #print(frame.decode('utf-8'))
    if len(frame) > 0:
        if new_message:
            message_length = int(frame[:HEADERSIZE])
            print(f"-- Message length: {message_length}")
            new_message = False
        else:
            appended_message += frame.decode('utf-8')
        #print(f"F={len(frame)} M={len(appended_message)} H={HEADERSIZE}")
        #print(f"len(frame) is {len(frame)} len(appended_message) is {len(appended_message)} and message_length is {message_length}")
        #print(appended_message)
        if len(appended_message) >= message_length:
            print(f"-- Full message recived {message_length}")
            print(appended_message)
            new_message = True
            appended_message = ""
print("Stop")