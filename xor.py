import socket
import subprocess
import sys
import random
import string
import time
import os
class xor:
    key = ''
    for x in range(0,1024):
        ch = random.choice(string.ascii_lowercase + string.ascii_uppercase +
                            string.digits + '^!$%&/()=?{[]}+~#-_.:,;<>|')
        while ch == '\\':
            ch = random.choice(string.ascii_lowercase + string.ascii_uppercase +
                            string.digits + '^!$%&/()=?{[]}+~#-_.:,;<>|')
        
        key = key + ch
        
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
            keyList[pos] = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!$%&/()=?{[]}+~#-_.:,;<>|')
        newKey = ""
        for i in range(0, len(keyList)):
            newKey += keyList[i]
        return newKey
    #when xor() is called decide wether to encrypt or decrypt    
    def __init__(self, choice, message, keyThem =''):
       
        if choice == 'e' or choice == 'E':
            self.newMessage = self.encryption(message, xor.key)
   
        if choice == 'd' or choice == 'D':
            #ask for key
            self.dMessage = self.decrypt(keyThem, message)
        #generate new key        
        #self.key = self.tumblur(self.key)
