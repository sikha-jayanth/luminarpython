import socket
client=socket.socket()
print("connecting to server")
client.connect(("localhost",9001))
client.send("Hello server..!".encode('ascii'))
print("data send")
client.close()