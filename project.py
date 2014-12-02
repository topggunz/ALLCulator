"""Project PSIT Startup at 11/11/2557
Author :    Nathawut Worakijlawan 
            Amita Mongkhonpreedarchai
"""
import urllib,  urllib2, wap, tkMessageBox, ttk, io, base64

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

try:
    from PIL import Image, ImageTk
    print 'Done'
except:
    msg = tkMessageBox.showerror('Error!', 'You must install PIL')

class Windows(Frame):
    '''Create Main Windows'''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #menu bar
        self.master.title("AllCulator (build 1)")
        #self.master.geometry("550x550")
        self.menubar = Menu(self, tearoff=False)
        self.optionmenu = Menu(self.menubar, tearoff=0)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Save As...', command=saveimage)
        self.filemenu.add_command(label='Exit', command=quit)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=popup_about)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
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

    def cb_var(self):
        '''for get value to radiobutton'''
        index = self.v.get()
        return index

    def submit(self):
        '''get input'''   
        self.URL2 = mainConnect.call_api(self.text_input.get(), 'src')[self.cb_var()]
        self.text = mainConnect.call_api(self.text_input.get(), 'alt')[self.cb_var()]
        self.widgets_output(self.URL2, self.text)

    def widgets_input(self):
        '''Creat Input Widgets'''
        #label for username
        self.username_input = StringVar()
        self.frame_username = ttk.LabelFrame(self.data_frm1, text='USER NAME',padding=5)
        self.frame_username.grid(row=1, column=0, padx=10, pady=10, sticky=N+W)      
        self.label_username_input = Entry(self.frame_username, width=20, textvariable = self.username_input)
        self.label_username_input.grid(row=1, column=0, sticky=N+W)

        #label for input
        self.text_input = StringVar()
        self.frame_input = ttk.LabelFrame(self.data_frm1, text='Enter what you want to calculate', padding=5)
        self.frame_input.grid(row=2, column=0, padx=10, pady=10)
        self.label_frame_input = Entry(self.frame_input, width=59, textvariable = self.text_input)
        self.label_frame_input.grid(row=2, column=0)

        #button
        self.button_frame0 = Frame(self.data_frm1, height=2, bd=1, relief=SUNKEN)
        self.button_frame0.grid(row=8, column=0, padx=5, pady=5)
        self.b_genradio = Button(self.button_frame0, text="Submit", command=self.radiobutton, padx=5, pady=2).grid(column=0, row=0)
        
        #LOGO
        canvas = Canvas(self.content,width=300,height=80,background="Black" )
        canvas.grid(row=0, column=1)

    def radiobutton(self):
        '''Creat Radiobutton , SelectOutput Button and Reset Button'''
        #checkbutton for output
        self.option_frame = ttk.Labelframe(self.data_frm1, text='Select Output', padding=5)
        self.option_frame.grid(row=9, column=0, padx=5, pady=5)
        input = self.text_input.get()
        print 'equation', input
        self.pod = mainConnect.call_api(self.text_input.get(), 'pod') 
        self.output_tp = []
        count = 0
        for name in self.pod:
            self.output_tp.append((name,count))
            count += 1

        self.v = IntVar()
        self.v.set("Input") # initialize
        self.row = 0

        for text, val_output in self.output_tp:
            self.radio = Radiobutton(self.option_frame, text=text, variable=self.v, value=val_output)
            self.radio.grid(row=self.row, column=0, padx=10, sticky=W)
            self.row += 1

        self.button_frame = Frame(self.data_frm1, height=2, bd=1, relief=SUNKEN)
        self.button_frame.grid(row=10, column=0, padx=5, pady=5)
        self.b_submit = Button(self.button_frame, text="Select Output", command=self.submit, padx=5, pady=2).grid(column=0, row=0)
        self.b_reset = Button(self.button_frame, text="Reset", command=self.reset, padx=5, pady=2).grid(column=1, row=0)
 
    def widgets_output(self, url, text):
        '''To Generate the Content for the Picture Frame'''
        #Frame output'''
        self.note2 = ttk.Notebook(self.content,padding=2)
        #   URL from API       
        self.URL = url
        self.link = urllib.urlopen(self.URL)
        self.raw_data = self.link.read()
        self.link.close()
        next = base64.encodestring(self.raw_data)
        self.image = PhotoImage(data=next)
        self.data_frm2 = Label(self.content,width=300,height=270,borderwidth=3,\
                relief="ridge",padx=2,pady=2, image=self.image, bg='white')
        self.data_frm2.grid(column=0, row=1)
        self.entryvalue = StringVar()
        self.data_frm3 = LabelFrame(self.content,width=0,height=0,borderwidth=3,\
                relief="ridge",padx=2,pady=2, bg='white')
        self.data_frm3.grid(column=0, row=0)
        self.entry = Entry(self.data_frm3,width=0, textvariable = self.entryvalue, font='10')
        self.entryvalue.set(self.text)
        self.entry.grid(column=0, row=0)
        self.note2.add(self.data_frm2,text="Image Output",padding=5)
        self.note2.grid(column=1,row=0,rowspan=2,padx=5,pady=5)
        self.note2.add(self.data_frm3,text="Text Output",padding=5)
        self.note2.grid(column=1,row=1,rowspan=2,padx=5,pady=5)

    def reset(self):
        '''clear all of Entry and remove widgets output'''
        self.label_username_input.delete(0, END)
        self.label_frame_input.delete(0, END)
        self.ls_widgets = [self.note2, self.data_frm2, self.data_frm3, self.option_frame, self.button_frame]
        for wid in self.ls_widgets:
            wid.grid_remove()


class Connect(object):
    """Connecting the API libary"""
    def __init__(self):
        '''Check internet connection'''
        try:
            self.server = urllib2.urlopen('http://www.google.com')
        except:
            self.msg = tkMessageBox.showerror('Error!', 'Can\'t connect to Server.')
       
    def call_api(self, val, gett):
        '''call API from Wolfram Alpha and return output'''
        server = 'http://api.wolframalpha.com/v2/query.jsp'
        appid = '6LA36U-7V45PGUA6E'
        input = val
        waeo = wap.WolframAlphaEngine(appid, server)
        queryStr = waeo.CreateQuery(val)
        wap.WolframAlphaQuery(queryStr, appid)
        result = waeo.PerformQuery(queryStr)
        result = wap.WolframAlphaQueryResult(result)
        ls_alt, ls_src, ls_pod = [], [], []
        for pod in result.Pods():
                waPod = wap.Pod(pod)
                title = "Pod.title: " + waPod.Title()[0]
                ls_pod.append(waPod.Title()[0])
                for subpod in waPod.Subpods():
                        waSubpod = wap.Subpod(subpod)
                        plaintext = waSubpod.Plaintext()[0]
                        img = waSubpod.Img()
                        src = wap.scanbranches(img[0], 'src')[0]
                        alt = wap.scanbranches(img[0], 'alt')[0]
                        ls_src.append(src)
                        ls_alt.append(alt)
                        print "-------------"
                        print "img.src: " + src
                        print "img.alt: " + alt
                        ls_src = map(str, ls_src)
                        break
                print "\n"

        if gett == 'src':
            return ls_src
        elif gett == 'alt':
            return ls_alt
        elif gett == 'pod':
            return ls_pod


def popup_about():
    '''Creat Popup About'''
    top = Toplevel()
    top.title("About AllCulator")
    top.geometry("280x380")
    Label(text="one").pack()
    f = Frame(top, width=280,height=70,bg="lightgreen")
    f.grid(column=0,row=0,rowspan=1,padx=0,pady=0)
    
    about_message = ' +:+ AllCulator +:+ ' 
    msg = Message(f, text=about_message)
    msg.config(width=280, bg="lightgreen", font=('tahoma', 14, 'bold'))
    msg.place(x=35, y=15) 

    about_message2 = 'Build With WolframAlpha'
    msg2 = Message(top, text=about_message2)
    msg2.config(width=280, bg="lightgreen", font=('tahoma', 10))
    msg2.place(x=95, y=40)

    button = Button(top, text="Close!", command=top.destroy)
    button.place(x=125, y=350)
    top.resizable(width=FALSE, height=FALSE)
 


root = Tk()
windows = Windows(root)
mainConnect = Connect()
windows.mainloop()
