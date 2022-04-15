# <<<<<<<<<<<<<<<<<<<<<<<<[ frames in tkinter]>>>>>>>>>>>>>>>>>>>>>>
# from tkinter import *
# from PIL import Image,ImageTk

# sudeep_root=Tk()
# sudeep_root.geometry("665x333")
# sudeep_root.title("FRAMES")
# frame=Frame(sudeep_root,bg="yellow",borderwidth=12)
# frame.pack(side=LEFT)

# l=Label(frame,text="project tkinter")
# l.pack()
# sudeep_root.mainloop()



# <<<<<<<<<<<<<<<<<<<<<<<<[ basic project text editor]>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
from PIL import Image,ImageTk

sudeep_root=Tk()
sudeep_root.geometry("665x333")
sudeep_root.title("FRAMES")
frame=Frame(sudeep_root,bg="green",borderwidth=12,relief=SUNKEN)
frame.pack(side=LEFT,fill="y")

frame1=Frame(sudeep_root,borderwidth=15,bg="yellow",relief=SUNKEN)
frame1.pack(side=TOP,fill="x")

l=Label(frame,text="project tkinter-pycharm")
l.pack(pady=142)


l2=Label(frame1,text="welcome to vs code")
l2.pack(pady=142)



sudeep_root.mainloop()
