#Slave

import time
import sys
import socket
import os

soc = socket.socket()
host = "Ademeso"
port =8282
soc.connect((host, port))
print("Connected to server")

command = soc.recv(1024)
command = command.decode()
if command == "shutdown":
    print("")
    print("Shutdown command")
    soc.send("command recieved".encode())
    os.system("shutdown.bat")
