import socket
server=socket.socket()
server.bind(("localhost",9001))
server.listen(10)
print("server waiting for connection")
client,addr=server.accept()
print(client.recv(1024).decode('ascii'))
client.close()
server.close()