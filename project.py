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




class Connect(object):
    """Connecting the API libary"""
    def __init__(self):
        '''Check internet connection'''
        self.ls_src=[]
        self.ls_alt=[]
        self.ls_pod=[]
        try:
            self.server = urllib2.urlopen('http://www.google.com')
        except:
            self.msg = tkMessageBox.showerror('Error!', 'Can\'t connect to Server.')
       
    def call_api(self, val):
        '''call API from Wolfram Alpha and return output'''
        server = 'http://api.wolframalpha.com/v2/query.jsp'
        appid = '6LA36U-7V45PGUA6E'
        input = val
        waeo = wap.WolframAlphaEngine(appid, server)
        queryStr = waeo.CreateQuery(val)
        wap.WolframAlphaQuery(queryStr, appid)
        result = waeo.PerformQuery(queryStr)
        result = wap.WolframAlphaQueryResult(result)
        self.ls_src=[]
        self.ls_alt=[]
        self.ls_pod=[]

        for pod in result.Pods():
                waPod = wap.Pod(pod)
                title = "Pod.title: " + waPod.Title()[0]
                self.ls_pod.append(waPod.Title()[0])
                for subpod in waPod.Subpods():
                        waSubpod = wap.Subpod(subpod)
                        plaintext = waSubpod.Plaintext()[0]
                        img = waSubpod.Img()
                        src = wap.scanbranches(img[0], 'src')[0]
                        alt = wap.scanbranches(img[0], 'alt')[0]
                        self.ls_src.append(src)
                        self.ls_alt.append(alt)
                        print "-------------"
                        print "img.src: " + src
                        print "img.alt: " + alt
                        self.ls_src = map(str, self.ls_src)
                        break
                print "\n"
        return self.ls_pod


class Windows(Frame):
    '''Create Main Windows'''
    global conn
    conn = Connect()
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #menu bar
        self.master.title("AllCulator (build 1)")
        self.menubar = Menu(self, tearoff=False)
        self.optionmenu = Menu(self.menubar, tearoff=0)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='History', command=history)
        self.filemenu.add_command(label='Save As...', command=saveimage)
        self.filemenu.add_command(label='Exit', command=quit)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=popup_about)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.helpmenu, label="Help")
        self.master.config(menu=self.menubar)
        self.grid(column=0, row=0)
        #content
        self.content = Frame(master, borderwidth=2, relief="groove")
        self.content.grid(column=0, row=0)
        #LOGO
        canvas = Canvas(self.content,width=300,height=80,background="Black" )
        canvas.grid(column=1, row=0, padx=10)
        #Input Area
        self.note = ttk.Notebook(self.content,padding=2)
        self.data_frm1 = Frame(self.content,width=300,height=400,borderwidth=3,\
                relief="ridge",padx=2,pady=2)
        self.data_frm1.grid(column=0, row=0)
        self.note.add(self.data_frm1,text="Input Area",padding=5)
        self.note.grid(column=0, row=0, rowspan=2, padx=5, pady=5)
        #-label for username
        self.username_input = StringVar()
        self.frame_username = ttk.LabelFrame(self.data_frm1, text='USER NAME',padding=5)
        self.frame_username.grid(column=0, row=0, padx=10, pady=10, sticky=N+W)      
        self.label_username_input = Entry(self.frame_username, width=20, textvariable = self.username_input)
        self.label_username_input.grid(column=0, row=0, sticky=N+W)
        #-label for input
        self.text_input = StringVar()
        self.frame_input = ttk.LabelFrame(self.data_frm1, text='Enter what you want to calculate', padding=5)
        self.frame_input.grid(column=0, row=1, padx=10, pady=10)
        self.label_frame_input = Entry(self.frame_input, width=59, textvariable = self.text_input)
        self.label_frame_input.grid(column=0, row=0)
        #-button
        self.button_frame0 = Frame(self.data_frm1, bd=1, relief=SUNKEN)
        self.button_frame0.grid(column=0, row=2, padx=5, pady=5)
        self.b_genradio = Button(self.button_frame0, text="Submit", padx=5, pady=2, command=self.radiobutton)# 
        self.b_genradio.grid(column=0, row=0)
        
        self.dic_hist = {}
        self.storage = []


    def select_output(self):
        '''get input and show output'''
        index = self.v.get()
        self.URL2 = conn.ls_src[index]
        self.text = conn.ls_alt[index]
        if 'widgets' in self.storage:
            self.ls_widgets0 = [self.note2, self.data_frm2, self.data_frm3]
            for wid in self.ls_widgets0:
                wid.grid_remove()
        self.widgets_output(self.URL2, self.text)

    def radiobutton(self):
        '''Creat Radiobutton , SelectOutput Button and Reset Button'''
        if 'radio' in self.storage:
            self.ls_widgets1 = [self.option_frame, self.button_frame]
            for wid in self.ls_widgets1:
                wid.grid_remove()

        #checkbutton for output
        self.option_frame = ttk.Labelframe(self.data_frm1, text='Select Output', padding=5)
        self.option_frame.grid(column=0, row=3, padx=5, pady=5)
        #generate from API
        input = self.username_input.get()
        print 'username', input
        self.user = input
        print self.user


        input = self.text_input.get()
        print 'equation', input
        self.equa = input
        print self.equa

        if self.equa == '':
            tkMessageBox.showerror('Error','Please Enter Input')
        else:
            if self.user not in self.dic_hist:
                self.ls_equa = []
                self.ls_equa.append(self.equa)
                self.dic_hist[self.user] = self.ls_equa
            else:
                self.dic_hist[self.user].append(self.equa)
            print 'dic_hist', self.dic_hist

            self.pod = conn.call_api(self.text_input.get()) 
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
            self.button_frame.grid(column=0, row=5, padx=5, pady=5)
            self.b_select_output = Button(self.button_frame, text="Select Output", command=self.select_output, padx=5, pady=2)
            self.b_select_output.grid(column=0, row=0)
            self.b_reset = Button(self.button_frame, text="Reset", command=self.reset, padx=5, pady=2)
            self.b_reset.grid(column=1, row=0)
            self.storage.append('radio')
 
    def widgets_output(self, url, text):
        '''To Generate the Content for the Picture Frame'''
        #Frame output'''
        self.note2 = ttk.Notebook(self.content, padding=2)
         #   URL from API       
        self.URL = url
        self.link = urllib.urlopen(self.URL)
        self.raw_data = self.link.read()
        self.link.close()
        next = base64.encodestring(self.raw_data)
        self.image = PhotoImage(data=next)
        #widgets
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

        self.storage.append('widgets')

    def reset(self):
        '''clear all of Entry and remove widgets output'''
        self.label_username_input.delete(0, END)
        self.label_frame_input.delete(0, END)
        self.ls_widgets2 = [self.option_frame, self.button_frame]
        self.ls_widgets3 = []
        if 'widgets' in self.storage:
            self.ls_widgets3 = [self.note2, self.data_frm2, self.data_frm3]
        for i in self.ls_widgets3:
            self.ls_widgets2.append(i)
        for wid in self.ls_widgets2:
            wid.grid_remove()

def popup_about():
    '''Creat Popup About'''
    top = Toplevel()
    top.title("About AllCulator")
    top.geometry("280x380")
    f = Frame(top, width=280,height=70,bg="lightgreen")
    f.grid(column=0,row=0,rowspan=1,padx=0,pady=0)
    
    about_message = ' +:+ AllCulator +:+ ' 
    msg = Message(f, text=about_message)
    msg.config(width=280, bg="lightgreen", font=('tahoma', 14, 'bold'))
    msg.place(x=35, y=15) 

    about_message2 = 'The Mighty of Calculater for everything'
    msg2 = Message(top, text=about_message2)
    msg2.config(width=280, bg="lightgreen", font=('tahoma', 10))
    msg2.place(x=20, y=40)

    about_message3 = 'Amita Mongkhonpreedarchai'
    msg3 = Message(top, text=about_message3)
    msg3.config(width=280)
    msg3.place(x=5, y=80)

    about_message4 = 'Nathawut Worakijlawan'
    msg3 = Message(top, text=about_message4)
    msg3.config(width=280)
    msg3.place(x=5, y=100)

    about_message5 = 'Spacial Thank : WolframAlpha'
    msg3 = Message(top, text=about_message5)
    msg3.config(width=280)
    msg3.place(x=100, y=320)


    button = Button(top, text="Close!", command=top.destroy)
    button.place(x=120, y=350)
    top.resizable(width=FALSE, height=FALSE)
 

def saveimage():
    pass
def history():
    pass
root = Tk()
windows = Windows(root)
windows.mainloop()
