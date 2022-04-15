# <<<<<<<<<<<<<<<<<[ Sliders in tkinter]>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("sliders in tkinter")


def getdollar():
    print(f"we have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo(
        "confirmation", f"we have credited {myslider2.get()} dollars to your bank account")


# myslider=Scale(root,from_=0,to=100)
# myslider.pack()
Label(root, text="how many dollars do you want??").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# note:-------------> tickinterval help us to get value in a particular interval
myslider2.set("34")
myslider2.pack()
Button(root, text="Get dollars", pady=10, command=getdollar).pack()
root.mainloop()
