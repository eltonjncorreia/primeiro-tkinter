from tkinter import *


class Top:
    def __init__(self, root):
        self.root = root

        self.top = Frame(self.root, width=1400, bd=1, relief='raise')
        self.top.pack(side=TOP)
        self.top.configure(background='#A9A9A9')

        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.greet)
        self.filemenu.add_command(label="Open", command=self.greet)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command=self.root.quit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.greet)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar, width=200)

    def greet(self):
        print('Greetings')


