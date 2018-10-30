from tkinter import *

root=Tk(); a=Button(root,justify = RIGHT); b=Button(root,justify = LEFT); root.title("Tyrus's important items tracker");

x = 'rupee/rupee_green.gif'
y = 'ice/ice0.gif'

def rupeeimage():
    global x
    if x == 'rupee/rupee_grey.gif':
        x= 'rupee/rupee_green.gif'
    elif x == 'rupee/rupee_green.gif':
        x= 'rupee/rupee_grey.gif'
def iceimage():
    global y
    if y == 'ice/ice0.gif':
        y= 'ice/ice1.gif'
    elif y == 'ice/ice1.gif':
        y= 'ice/ice2.gif'
    elif y == 'ice/ice2.gif':
        y= 'ice/ice3.gif'
    elif y == 'ice/ice3.gif':
        y= 'ice/ice4.gif'
    elif y == 'ice/ice4.gif':
        y= 'ice/ice5.gif'
    elif y == 'ice/ice5.gif':
        y= 'ice/ice6.gif'
    elif y == 'ice/ice6.gif':
        y= 'ice/ice0.gif'

def clicky(rupee_ice):
    if rupee_ice == True:
        rupeeimage();

        rupeephoto = PhotoImage(file=x);
        a.config(bg='black',activebackground='black',image=rupeephoto,width="224",height="351",command= lambda : aaa('rupee'));
        a.pack(side=RIGHT);


        icephoto = PhotoImage(file=y);
        b.config(bg='black',activebackground='black',image=icephoto,width='320',height='351',command= lambda : aaa('ice'));
        b.pack(side=LEFT);

        root.mainloop();

    elif rupee_ice == False:
        iceimage();

        icephoto = PhotoImage(file=y);
        b.config(bg='black',activebackground='black',image=icephoto,width='320',height='351',command= lambda : aaa('ice'));
        b.pack(side=LEFT);


        rupeephoto = PhotoImage(file=x);
        a.config(bg='black',activebackground='black',image=rupeephoto,width="224",height="351",command= lambda : aaa('rupee'));
        a.pack(side=RIGHT);

        root.mainloop();

def aaa(a):
    if a == 'rupee':
        clicky(True)
    elif a == 'ice':
        clicky(False)
    
aaa('rupee')
