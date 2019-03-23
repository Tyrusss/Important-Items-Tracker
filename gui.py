from tkinter import (PhotoImage, Tk, Button, RIGHT, LEFT, TOP, BOTTOM)

root=Tk()
a=Button(root,justify = RIGHT)
root.title("Tyrus's important items tracker")

x = 'rupee/rupee_green.gif'
global x

def rupeeimage():
    if x == 'rupee/rupee_grey.gif':
        x= 'rupee/rupee_green.gif'
    elif x == 'rupee/rupee_green.gif':
        x= 'rupee/rupee_grey.gif'


def clicky():
    rupeeimage()

    rupeephoto = PhotoImage(file=x)
    a.config(bg='black',activebackground='black',image=rupeephoto,width="224",height="351",command= clicky)
    a.pack(side=RIGHT)

    root.mainloop()

clicky()
