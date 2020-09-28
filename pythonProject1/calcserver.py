import socket
import re
server=socket.socket()
server.bind(("localhost",9001))
server.listen(10)
msg2=''
print("waiting for client")
while True:
    client,addr=server.accept()
    msg=client.recv(1024).decode('ascii')
    oper=re.findall('[0-9]+',msg)
    num=list(map(int,oper))
    a=num[0]
    b=num[1]
    if '+' in msg:
        res = a + b
    elif '-' in msg:
        res = a - b
    elif '*' in msg:
        res = a * b
    elif '/' in msg:
        res = a / b
    else:
        print("invalid")
    msg2 = str(res)
    client.send(msg2.encode('ascii'))
    client.close()

# server.close()