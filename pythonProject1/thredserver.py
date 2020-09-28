import socket
import _thread

server = socket.socket()

server.bind(("localhost", 9001))

server.listen(10)

def client_thread(client):
    name = ""
    while True:
        msg = client.recv(1024).decode("ascii")
        # command:arguments
        # commands => connect,message,disconnect
        # connect:name
        # message:"string"
        # disconnect:name
        # connect:user1
        # name = 'user1'
        # message:Hello i am online
        # command=message
        # arguments = Hello i am online
        command,arguments = msg.split(":")
        if command=='connect':
            name = arguments
        elif command=='message':
            message = arguments
            print("Message from %s: %s" % (name, message))
        elif command=='disconnect':
            print("Disconnecting ", name)
            client.close() #gracefully disconnect
            break # while True loop exit


    # thread exit gracefully
    #no longer serving that client

while True:
    client,addr = server.accept()
    print(addr)

    _thread.start_new_thread(client_thread, (client, ))