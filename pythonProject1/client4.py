import socket
client=socket.socket()
client.connect(("localhost",9001))
print("connected to server")

name=input("input a name")
msg="Hello I am {}".format(name)
client.send(msg.encode('ascii'))
print("message from server")
print(client.recv(1024).decode('ascii'))
client.close()