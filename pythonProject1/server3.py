import socket
server=socket.socket()
server.bind(("localhost",9001))
server.listen(10)
while True:
    print("waiting for client")
    client,addr=server.accept()
    print("message from client")
    print(client.recv(1024).decode('ascii'))
    client.send("Hello client..!!".encode('ascii'))
    client.close()
    print("client disconnected")
