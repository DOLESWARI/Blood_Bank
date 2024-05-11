import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from tkinter import messagebox as msg

#import ImageTk

from Main_menu import main_menu
def check():
    t1=e1.get()
    t2=e2.get()
    ###if t1!="admin@dsr":
    if t1 != "a":
        msg.showerror('ERROR', 'INCORRECT PASSWORD')
        return
    elif (t1!=t2):
        msg.showerror('ERROR', 'PASSWORDS DO NOT MATCH')
        return
    root.destroy()
    main_menu()

def cancel():
    root.destroy()
root=Tk()
root.geometry("450x175+500+200")
root.config(bg='#99004d')
root.title("DSR Login")
root.resizable(width=False,height=False)

frm1=Frame(root,width=440,height=120,bg='#99004d',relief=GROOVE,bd=5)
frm1.place(x=5,y=4)

l1=Label(frm1,text="PASSWORD:",font=('Helvetica',12,font.BOLD),bg='#99004d',fg='white')
l1.place(x=20,y=20)

e1=Entry(frm1,width=30,show='#',font=('Helvetica',8,font.BOLD))
e1.place(x=220,y=20)

l2=Label(frm1,text="CONFIRM PASSWORD:",font=('Helvetica',12,font.BOLD),bg='#99004d',fg='white')
l2.place(x=20,y=60)

e2=Entry(frm1,width=30,show='#',font=('Helvetica',8,font.BOLD))
e2.place(x=220,y=60)

frm2=Frame(root,width=440,height=50,bg='#99004d',relief=GROOVE,bd=5)
frm2.place(x=5,y=120)

b1=Button(frm2,text='LOGIN',width=6,font=('Helvetica',10,font.BOLD),relief=FLAT,bd=4,bg="#33BDC4",command=check)
b1.place(x=280,y=4)

b2=Button(frm2,text='CANCEL',width=6,font=('Helvetica',10,font.BOLD),relief=FLAT,bd=4,bg="#33BDC4",command=cancel)
b2.place(x=355,y=4)
#msg.showerror('invalid','ja baari jaa')
#password=admin@dsr
img=PhotoImage(file='images/image31.png_format.png')
root.iconphoto(False,img)
root.mainloop()
