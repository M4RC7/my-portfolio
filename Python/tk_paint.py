import tkinter

canvas_width = 500
canvas_height = 150

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

def press(event):
   print ("Pressed", repr(event.char))

def press_spec(event):
   print (repr(event.char))
#"event=None" grants nothing will disturb the binding input

#def loc(event):
#  x, y = event.x, event.y
#  print('{}, {}'.format(x, y))

#same as above, but more convenient
def loc(event):
   print(event.x, event.y)

def delete(event):
   w.delete("all")

master = tkinter.Tk()
master.title( "Painting using Ovals" )
w = tkinter.Canvas(master, width=canvas_width, height=canvas_height)
#w.focus_set()#if not set, key bindings to canvas only work after pressing Tab
w.pack()
w.bind( "<B1-Motion>", paint )
w.bind( "<Button-1>", paint )
w.bind( "<Button-2>", loc )
w.bind( "<Button-3>", delete )#always bind to a function or it won't work
#w.bind( "<Key>", press )
master.bind( "<Key>", press )#why didn't I think of that?
#w.bind( "r", press_spec )
master.bind( "r", press_spec )

message = tkinter.Label( master, text = "Press and Drag the mouse to draw. Middle click to track coords. Right click to clear." )
message.pack()
    
master.mainloop()

#"<Motion>"-> Mouse moving through widget
#"<B2-Motion>"-> Middle Mouse Button Held while moving
#"<B3-Motion>"-> Right Mouse Button while moving
#more at "tk_events.txt"