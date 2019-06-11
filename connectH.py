import socket
import subprocess
import sys
import random
import string
import time
import os
import tkinter as tk

class connectH:
    def recieve(self):
        keyThem = self.conn.recv(1024)
           
        keyF = open("Key.txt", 'w')
        keyF.write(keyThem.decode())
        keyF.close()
            #recieve the host message
        themMess= self.conn.recv(1024)
        return themMess.decode()
    def sendMess(self,object):

        self.conn.send(object.key.encode())
        self.conn.send(object.newMessage.encode())
       
    def __init__(self, ip, port, decrypt =''):

        #create new socket
        self.s = socket.socket()
        self.s.bind((ip, int(port)))
        self.s.listen(1)
        self.conn, addr = self.s.accept()
    
        print("connection from ip: " + ip)
   
