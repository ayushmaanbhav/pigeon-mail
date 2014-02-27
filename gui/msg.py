
import sys
import pigeon

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Sending...')
    root.geometry('319x432+650+150')
    w = New_Toplevel_1 (root)
    init()
    root.mainloop()

w = None
def create_New_Toplevel_1 (root,fr,to,sub,message):
    '''Starting point when module is imported by another program.'''
    global w, w_win
    if w: # So we have only one instance of window.
        return
    w = Toplevel (root)
    w.title('Sending...')
    w.geometry('319x432+650+150')
    w_win = New_Toplevel_1 (fr,to,sub,message,w)
    init()
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None




def init():
    pass




class New_Toplevel_1:
    def __init__(self,fr,to,sub,message,master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])


        self.Label1 = Label (master)
        self.Label1.place(relx=0.03,rely=0.02,height=15,width=299)
        self.Label1.configure(text='''Messages ''')
        self.Label1.configure(width=299)

        self.Scrolledtext1 = ScrolledText (master)
        self.Scrolledtext1.place(relx=0.02,rely=0.08,relheight=0.83
                ,relwidth=0.96)
        self.Scrolledtext1.configure(background="#020202")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="#43e043")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(width=10)

        self.Button1 = Button (master)
        self.Button1.place(relx=0.38,rely=0.93,height=23,width=68)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Close''')
	self.Button1.configure(command=w.destroy)
	
	st=pigeon.pigeon("172.16.1.138")
	self.Scrolledtext1.insert(END,st)
	st = pigeon.sayHello("iitp.ac.in")
	self.Scrolledtext1.insert(END,st)
	st = pigeon.msgFrom(fr)
	self.Scrolledtext1.insert(END,st)
	st = pigeon.rcptTo(to)
	self.Scrolledtext1.insert(END,st)
	pigeon.beginData()
	line = "subject:"+sub+"\n"
	pigeon.writeData(line)
	pigeon.writeData(message)
	st = pigeon.sendMsg()
	self.Scrolledtext1.insert(END,st)
	st = "Message sent.\n"
	self.Scrolledtext1.insert(END,st)



# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        self.configure(yscrollcommand=self._autoscroll(vsb),
            xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (took from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()


