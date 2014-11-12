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
        #self.menubar.add_command(menu=, label="")
        self.master.config(menu=self.menubar)
        self.pack()
        
        #bymimimimi
        frame_input = LabelFrame(root, text='Enter what you want to calculate                                                 ', padx=5, pady=2)
        label_frame_input = Entry(frame_input)
        frame_input.pack(padx=10, pady=10, anchor=NW)
        label_frame_input.pack(fill=BOTH, anchor=NW)
        

        self.var_in = IntVar()
        self.var_graph = IntVar()
        self.var_equa = IntVar()
        self.var_sol = IntVar()
        self.var_int_sol = IntVar()

        chck_input = Checkbutton(master, text="Input", variable=self.var_in, command=self.cb_input)
        chck_input.pack(anchor=NW)
        chck_graph = Checkbutton(master, text="Graph", variable=self.var_graph, command=self.cb_graph)
        chck_graph.pack(anchor=NW)
        chck_equa = Checkbutton(master, text="Equation", variable=self.var_equa, command=self.cb_equa)
        chck_equa.pack(anchor=NW)
        chck_sol = Checkbutton(master, text="Solution", variable=self.var_sol, command=self.cb_sol)
        chck_sol.pack(anchor=NW)
        chck_int_sol = Checkbutton(master, text="Integer Solution", variable=self.var_int_sol, command=self.cb_int_sol)
        chck_int_sol.pack(anchor=NW)

        b_submit = Button(master, text="Submit", command=submit, padx=5, pady=2)
        b_submit.pack()

    def cb_input(self):
        print "variable1 is", self.var_in.get()
    def cb_graph(self):
        print "variable2 is", self.var_graph.get()
    def cb_equa(self):
        print "variable3 is", self.var_equa.get()
    def cb_sol(self):
        print "variable4 is", self.var_sol.get()
    def cb_int_sol(self):
        print "variable5 is", var_int_sol.get()

def submit():
    print 'Submit'

root = Tk()
windows = mainWindow(root)
root.mainloop()

#dssdafddfds