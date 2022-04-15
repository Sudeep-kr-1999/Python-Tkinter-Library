# <<<<<<<<<<<<<<<<<<<<<<[ statusbar using tkinter in python]>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
import tkinter
root = Tk()
root.geometry("455x233")
root.title("statusbar in tkinter")


def upload():
    statusvar.set("busy...")
    sbar.update()

    # agar hum sbar.update() use nhi krege to wo function ke andar ka activity ko tkinter show nhi krega direct return value show krega
    # andar ke activity ko show krne ko hum sbar.update() use krege....................!
    import time
    time.sleep(2)
    statusvar.set("Ready Now")


statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()

root.mainloop()
