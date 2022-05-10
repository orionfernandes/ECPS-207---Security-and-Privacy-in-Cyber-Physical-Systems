#ECPS 207 - SEC & PRIVACY CPS           By Orion Peter Fernandes - 65047854

from dataclasses import field
from socket import *
import csv
import codecs
import pandas as pd
from cryptography.fernet import Fernet          # Using Fernet for Encryption
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



serverPort = 12000 #same port number as used in client script

key = Fernet.generate_key()

file = open('private.txt', 'wb')  # Open the private file as wb to write bytes
file.write(key)  # The key is type bytes still
file = open('public.txt', 'wb')  # Open the private file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()





def option_a():
    
    df = pd.read_csv("data_base.csv")
    b = (df.loc[df.game_id == a , 'type'])     
    print(a, "\t")
    print(b)
    message = b.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)  # Encrypt the bytes. The returning object is of type bytes
    connectionSocket.send(encrypted)

def option_b():
    
    df = pd.read_csv("data_base.csv")
    b = (df.loc[df.game_id == a, 'game_id'])
    b.to_string()
    print(a, "\t")
    print(b.to_string())

    
def option_c():
    
    df = pd.read_csv("data_base.csv")
    b = (df.loc[df.game_id == a, 'home_team'])
    b.to_string()
    print(a, "\t")
    print(b.to_string())

def option_d():
    
    df = pd.read_csv("data_base.csv")
    b =(df.loc[df.game_id == a, 'away_team'])
    b.to_string()
    print(a, "\t")
    print(b.to_string())

def option_e():
    
    df = pd.read_csv("data_base.csv")
    b =(df.loc[df.game_id == a, 'week'])
    b.to_string()
    print(a, "\t")
    print(b.to_string())

def option_f():
    
    df = pd.read_csv("data_base.csv")
    b =(df.loc[df.game_id == a, 'season'])
    b.to_string()
    print(a, "\t")
    print(b.to_string())

def option_g():
    
    df = pd.read_csv("data_base.csv")
    b =(df.loc[df.game_id == a, 'home_score'])
    b.to_string()
    print(a, "\t")
    print(b.to_string())

def option_h():
    
    df = pd.read_csv("data_base.csv")
    b = (df.loc[df.game_id == a, 'away_score'])
    b.to_string()
    print(a, "\t")
    print(b.to_string())

def close():
    
    connectionSocket.close()        #closing the socket connection with the current client




#creating a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#socket listening to incoming connection request
serverSocket.listen(1)
print('server started ')


while True:
        connectionSocket,addr = serverSocket.accept() #connection established
        a = connectionSocket.recv(1024).decode()    #field
        gameid = connectionSocket.recv(1024).decode() #recieving the data
        
        
        if (gameid) == 'type':
            option_a()
        elif (gameid) == "game_id":
            option_b()
        elif (gameid) == "home_team":
            option_c()
        elif (gameid) == "away_team":
            option_d()
        elif (gameid) == "week":
            option_e()
        elif (gameid) == "season":
            option_f()
        elif (gameid) == "home_score":
            option_g()
        elif (gameid) == "away_score":
            option_h()
        elif (gameid) == KeyboardInterrupt:
            close()
        
