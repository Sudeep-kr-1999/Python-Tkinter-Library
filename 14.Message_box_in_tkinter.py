# <<<<<<<<<<<<<<<<<<<<<[ Messagebox in tkinter ]>>>>>>>>>>>>
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()


def rate():
    print("rate us")
    value = tmsg.askquestion(
        "was your experience good?", "how was your experience")
    # the reuturn value of "value"or "askquestion" here is yes or no as per the user choice
    print(value)
    if value == "yes":
        msg = "Great,Rate us on appstore please"
    else:
        msg = "Tell us what went wrong we will call you soon"

    tmsg.showinfo("experience", msg)


def help():
    print("i will help you")
    a = tmsg.showinfo("help", "i will help you with this gui")
    # note:--------------> the return value of a(showinfo) here is "ok"----(very very important)
    print(a)


def myfunc():
    print("i am very naughty")


def divya():
    ans = tmsg.askretrycancel("divya se dosti kr lo",
                              "sorry divya nhi banegi aapki dost")
    # note:--------> tmsg.askretrycancel()returns true or false
    print(ans)
    if ans:
        print("retry krne pe bhi kuch nhi hoga")
    else:
        print("bhut bhadiya bhai cancel kr diya wrna pitte")


root.geometry("733x566")
root.title("menus and submenus")


mainmenu = Menu(root)


m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)

m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)

m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="help", command=help)
m3.add_command(label="rate us", command=rate)
m3.add_command(label="befriend Divya", command=divya)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)
root.mainloop()
