import socket
client=socket.socket()
print("connecting to server...")
client.connect(('localhost',9001))
print("connected")