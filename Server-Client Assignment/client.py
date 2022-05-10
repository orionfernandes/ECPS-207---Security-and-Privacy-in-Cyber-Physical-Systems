#client.py      by Orion Peter Fernandes

import socket
from cryptography.fernet import Fernet
from socket import *
serverName = '127.0.0.1' #localHost IP
serverPort = 12000 #port number assigned

#AF_INET indicates we are using ipv4, SOCK_STREAM means we are using TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)  

file = open('public.txt', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()


#establishing a tcp socket connection with server 
clientSocket.connect((serverName, serverPort))

try:
    while True:
        a = input("Enter game_id = ")
        clientSocket.send(a.encode()) #sending to server
        gameid = input("> field = ")
        clientSocket.send(gameid.encode()) #sending to server
        encrypted = socket.recv(1024).decode()
        f = Fernet(key)
        decrypted = f.decrypt(encrypted)  # Decrypt the bytes. The returning object is of type bytes
        print(decrypted)

except KeyboardInterrupt:       #Ctrl-C to close input
    clientSocket.close()    #closing the socket


