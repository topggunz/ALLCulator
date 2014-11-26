"""Project PSIT Startup at 11/11/2557
Author :    Nathawut Worakijlawan 
            Amita Mongkhonpreedarchai
"""
from Tkinter import *
from urllib2 import urlopen
import urllib2
import wap
import tkMessageBox
import ttk
import io

try:
    from PIL import Image, ImageTk
    print 'Done'
    #msg2 = tkMessageBox('Done')
except:
    msg = tkMessageBox.showerror('Error!', 'You must install PIL')

class mainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        #menu bar
        self.master.title("All Math (Alltimate Math)")
        self.master.geometry("840x550")
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
        
        ####bymimimimi###

        #label for username
        self.username_input = StringVar()
        self.frame_username = ttk.LabelFrame(master, text='USER NAME',padding=5)
        self.frame_username.pack(padx=10, pady=10)   
        #self.frame_username.grid(row=0, column=0,padx=10, pady=10)      
        self.label_username_input = Entry(self.frame_username, width=20, textvariable = self.username_input)
        #self.label_username_input.grid(row=0, column=0)
        self.label_username_input.pack()

        #label for input
        self.text_input = StringVar()
        self.frame_input = ttk.LabelFrame(master, text='Enter what you want to calculate', padding=5)   
        self.frame_input.pack(padx=10, pady=10)     
        #self.frame_input.grid(row=1, column=0, padx=10, pady=10)
        self.label_frame_input = Entry(self.frame_input, width=79, textvariable = self.text_input)
        #self.label_frame_input.grid(row=1, column=0)
        self.label_frame_input.pack()
        
        #checkbutton for output
        self.option_frame = ttk.Labelframe(master, text='Select Output', padding=5)
        #self.option_frame.grid(row=2, column=0,)
        self.option_frame.pack(padx=5, pady=5)

        self.output_tp = [
        ("Input", "Input"),
        ("Graph", "Grap"),
        ("Equation", "Equ"),
        ("Solution", "Sol"),
        ("Integer Solution", "IS")   ]

        self.v = StringVar()
        self.v.set("Input") # initialize

        for text, val_output in self.output_tp:
            self.b = Radiobutton(self.option_frame, text=text, variable=self.v, value=val_output, command=self.cb_var)
            self.b.pack(padx=10, anchor=W)

        

        
        #button
        self.button_frame = Frame(master, height=2, bd=1, relief=SUNKEN)
        self.button_frame.pack(padx=5, pady=5)
        #self.button_frame.grid(row=3, column=0, padx=5, pady=5)
        self.b_submit = Button(self.button_frame, text="Submit", command=self.submit, padx=5, pady=2).pack(side=LEFT)
        self.b_reset = Button(self.button_frame, text="Reset", command=reset, padx=5, pady=2).pack(side=LEFT)

        #####combobox test
        # Label(master,text="Package:").pack(padx=2,pady=2)
        # package=StringVar()
        # pack=ttk.Combobox(master,width=10,state="readonly",values=['SIP','DIP','CONN-Dual','QUAD'],textvariable=package)
        # pack.current(0)
        # pack.pack()

        #To Generate the Content for the Picture Frame
        #canvas = Canvas(master,width=200,height=200,background="white" ,image=tk_image)
        #canvas.pack(fill=BOTH)

        image_bytes = urllib2.urlopen(
            "http://www.cuisinetoo.com/ill/brownies.jpg"
            ).read()
        data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        tk_image = ImageTk.PhotoImage(pil_image)
        label = Label(root, image=tk_image, bg='brown')
        #label.grid(row=0, column=1)#(padx=10, pady=20)


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
root.mainloop()
