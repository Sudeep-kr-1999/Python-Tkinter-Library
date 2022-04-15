from tkinter import *
sudeep_root=Tk()

# geometry has the order (width X height)....!!!!!!!!!!
sudeep_root.geometry("644x634")

# its takes argument like :---------> (width,height)
# it set the minimum size of the gui window...!!!!!!
sudeep_root.minsize(200,100)
sudeep_root.maxsize(1200,988)


# Label:------> it is a thing with with user donot interect............!!!!!!!!!!!!!!!!!!
label=Label(text="It is the label of the GUI")
label.pack()
sudeep_root.mainloop()