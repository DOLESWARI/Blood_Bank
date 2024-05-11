import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image

class report:
    def __init__(self):
        self.root = Tk()
        ######self.root=Toplevel()
        self.root.geometry("585x408+450+80")
        self.root.resizable(width=False, height=False)
        self.root.title("DISPLAY REPORT")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=579, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=3, y=3)

        self.frm2 = Frame(self.root, width=579, height=300, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=3, y=53)

        self.frm3 = Frame(self.root, width=579, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm3.place(x=3, y=353)

        #self.rbvar = IntVar()
        #self.rbvar.set(0)
        #self.rb1 = Radiobutton(self.frm1, text='Male', variable=rbvar, bg='#456398', value=1, command=selectRadio)
        self.rb1 = Radiobutton(self.frm1, text='DONOR',font=('Helvetica', 11, font.BOLD), value=1,bd=3, bg="#33BDC4")
        self.rb1.place(x=10, y=4)

        #self.rb2 = Radiobutton(self.frm1, text='Female', variable=rbvar, bg='#456398', value=2, command=selectRadio)
        self.rb2 = Radiobutton(self.frm1, text='BUYER', font=('Helvetica', 11, font.BOLD), value=2,bd=3, bg="#33BDC4")
        self.rb2.place(x=150, y=4)

        self.b1 = Button(self.frm3, text='GENERATE REPORT', width=20, font=('Helvetica', 11, font.BOLD), bd=3, bg="#33BDC4")
        self.b1.place(x=365, y=3)


        self.img = ImageTk.PhotoImage(file="E:\\python_projects\\blood_bank\\images\\image27.jpeg")
        print(self.img)
        l_img = Label(self.root, height=280, width=560, image=self.img)
        l_img.place(x=9, y=61)





        self.root.mainloop()

report()