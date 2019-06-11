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
import connectH
class mainHost:
    def mainHost():
        window = tk.Tk()
        window.title("Night Man")
        i = 1
        def click():       
            ip=userOption.get()
            port=userOptionP.get()

            service = connectH.connectH(ip, port)
            
            window.destroy()
            passWind()
            chatWind(service)     
            
            
        optOne = tk.Label (window, text = "Enter ip", bg="black",fg="green", font="none 12 bold") .grid(row=1,column=0)
        optTwo = tk.Label (window, text = "Enter port", bg="black",fg="green", font="none 12 bold") .grid(row=1,column=1)

        userOption = tk.Entry(window, width=20, bg="black", fg="green")
        userOption.grid(row=2, column=0)
        userOptionP = tk.Entry(window, width=20, bg="black", fg="green")
        userOptionP.grid(row=2, column=1)
        
        send = tk.Button(window, text="Send", width=6,command=click) .grid(row=3, column=0)
            
        window.mainloop()
    def __init__(self):
        mainHost.mainHost()

