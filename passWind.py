import socket
import subprocess
import sys
import random
import string
import time
import os
import tkinter as tk
class passWind:
    access = False
    def storePass(self):
        global password
        password = self.newPass.get()
        self.root.destroy()
    def checkPass(self):
        
        if self.newCheck.get() == password:
            passWind.access = True
            self.root1.destroy()
        else:
            self.root1.destroy()
            passWind(2)
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password")
        self.newPass = tk.Entry(self.root, width = 9, bg = "black", fg = "green", show = '*')
        self.newPass.grid(row=0, column=1)
        self.set = tk.Button(self.root, text="Set", width=6,command= self.storePass)
        self.set.grid(row=0, column=0)
        self.root.mainloop()
