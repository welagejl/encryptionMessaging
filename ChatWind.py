import socket
import subprocess
import sys
import random
import string
import os
import xor
import passWind
import tkinter as tk

class chatWind:

    def clickMess(self, object):
        self.newmessage = self.messages.get("1.0", "end-1c")
        mess = xor.xor('e', self.newmessage)
        object.sendMess(mess)

    def clickKeyRes(self, message):
        check = self.check.get()
        if check == passWind.password:
            self.key = self.keyEntry.get("1.0", "end-1c")
            decMess = xor.xor('d', message, keyThem= self.key)
            return decMess.dMessage
        else:
            self.them.delete("1.0", tk.END)
            self.them.insert("1.0", "Message loss due to incorret password.")
            return

    def updateThem(self, object):
        self.them.delete("1.0", "end-1c")
        self.keyEntry.delete("1.0", "end-1c")
        try:
            self.them.insert("1.0",object.recieve())
        except:
            return
        
    def updateThemD(self):
        
        self.message= self.clickKeyRes(self.them.get('1.0', 'end-1c'))
        self.them.delete("1.0", tk.END)
        self.them.insert("1.0", self.message)
    def terminate(self, object):
        object.s.close()
        self.root.destroy()
        
    def __init__ (self, service = object):
        self.root = tk.Tk()

        self.root.title("Night Man U")
        self.root.configure(bg = "black")

        self.them = tk.Label(self.root, text = "<Them>", bg="black",fg="green")
        self.them.grid(row=0,column=0)

        self.them = tk.Text(self.root,height=10, width=10, bg="black",fg="green", wrap = tk.WORD)
        self.them.grid(row=0,column=1)

        
        self.labelK = tk.Label(self.root, text = "<Key>", bg="black",fg="green")
        self.labelK.grid(row=1,column=0)
        
        self.keyEntry = tk.Text(self.root, height =10, width=10, bg="black",fg="green", wrap = tk.CHAR)
        self.keyEntry.grid(row=1,column=1)
        
        self.you = tk.Label(self.root, text = "<You>", bg="black",fg="green")
        self.you.grid(row=1,column=3)
           
        self.messages = tk.Text(self.root, height = 10, width=10, bg="black", fg="green")
        self.messages.grid(row=1,column=4)

        send = tk.Button(self.root, text="Send", width=6,command= lambda: self.clickMess(service))
        send.grid(row=2, column=0)
        
        self.decrypt = tk.Button(self.root, text="Decrypt", width=6,command=self.updateThemD)
        self.decrypt.grid(row=2, column=1)

        refre = tk.Button(self.root, text="Refresh", width=6,command= lambda: self.updateThem(service))
        refre.grid(row=3, column=0)
        
        self.checkBox= tk.Label(self.root, text = "<Password>", bg="black",fg="green")
        self.checkBox.grid(row=3,column=1)

        self.check = tk.Entry(self.root, width=12, bg="black", fg="green", show = '*')
        self.check.grid(row=3,column=2)


        self.root.bind('<Control-e>',lambda event: self.terminate(service))
                           
        self.root.mainloop()
