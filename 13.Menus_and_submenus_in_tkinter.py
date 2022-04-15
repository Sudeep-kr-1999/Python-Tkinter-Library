# <<<<<<<<<<<<<<<<<<<<<<[ Menus and submenus in tkinter python]>>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
root = Tk()


def myfunc():
    print("i am very naughty")


root.geometry("733x566")
root.title("menus and submenus")


# use these to create a non dropdown menu
# mymenu=Menu(root)
# mymenu.add_command(label="file",command=myfunc)
# mymenu.add_command(label="Quit",command=quit)
# root.config(menu=mymenu)


#  use these to create a dropdown menu
mainmenu = Menu(root)

# tearoff----------> ye hum isliye use krte h kyuki agr hum chahe to submenu to utha kr khi aur shift kr sake agr tearff=0 hoga to ye shift nhi
#                    ho paayega......!


m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)

# add_seprator()-----------> ye submenus mein according to user region seprate krne ke kaam mein aata h 2 different menus region horizontal line
#                            se seprate ho jaate h
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)

# add_seprator()-----------> ye submenus mein according to user region seprate krne ke kaam mein aata h 2 different menus region horizontal line
#                            se seprate ho jaate h
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="Edit", menu=m2)

root.mainloop()
