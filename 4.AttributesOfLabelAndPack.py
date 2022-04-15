# <<<<<<<<<<<<<<<<<<<<<<<[ Attributes of label and pack]>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from tkinter import *
from PIL import Image,ImageTk
sudeep_root=Tk()
sudeep_root.geometry("444x233")
sudeep_root.title("My gui with sudeep")

# important label options(attributes)..........!!!!!!!!!!!
# text= adds the text
# bd or background== give background
# fg=foreground
# font=set the font
    #  2 ways of doing font:------------------------------!
    #   i) font=("comicsansms",19,"bold")
    #   ii)font="comicsansms 19 bold"


# padx=padding in x
# pady=padding in y
# relief=border styling- SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text="Mahendra Singh Dhoni (About this soundpronunciation (help·info) born 7 July 1981), is a former Indian international\n cricketer who captained the Indian national team in limited-overs formats from 2007 to 2016 and in Test cricket from 2008 to 2014. Under his\n captaincy, India won the inaugural 2007 ICC World Twenty20, the 2010 and 2016 Asia Cups, the 2011 ICC Cricket World Cup and the 2013 ICC\n Champions Trophy. A right-handed middle-order batsman and wicket-keeper, Dhoni is one of the highest run scorers in One Day Internationals\n (ODIs) with more than 10,000 runs scored and is considered an effective finisher in limited-overs formats.[2][3][4] He is also regarded by some\n as one of the best wicket-keepers and captains in modern limited-overs international cricket.He was also the first wicketkeeper to effect\n 100 stumpings in ODI cricket. [5]",bg="red",fg="white",padx=23,pady=94,font="comicsansms 12 bold",borderwidth=3,relief=SUNKEN)
# title_label.pack()


# Important pack options(attirbutes)...................!
# anchor------> it set the direction of the element like nw for northwest, ne for northeast etc................!!!!!!!!
# side------------>TOP,BOTTOM,LEFT,RIGHT
# fill---------------> fill=X means jaise jaise x mein khichege to x mein khicta chla jaayega............!!!!!!!!
                    #  fill=y means jaise jaise y mein khichege to y mein khicta chla jaayega............!!!!!!!!


# padx--------------->give padding in x
# pady--------------->give padding in y

# title_label.pack(anchor="ne")
# title_label.pack(anchor="nw")
# title_label.pack(anchor="se") # -----> ye nihe nhi aayega ........(very very important)
# title_label.pack(anchor="sw") #------> ye nihe nhi aayega ........(very very important)
# title_label.pack(anchor="se",side=BOTTOM)
# title_label.pack(side=BOTTOM,fill=X)
title_label.pack(side=LEFT,fill=Y,padx=34,pady=34)


sudeep_root.mainloop()