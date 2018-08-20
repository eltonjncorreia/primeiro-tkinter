from tkinter import *


class Left:
    def __init__(self, root):
        self.root = root

    def set_left(self):
        Left = Frame(self.root, width=300, height=750, bd=2, relief='raise')
        Left.pack(side=LEFT)
        Left.configure(background='#A9A9A9')