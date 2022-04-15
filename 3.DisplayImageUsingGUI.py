from tkinter import *

# pillow is a library in python which handle all types of images in tkinter library............!!!!!!!!!!
from PIL import Image,ImageTk
sudeep_root=Tk()

# image is the widgets by which user donot interact...............!!!!!!!!!
sudeep_root.geometry("455x254")

# this will show error sometimes!................
# photo=PhotoImage(file="mypic.png")

# better to use this for imgaes............!!!!!!!!!!
photo=ImageTk.PhotoImage(file="mypic.png")

# for jpg and also for any other type of images because tkinter donot support jpg image till now>>___!
# image=Image.open("mypic.png")
# photo=ImageTk.PhotoImage(image)


# note:---------> everytime we have to pack the label which we are creating............!!!!!!!!!!
label=Label(text="this is my photo",image=photo)
label.pack()

sudeep_root.mainloop()