# <<<<<<<<<<<<<<<<<<<<[ packing buttons in tkinter]>>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("655x333")
def hello():
    print("hello kinter button")

def name():
    print("hello my name is sudeep")
frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame,fg="red",text="print_now",command=hello)
b1.pack(side=LEFT,padx=23)


b2=Button(frame,fg="red",text="tell me name now",command=name)
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg="red",text="print_now")
b3.pack(side=LEFT,padx=23)

b4=Button(frame,fg="red",text="print_now")
b4.pack(side=LEFT,padx=23)
root.mainloop()