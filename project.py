"""Project PSIT Startup at 11/11/2557
Author :    Nathawut Worakijlawan 
            Amita Mongkhonpreedarchai
"""
from Tkinter import *
import urllib2
import wap
import tkMessageBox
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
        self.frame_username = LabelFrame(master, text='USER NAME', padx=7, pady=5)
        self.frame_username.pack(padx=10, pady=10)      
        self.label_username_input = Entry(self.frame_username, width=40, textvariable = self.username_input)
        self.label_username_input.pack()

        #label for input
        self.text_input = StringVar()
        self.frame_input = LabelFrame(master, text='Enter what you want to calculate', padx=7, pady=5)        
        self.frame_input.pack(padx=10, pady=20)
        self.label_frame_input = Entry(self.frame_input, width=80, textvariable = self.text_input)
        self.label_frame_input.pack()
        
        #checkbutton for output
        self.option_frame = Frame(master, height=2, bd=1, relief=SUNKEN)
        self.option_frame.pack(padx=5, pady=5)

        self.var_in = IntVar()
        self.var_graph = IntVar()
        self.var_equa = IntVar()
        self.var_sol = IntVar()
        self.var_int_sol = IntVar()

        self.chck_input = Checkbutton(self.option_frame, text="Input", variable=self.var_in, command=self.cb_input)
        self.chck_input.pack(side=LEFT, padx=10)
        self.chck_graph = Checkbutton(self.option_frame, text="Graph", variable=self.var_graph, command=self.cb_graph)
        self.chck_graph.pack(side=LEFT, padx=10)
        self.chck_equa = Checkbutton(self.option_frame, text="Equation", variable=self.var_equa, command=self.cb_equa)
        self.chck_equa.pack(side=LEFT, padx=10)
        self.chck_sol = Checkbutton(self.option_frame, text="Solution", variable=self.var_sol, command=self.cb_sol)
        self.chck_sol.pack(side=LEFT, padx=10)
        self.chck_int_sol = Checkbutton(self.option_frame, text="Integer Solution", variable=self.var_int_sol, command=self.cb_int_sol)
        self.chck_int_sol.pack(side=LEFT, padx=10)

        
        #button
        self.button_frame = Frame(master, height=2, bd=1, relief=SUNKEN)
        self.button_frame.pack(padx=5, pady=5)
        self.b_submit = Button(self.button_frame, text="Submit", command=self.submit, padx=5, pady=2).pack(side=LEFT)
        self.b_reset = Button(self.button_frame, text="Reset", command=reset, padx=5, pady=2).pack(side=LEFT)

class Connect(object):
    """docstring for Connect"""
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

    
    #function with check button for output 
    #return 1 when check
    #return 0 when don't check
    def cb_input(self):
        print "variable1 is", self.var_in.get()

    def cb_graph(self):
        print "variable2 is", self.var_graph.get()

    def cb_equa(self):
        print "variable3 is", self.var_equa.get()

    def cb_sol(self):
        print "variable4 is", self.var_sol.get()

    def cb_int_sol(self):
        print "variable5 is", self.var_int_sol.get()


    def submit(self):
        '''get input'''
        input = self.username_input.get()
        print 'username', input
        input = self.text_input.get()
        print 'equation', input


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
