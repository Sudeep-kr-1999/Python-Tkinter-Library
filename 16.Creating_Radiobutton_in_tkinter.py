# <<<<<<<<<<<<<<<<<<<<[ Radio button on tkinter]>>>>>>>>>>>>>>>>>
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("radiobutton in tkinter")
# var=IntVar()
var=StringVar()

# note:------------->kuch bhi value set kr skte h takki radiobutton already selected na ho
var.set("Radio")

def order():
    tmsg.showinfo(
        "confirmation", f"we have recieved your order {var.get()} for this")

Label(root,text="what would you like to have sir?",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack()
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack()
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value="Paratha").pack()
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack()
Button(root,text="Order now",command=order).pack()
root.mainloop()