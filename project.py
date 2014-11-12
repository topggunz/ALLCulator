"""Project PSIT Startup at 11/11/2557
Author : Nathawut Worakijlawan 
"""
from tkinter import *

class mainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("MathPro Alpha Version (build 00011) **Name non official**")
        self.master.geometry("840x550")

        self.menubar = Menu(self, tearoff=False)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=popup_about)

        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.filemenu, label="Options")
        self.menubar.add_cascade(menu=self.helpmenu, label="Help")
        
        self.master.config(menu=self.menubar)
        self.pack()
        
def popup_about():
    top = Toplevel()
    top.title("About MathPro")
    top.geometry("250x300")

    about_message = 'Hello World'

    msg = Message(top, text=about_message)
    msg.pack()

    button = Button(top, text="Close", command=top.destroy)
    button.pack()   

root = Tk()
windows = mainWindow(root)
root.mainloop()

