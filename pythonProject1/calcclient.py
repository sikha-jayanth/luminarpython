import socket
client=socket.socket()
print("connecting to server....")
client.connect(("localhost",9001))
exp=input("enter an expression :")
client.send(exp.encode('ascii'))
print(client.recv(1024).decode('ascii'))
client.close()