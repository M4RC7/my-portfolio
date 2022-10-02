#don't name your file "tkinter.py"
import tkinter as tk#does not work in Python 2
#"as tk" gives tkinter a nick
window = tk.Tk()#Tk() is the master window
window.title("Test")
label = tk.Label(text="Python rocks!")#Label is a wigdet
label.pack()#Geometry manager methods return none, so it's useful to not insert them in the same line of the object creation
#".pack()" places the object at the top-most available position in order by default
#If no geometry manager is specified, the object is not projected in window
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
#frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

#label.config(text= "should be easier")#Now it worked :)
#label["text"]= "should be easier2"#Also works like a charm :):)

window.mainloop()#grants the window will stay active
#more at <realpython.com/python-gui-tkinter>