import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image

class t_history:
    def __init__(self):
        self.root = Tk()
        ######self.root=Toplevel()
        self.root.geometry("1374x682+70+40")
        self.root.resizable(width=False, height=False)
        self.root.title("DSR Transaction_History")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=1370, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=2, y=0)

        self.l1 = Label(self.frm1, text="TRANSACTIONS", font=('Helvetica', 15, font.BOLD), width=15, bg='#99004d',fg="white")
        self.l1.place(x=8, y=6)

        self.l2 = Label(self.frm1, text="Buyer_Id", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l2.place(x=350, y=6)

        val1 = ["Select Buyer_Id"]
        cmbtext1 = StringVar()
        self.cmb1 = ttk.Combobox(self.frm1, width=23, textvariable=cmbtext1, values=val1)
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb1.place(x=460, y=6)

        self.l3 = Label(self.frm1, text="Donor_Id", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l3.place(x=700, y=6)

        val2 = ["Select Donor_Id"]
        cmbtext2 = StringVar()
        self.cmb2 = ttk.Combobox(self.frm1, width=23, textvariable=cmbtext2, values=val1)
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb2.place(x=810, y=6)

        self.l4 = Label(self.frm1, text="Duration", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l4.place(x=1050, y=6)

        val3 = ["Current Month","Previous Month","Last 2 Months","Last 3 Months","Last 6 Months","Current Year","Previous Year"]
        cmbtext3 = StringVar()
        self.cmb3 = ttk.Combobox(self.frm1, width=23, textvariable=cmbtext3, values=val3)
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb3.place(x=1160, y=6)




        self.root.mainloop()

t_history()