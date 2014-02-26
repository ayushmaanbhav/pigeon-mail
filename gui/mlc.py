
import sys
import msg

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
    root.title('IITP Mail Client')
    root.geometry('600x450+419+180')
    w = New_Toplevel_1 (root)
    init()
    root.mainloop()

w = None
def create_New_Toplevel_1 (root):
    '''Starting point when module is imported by another program.'''
    global w, w_win
    if w: # So we have only one instance of window.
        return
    w = Toplevel (root)
    w.title('IITP Mail Client')
    w.geometry('600x450+419+180')
    w_win = New_Toplevel_1 (w)
    init()
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None




def init():
    pass




class New_Toplevel_1:
    def __init__(self, master=None):
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
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(background=_bgcolor)
        master.configure(highlightcolor="black")
	self.master=master


        self.TLabel1 = ttk.Label (master)
        self.TLabel1.place(relx=0.02,rely=0.02,height=23,width=84)
        self.TLabel1.configure(background=_bgcolor)
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(justify="center")
        self.TLabel1.configure(text='''To :''')

        self.TEntry1 = ttk.Entry (master)
        self.TEntry1.place(relx=0.17,rely=0.02,relheight=0.05,relwidth=0.81)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="xterm")

        self.TLabel2 = ttk.Label (master)
        self.TLabel2.place(relx=0.02,rely=0.09,height=23,width=84)
        self.TLabel2.configure(background=_bgcolor)
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(justify="center")
        self.TLabel2.configure(text='''From :''')

        self.TEntry2 = ttk.Entry (master)
        self.TEntry2.place(relx=0.17,rely=0.09,relheight=0.05,relwidth=0.81)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="xterm")

        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)



        self.TLabel3 = ttk.Label (master)
        self.TLabel3.place(relx=0.02,rely=0.15,height=23,width=84)
        self.TLabel3.configure(background=_bgcolor)
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(justify="center")
        self.TLabel3.configure(text='''Subject :''')

        self.TEntry3 = ttk.Entry (master)
        self.TEntry3.place(relx=0.17,rely=0.15,relheight=0.05,relwidth=0.81)
        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="xterm")

        self.TButton1 = ttk.Button (master)
        self.TButton1.place(relx=0.85,rely=0.92,height=22,width=74)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Send''')
	self.TButton1.configure(command=self.ft)

        self.Scrolledtext1 = ScrolledText (master)
        self.Scrolledtext1.place(relx=0.02,rely=0.22,relheight=0.69
                ,relwidth=0.96)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(width=10)

        self.Label1 = Label (master)
        self.Label1.place(relx=0.02,rely=0.93,height=15,width=89)
        self.Label1.configure(activebackground="#3d688e")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#ffffff")
        self.Label1.configure(text='''saswat raj''')

    def ft(self):
	fr = self.TEntry1.get()
	to = self.TEntry2.get()
	sub = self.TEntry3.get()
	message = self.Scrolledtext1.get('1.0',END)
	msg.create_New_Toplevel_1(self.master,fr,to,sub,message)
	


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


