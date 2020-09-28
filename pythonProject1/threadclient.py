import socket
client=socket.socket()
name=input("Input login name:")
client.connect(("localhost",9001))
client.send("connect:{}".format(name).encode('ascii'))
while True:
    ch=int(input("1.messege\n2.exit"))
    if ch==1:
        msg=input("enter a message:")
        client.send("message:{}".format(msg).encode('ascii'))
    elif ch==2:
        client.send("disconnect:{}".format(name).encode('ascii'))
        client.close()
        break
    else:
        print("invalid option try again")