import socket
s=socket.socket()
s.connect(('localhost',5000))
while True: 
 print(s.recv(1024).decode())
 s.send("acknowledgement recived from the server".encode())