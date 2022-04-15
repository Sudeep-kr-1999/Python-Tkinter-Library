# <<<<<<<<<<<<<<<<<<<<<<<<[ MORE ON TKINTER]>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("more in tkinter")

# to change the inbuilt feather icon of the gui window
root.wm_iconbitmap("download.ico")

root.config(background="grey")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="close",command=root.destroy).pack()

root.mainloop()
