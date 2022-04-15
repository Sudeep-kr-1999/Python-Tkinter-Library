# <<<<<<<<<<<<<<<<<<<<<[travel form using checkbuttons and entry widgets]>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
root=Tk()

def getvals():
    print("it works")
root.geometry("644x344")
Label(root,text="Welcome to Sudeep Travels",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emergencycontact=Label(root,text="emergency contact")
payment=Label(root,text="payment mode")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergencycontact.grid(row=4,column=2)
payment.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentvalue=StringVar()

foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymententry=Entry(root,textvariable=paymentvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

foodservice=Checkbutton(text="Want to prebook meals",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

Button(text="submit",command=getvals).grid(row=7,column=3)

root.mainloop()