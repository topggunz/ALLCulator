"""Project PSIT Startup at 11/11/2557
Author :    Nathawut Worakijlawan 
            Amita Mongkhonpreedarchai
"""
import io
import base64
try:
    # Python2
    from Tkinter import *
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    from tkinter import *
    import tkinter as tk
    from urllib.request import urlopen
import urllib
import urllib2
import wap
import tkMessageBox
import ttk


try:
    from PIL import Image, ImageTk
    print 'Done'
    #msg2 = tkMessageBox('Done')
except:
    msg = tkMessageBox.showerror('Error!', 'You must install PIL')

class mainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #menu bar
        self.master.title("All Math (Alltimate Math)")
        #self.master.geometry("550x550")
        self.menubar = Menu(self, tearoff=False)
        self.optionmenu = Menu(self.menubar, tearoff=0)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Save As...', command=saveimage)
        self.filemenu.add_command(label='Exit', command=quit)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=popup_about)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.optionmenu, label="Options")
        self.menubar.add_cascade(menu=self.helpmenu, label="Help")
        self.master.config(menu=self.menubar)
        self.pack()

        #Frame input
        self.content = Frame(master ,width=300,height=400,borderwidth=2,relief="groove")
        self.content.pack()
        self.note = ttk.Notebook(self.content,padding=2)
        self.data_frm1 = Frame(self.content,width=300,height=400,borderwidth=3,\
                relief="ridge",padx=2,pady=2)
        self.data_frm1.pack()
        self.note.add(self.data_frm1,text="Input Area",padding=5)
        self.note.grid(column=0,row=0,rowspan=2,padx=5,pady=5)
        self.widgets_input()

        #Frame output
        self.note2 = ttk.Notebook(self.content,padding=2)
        self.data_frm2 = Frame(self.content,width=300,height=230,borderwidth=3,\
                relief="ridge",padx=2,pady=2)
        self.data_frm2.pack()
        self.data_frm3 = Frame(self.content,width=200,height=150,borderwidth=3,\
                relief="ridge",padx=2,pady=2)
        self.data_frm3.pack()
        self.note2.add(self.data_frm2,text="Output Area",padding=5)
        self.note2.grid(column=1,row=0,rowspan=2,padx=5,pady=5)
        self.note2.add(self.data_frm3,text="Output Area2",padding=5)
        self.note2.grid(column=1,row=1,rowspan=2,padx=5,pady=5)

        #LOGO
        canvas = Canvas(self.content,width=300,height=80,background="Black" )
        canvas.grid(row=0, column=1)


                
    def cb_var(self):
        '''for get value to radiobutton'''
        print 'variable', self.v.get()


    def submit(self):
        '''get input'''
        input = self.username_input.get()
        print 'username', input
        input = self.text_input.get()
        print 'equation', input
        connect = mainConnect.cal_api(self.text_input.get())

    def widgets_input(self):
        #label for username
        self.username_input = StringVar()
        self.frame_username = ttk.LabelFrame(self.data_frm1, text='USER NAME',padding=5)
        #self.frame_username.pack(padx=10, pady=10)   <<<<<<< HEAD
        self.frame_username.grid(row=1, column=0, padx=10, pady=10, sticky=N+W)      
        self.label_username_input = Entry(self.frame_username, width=20, textvariable = self.username_input)
        self.label_username_input.grid(row=1, column=0, sticky=N+W)
        #self.label_username_input.pack()

        #label for input
        self.text_input = StringVar()
        self.frame_input = ttk.LabelFrame(self.data_frm1, text='Enter what you want to calculate', padding=5)   
        #self.frame_input.pack(padx=10, pady=10)     
        self.frame_input.grid(row=2, column=0, padx=10, pady=10)
        self.label_frame_input = Entry(self.frame_input, width=59, textvariable = self.text_input)
        self.label_frame_input.grid(row=2, column=0)
        #self.label_frame_input.pack()
        
        #checkbutton for output
        self.option_frame = ttk.Labelframe(self.data_frm1, text='Select Output', padding=5)
        self.option_frame.grid(row=3, column=0, padx=5, pady=5)
        #self.option_frame.pack(padx=5, pady=5)

        self.output_tp = [
        ("Input", "Input"),
        ("Graph", "Grap"),
        ("Equation", "Equ"),
        ("Solution", "Sol"),
        ("Integer Solution", "IS")   
        ]

        self.v = StringVar()
        self.v.set("Input") # initialize
        self.row = 4

        for text, val_output in self.output_tp:
            self.b = Radiobutton(self.option_frame, text=text, variable=self.v, value=val_output, command=self.cb_var)
            self.b.grid(row=self.row, column=0, padx=10, sticky=W)
            self.row += 1

        

        
        #button
        self.button_frame = Frame(self.data_frm1, height=2, bd=1, relief=SUNKEN)
        #self.button_frame.pack(padx=5, pady=5)
        self.button_frame.grid(row=8, column=0, padx=5, pady=5)
        self.b_submit = Button(self.button_frame, text="Submit", command=self.submit, padx=5, pady=2).pack(side=LEFT)
        self.b_reset = Button(self.button_frame, text="Reset", command=reset, padx=5, pady=2).pack(side=LEFT)

        # #####combobox test
        # # Label(master,text="Package:").pack(padx=2,pady=2)
        # # package=StringVar()
        # # pack=ttk.Combobox(master,width=10,state="readonly",values=['SIP','DIP','CONN-Dual','QUAD'],textvariable=package)
        # # pack.current(0)
        # # pack.pack()

        
    def widgets_output(self):
        #To Generate the Content for the Picture Frame
        canvas = Canvas(self.data_frm2,width=200,height=200,background="red" )
        canvas.grid(row=0, column=1)
            
        # image_bytes = urllib2.urlopen(
        #     "http://www.cuisinetoo.com/ill/brownies.jpg"
        #     ).read()
        # data_stream = io.BytesIO(image_bytes)
        # pil_image = Image.open(data_stream)
        # tk_image = ImageTk.PhotoImage(pil_image)
        # label = Label(root, image=tk_image, bg='brown')
        # label.grid(row=0, column=1)#(padx=10, pady=20)

class Connect(object):
    """Connecting the API libary"""
    def __init__(self):
        try:
            self.server = urllib2.urlopen('http://www.google.com')
            print 'Hello'
        except:
            self.msg = tkMessageBox.showerror('Error!', 'Can\'t connect to Server.')
       
    def cal_api(self, val):
        server = 'http://api.wolframalpha.com/v2/query.jsp'
        appid = '6LA36U-7V45PGUA6E'
        input = val
        waeo = wap.WolframAlphaEngine(appid, server)
        queryStr = waeo.CreateQuery(val)
        wap.WolframAlphaQuery(queryStr, appid)
        result = waeo.PerformQuery(queryStr)
        result = wap.WolframAlphaQueryResult(result)

        for pod in result.Pods():
                waPod = wap.Pod(pod)
                title = "Pod.title: " + waPod.Title()[0]
                print title
                for subpod in waPod.Subpods():
                        waSubpod = wap.Subpod(subpod)
                        plaintext = waSubpod.Plaintext()[0]
                        img = waSubpod.Img()
                        src = wap.scanbranches(img[0], 'src')[0]
                        alt = wap.scanbranches(img[0], 'alt')[0]
                        print "-------------"
                        print "img.src: " + src
                        print "img.alt: " + alt
                print "\n"


def reset():
    '''for reset button'''
    print 'Reset'

def saveimage():
    '''for save as on file.menubar'''
    print 'saveimage'

def popup_about():
    '''popup in help on menubar'''
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
mainConnect = Connect()
windows.mainloop()
