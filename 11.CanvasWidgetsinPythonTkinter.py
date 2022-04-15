# <<<<<<<<<<<<<<<<<<[Canvas widgets in python tkinter]>>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
root=Tk()
root.title("gui with me")
canvas_width=880
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

#the line goes from the point x1,y1 to x2,y2

can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

# top-left coordinates and bottom-right coordinates is the order to create the rectangle in GUI
can_widget.create_rectangle(3,5,700,300,fill="green")

# centre coordinate of the text under the create text
can_widget.create_text(200,200,text="python")

# it take coordinate of the rectangle inside which the oval is printed!
can_widget.create_oval(3,5,700,300,fill="red")

# oval ko circle mein convert krne ke liye rectangle ke jagh square le skte h!!!!!!!!!!!!!!!
root.mainloop()
