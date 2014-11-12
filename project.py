"""Project PSIT Startup at 11/11/2557
Author : Nathawut Worakijlawan 
"""
from Tkinter import *

class mainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("MathPro Alpha Version (build 00011) **Name non official**")
        self.master.geometry("840x550")

        self.menubar = Menu(self, tearoff=False)
        self.filemenu = Menu(self.menubar, tearoff=False)

        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.filemenu, label="Options")
        self.menubar.add_cascade(menu=self.filemenu, label="Help")
        
        self.master.config(menu=self.menubar)
        self.pack()
        #bymimimimi
root = Tk()
windows = mainWindow(root)
root.mainloop()

