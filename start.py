import tkinter as tk
import socket
import subprocess
import sys
import random
import string
import time
import os
import tkinter as tk
import ChatWind as chatWind
import xor
import connectU
import user, server

class start:
    def clickU(self):
        user.mainUser()
        self.root.destroy()
    def clickH(self):
        server.mainHost()
        self.root.destroy()
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Night Main")
        self.user = tk.Button(self.root, text="user", width=6,command=self.clickU)
        self.user.grid(row=0,column=0)
        self.host = tk.Button(self.root, text="host", width=6,command=self.clickH) 
        self.host.grid(row=0,column=1)
        
        self.root.mainloop()
def main1():
    start()
if __name__ == '__main__':
    main1()
