#import tkinter #see "tk_linespec.py"
from tkinter import * #dismisses the specification requirement
#for also importing the namespace (disencouraged)
master = Tk()

canvas_width = 80
canvas_height = 40
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042", width=2)
#variables in "create_line" are: (x_start, y_start, x_end, y_end, color, width)

mainloop() #"from tkinter import *" dismissies allocating this to master