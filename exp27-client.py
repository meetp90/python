import socket

s = socket.socket()
s.connect(("localhost",4000))
while True:
    msg = s.recv(1024).decode()
    print("server said : ",msg)
    msg = input("->")
    s.send(msg.encode())
