from Tkinter import *
import ttk
root = Tk()

root.title("Kicad Module Generator v"\
         " by A.D.H.A.R Labs Research,Bharat(India) ")  
root.bind("<Escape>",lambda e:root.destroy())
root["padx"]=10
root["pady"]=10

content = Frame(root,width=300,height=200,borderwidth=2,relief="groove")

note = ttk.Notebook(content,padding=2)
data_frm1 = Frame(note,width=300,height=400,borderwidth=3,\
                relief="ridge",padx=2,pady=2)

note.add(data_frm1,text="Input Area",padding=5)
note.grid(column=0,row=0,rowspan=2,padx=5,pady=5)

data_frm2 = Frame(content,width=300,height=200,borderwidth=3,\
                relief="ridge",padx=2,pady=2)

data_frm2.grid(column=1,row=0,padx=5,pady=5,sticky=N+W+E+S)

data_frm3 = Frame(content,width=200,height=200,borderwidth=3,\
                relief="ridge",padx=2,pady=2)

data_frm3.grid(column=1,row=1,padx=5,pady=5,sticky=N+W+E+S)

data_frm4 = Frame(content,padx=2,pady=2)

data_frm4.grid(column=0,row=2,columnspan=2,padx=5,pady=5,sticky=N+W+E+S)

content.grid(column=0,row=0,sticky=N+S+E+W)


root.mainloop()
