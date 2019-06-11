import socket
import subprocess
import sys
import random
import string
import time
import os
import tkinter as tk
class connectU:
    def recieve(self):
        keyThem = self.s.recv(1024)
            
        keyF = open("Key.txt", 'w')
        keyF.write(keyThem.decode())
        print(keyThem.decode())
        keyF.close()
            #recieve the host message
        themMess= self.s.recv(1024)
        print(themMess.decode())
        return themMess.decode()
    def sendMess(self,object):
        self.s.send(object.key.encode())
        self.s.send(object.newMessage.encode())
        
    def __init__(self, ip, port, decrypt =''):
        print(ip + ' ' + port)
        #create new socket
        self.s = socket.socket()
        self.s.connect((ip, int(port)))
        #self.themMess = self.recieve
        print("connection from ip: " + ip)
