from tkinter import *
from frames.esquerda import Left
from frames.direita import Right
from frames.topo import Top


root = Tk()

root.geometry("1400x700")
root.title('IDE Deapy')
root.configure(background='#696969')

top = Top(root)

Left(root).set_left()

Right(root).set_right()

root.mainloop()