import socket
import subprocess
import sys
import random
import string
import time
import os
#generate key
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase +
                            string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0,1024))
class xor:
    #xor the message typed
    def str_xor(self, s1, s2):
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])
    #start xor encryption based on key
    def encryption(self, message, key):     
        enc = self.str_xor(message, key)
        return enc
    #decrypt message
    def decrypt(self, key, message):
        return self.str_xor(message, key)
    #create new key based changing individual characters
    def tumblur(self, key):
        keyList = list(key)
        random.seed()
        runThrough = random.random() * 1024
        for i in range(0, int(runThrough)):
            pos = int(random.random() * 1024)
            keyList[pos] = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\')
        newKey = ""
        for i in range(0, len(keyList)):
            newKey += keyList[i]
        return newKey
    #when xor() is called decide wether to encrypt or decrypt    
    def __init__(self, choice, message):    
        if choice == 'e' or choice == 'E':
            self.newMessage = self.encryption(message, key)
        if choice == 'd' or choice == 'D':
            #ask for key
            keyThem = input("Enter key: ")
            self.dMessage = self.decrypt(keyThem, message)
        #generate new key        
        key = self.tumblur(key)
            
#allow user to connect to host
def connect(ip, port):
    #create new socket
    s = socket.socket()
    s.connect((ip, int(port)))
    
    print("connection from ip: " + ip)
    
    while True:
        time.sleep(2)
        #clear the screen from who user connected to
        os.system('cls')
        #recieve key from host for their messages
        keyThem = s.recv(1024)
        
        keyF = open("Key.txt", 'w')
        keyF.write(keyThem.decode())
        keyF.close()
        #recieve the host message
        themMess= s.recv(1024)
        
        if 'terminate' in themMess.decode():
            s.close()
            break
        else:
            #display 'chat room'
            print("<them>" + themMess.decode() + '\n')
            display =  xor('d', themMess.decode())
            
            print("<them>" + display.dMessage)
            
            sys.stdout.write("<You>")
            
            message = sys.stdin.readline()
            #encrypt your message
            eMess = xor('e', message)
            #send that message to host
            s.send(key.encode())
            s.send(eMess.newMessage.encode())         
            sys.stdout.flush()
            

    s.close()
    
def main():
    userOption = input("Enter ip address: ")
    port = input("Enter port: ")
    connect(userOption, port)
    
    
if __name__ == '__main__':
    main()
