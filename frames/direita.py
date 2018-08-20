from tkinter import *


class Right:
    def __init__(self, root):
        self.root = root

    def set_right(self):
        Right = Frame(self.root, width=250, height=750, bd=2, relief='raise')
        Right.pack(side=RIGHT)
        Right.configure(background='#A9A9A9')