# <<<<<<<<<<<<<<<<<<[ Listbox in tkinter python]>>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("listbox in tkinter")


def add():
    global i
    # ACTIVE here means jo bhi list item selected h or active h uske upar jaakr add hote jaayega
    lbx.insert(ACTIVE, f"{i}")
    i += 1


i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "fist item of the listbox")
Button(root, text="Add Items", command=add).pack()


root.mainloop()
