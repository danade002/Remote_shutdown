#Master

import time
import sys
import socket
import os

soc = socket.socket()
host = socket.gethostname()
print(host)
port =8282
soc.bind((host, port))
print("")
print("Waiting for any incoming connection...")
print("")
soc.listen(1)
conn, addr = soc.accept()
print("")
print(addr, "Connected to server")
print("")

command  = input(str("Command: "))
conn.send(command.encode())
print("Command has been sent successfully...")
print("")

data = conn.recv(1024)
if data:
    print("Shutdown Command has been recieved and executed")
    print("")
    
                 
