import tkinter #there is no "Tkinter" with capital 'T' in Python 3
#keep an eye out for that when looking for tutorials
top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)
#variables in "Canvas" are: (orientation, background color, height, width)

coord = 10, 50, 190, 230
arc = C.create_arc(coord, start=0, extent=270, width=3, outline="brown", fill="red")
#variables in "create_arc" are: (x_topleft, y_topleft, x_bottomright, y_bottomright*, arc_start, arc_extent, color)
#*The coordinates are the locations of top left and bottom right edges of the rectangle in which the arc will be drawn inside of
C.pack()
top.mainloop()