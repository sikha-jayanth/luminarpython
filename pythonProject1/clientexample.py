import socket
import time

client = socket.socket()

client.connect(("localhost", 9001))
clientname = input("Enter Name: ")
while True:
    client.send(("pinging from %s" % (clientname))
                   .encode("ascii"))
    time.sleep(1)
