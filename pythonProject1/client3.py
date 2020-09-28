import socket
client=socket.socket()
client.connect(("localhost",9001))
print("connected to server")
client.send("Hello server..!!".encode('ascii'))
print("message from server")
print(client.recv(1024).decode('ascii'))
client.close()