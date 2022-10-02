import tkinter

canvas_width = 190
canvas_height =150

master = tkinter.Tk()

w = tkinter.Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

w.create_oval(50,50,100,100)
#The coordinates are the locations of top left and bottom right edges of the rectangle in which the oval will be drawn inside of
master.mainloop()