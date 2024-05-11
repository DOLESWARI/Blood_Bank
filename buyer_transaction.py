import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image

class b_trans:
    def __init__(self,con):
        ######self.root = Tk()
        self.root=Toplevel()
        self.con = con
        self.c = self.con.cursor()
        self.root.geometry("1125x460+190+80")
        self.root.resizable(width=False, height=False)
        self.root.title("DSR Buyer_Transaction_History")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=1120, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=2, y=0)

        self.frm2 = Frame(self.root, width=1120, height=406, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=2, y=50)

        self.l1 = Label(self.frm1, text="TRANSACTIONS", font=('Helvetica', 15, font.BOLD), width=15, bg='#99004d',fg="white")
        self.l1.place(x=8, y=6)

        self.l2 = Label(self.frm1, text="Buyer_Id", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l2.place(x=350, y=6)

        #val1 = ["Select Buyer_Id"]
        self.cmbtext1 = StringVar()
        self.cmbtext1.set("Select Buyer_Id")
        self.c = self.con.cursor()
        lst = self.c.execute('select bid from Buyer order by bid desc')
        val1 = [row[0] for row in lst]
        self.cmb1 = ttk.Combobox(self.frm1, width=23, textvariable=self.cmbtext1, values=val1,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb1.place(x=460, y=6)

        self.l4 = Label(self.frm1, text="Duration", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l4.place(x=700, y=6)

        val2 = ["Current Month","Previous Month","Last 2 Months","Last 3 Months","Last 6 Months","Current Year","Previous Year"]
        self.cmbtext2 = StringVar()
        self.cmbtext2.set("Select Duration")
        self.cmb2 = ttk.Combobox(self.frm1, width=23, textvariable=self.cmbtext2, values=val2,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb2.place(x=810, y=6)

        self.tree = ttk.Treeview(self.frm2, height=18, columns=4)
        self.tree["show"] = "headings"
        self.tree["columns"] = ['CLAIM ID','BUYER ID', 'BUYER NAME', 'BUYER PHONE NUMBER', 'STATE','BLOOD GROUP','QUANTITY','COST']
        for i in range(8):
            self.tree.heading(i, text=self.tree["columns"][i])
            if i == 0 or i == 1:
                self.tree.column(i, anchor=CENTER, width=110)
            elif i == 2:
                self.tree.column(i, anchor=CENTER, width=180)
            elif i == 3 or i == 4 or i ==7:
                self.tree.column(i, anchor=CENTER, width=153)
            elif i == 5 or 6:
                self.tree.column(i, anchor=CENTER, width=120)
           # elif i == 7:
                #self.tree.column(i, anchor=CENTER,width=180)

        self.tree.place(x=4, y=4)
        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.tree.yview)
        self.tree["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1087, y=30, height=359)

        self.l1.focus_force()
        self.root.mainloop()

#b_trans(1)