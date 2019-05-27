import socket
import subprocess
import sys
import random
import string
import time
import os

key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase +
                            string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0,1024))
class xor:  
    def str_xor(self, s1, s2):
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])
    def encryption(self, message, key):
       
        enc = self.str_xor(message, key)
        file = open("Message.txt",'w')
        file.write(enc)
        file.close()
        return enc
    def decrypt(self, key, message):
        return self.str_xor(message, key)
    def __init__(self, choice, message):
        if choice == 'e' or choice == 'E':

            self.newMessage = self.encryption(message, key)
        if choice == 'd' or choice == 'D':
            keyThem = input("Enter key: ")
           
            
            self.dMessage = self.decrypt(keyThem, message)
            
def connect():
    
    s = socket.socket()
    choice = int(input("Enter port: "))
    s.bind(("192.168.200.208", choice))
    s.listen(1)
    conn, addr = s.accept()
    print("connection from: ", addr)
    while True:
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            
            sys.stdout.write("<You>")
            message = sys.stdin.readline()
        
            eMess = xor('e', message)
            sys.stdout.flush()
            
            conn.send(key.encode())
            conn.send(eMess.newMessage.encode())
            
            keyThem = conn.recv(1024)
            fileCreation(keyThem.decode())
            
            themMess = conn.recv(1024)
            sys.stdout.write("<Them>" + str(themMess.decode()))
            display = xor('d', themMess.decode())
            sys.stout.write("<Them>" + display.dMessage)
            
    s.close()

def fileCreation(text):
    keyF = open("key.txt", 'w')
    keyF.write(text)
    keyF.close()
    
def main():
    connect()
   
if __name__ == '__main__':
    main()



