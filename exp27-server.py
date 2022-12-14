import socket

s = socket.socket()
s.bind(("localhost",4000))
s.listen()
conn,addr = s.accept()
msg = "I am server and i am always listening"
conn.send(msg.encode())
while True:
    msg = conn.recv(1024).decode()
    print(addr,": ",msg)
    msg = input(" -> ")
    conn.send(msg.encode())
