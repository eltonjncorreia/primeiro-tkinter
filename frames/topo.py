from tkinter import *


class Top:
    def __init__(self, root):
        self.root = root

        self.top = Frame(self.root, width=1400, bd=1, relief='raise')
        self.top.pack(side=TOP)
        self.top.configure(background='#A9A9A9')

        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new_project)
        self.filemenu.add_command(label="Open", command=self.greet)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command=self.root.quit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.greet)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    def greet(self):
        print('Greetings')

    def new_project(self):
        root = Tk()
        root.geometry("400x200+500+100")
        root.title('New Project')
        root.configure(background='#696969')
        new_project = Frame(root, width=400, height=200, bd=1, relief='raise')
        new_project.pack(side=TOP)
        new_project.configure(background='#A9A9A9')





