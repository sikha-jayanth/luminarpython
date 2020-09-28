import socket
server=socket.socket()
server.bind(('localhost',9001))
server.listen(10)
print("wating for a client")
client=server.accept()
print("client connected")
print(client)