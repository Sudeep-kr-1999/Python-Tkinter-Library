# <<<<<<<<<<<<<<<<<<<<<<<<<<<<[ Entry widgets and grid layout]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from tkinter import *
from PIL import Image,ImageTk
root=Tk()

def getvals():
    print("The value of username is : ",uservalue.get())
    print("The value of paasword  is : ",passvalue.get())

    # fstring method
    print(f"The value of username is : {uservalue.get()}")
    print(f"The value of paasword  is : {passvalue.get()}")


root.geometry("600x300")
label_1=Label(root,text="user_name")
label_2=Label(root,text="paasword")
label_1.grid()
label_2.grid()

# variable classes in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
paasentry=Entry(root,textvariable=passvalue)
paasentry.grid(row=1,column=1)
userentry.grid(row=0,column=1)


Button(text="submit",command=getvals).grid()


root.mainloop()