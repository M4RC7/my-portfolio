import tkinter #requires specify that imported methods comes from this pack
#from tkinter import *
master = tkinter.Tk()

canvas_width = 80
canvas_height = 40
w = tkinter.Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042", width=2)
#variables in "create_line" are: (x_start, y_start, x_end, y_end, color, width)

master.mainloop()