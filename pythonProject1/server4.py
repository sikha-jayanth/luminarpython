import socket
server=socket.socket()
server.bind(("localhost",9001))
server.listen(10)
while True:
    print("waiting for client")
    client,addr=server.accept()
    print("message from client")
    msg=client.recv(1024).decode('ascii')
    print("message form client:{}".format(msg))
    lst=msg.split()
    server_msg="Hello {}".format(lst[-1])
    client.send(server_msg.encode('ascii'))
    client.close()
    print("client disconnected")