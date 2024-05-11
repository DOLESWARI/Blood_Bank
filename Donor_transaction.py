import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image
from datetime import datetime

class d_trans:
    def __init__(self,con):
        ######self.root = Tk()
        self.root=Toplevel()
        self.con = con
        self.c = self.con.cursor()
        self.root.geometry("1315x460+120+80")
        self.root.resizable(width=False, height=False)
        self.root.title("DSR Donor_Transaction_History")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=1310, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=2, y=0)

        self.frm2 = Frame(self.root, width=1310, height=406, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=2, y=50)

        self.l1 = Label(self.frm1, text="TRANSACTIONS", font=('Helvetica', 15, font.BOLD), width=15, bg='#99004d',fg="white")
        self.l1.place(x=8, y=6)

        self.l2 = Label(self.frm1, text="Donor_Id", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l2.place(x=350, y=6)

        #val1 = ["Select Donor_Id","123"]
        self.cmbtext1 = StringVar()
        self.cmbtext1.set("Select Donor_Id")
        self.c = self.con.cursor()
        lst = self.c.execute('select did from Donor order by did desc ')
        val1 = [row[0] for row in lst]
        self.cmb1 = ttk.Combobox(self.frm1, width=23, textvariable=self.cmbtext1, values=val1,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb1.place(x=460, y=6)
        self.cmb1.bind('<<ComboboxSelected>>', self.combo_select)


        self.l4 = Label(self.frm1, text="Duration", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l4.place(x=700, y=6)

        val2 = ["Current Month","Previous Month","Last 2 Months","Last 3 Months","Last 6 Months","Current Year","Previous Year"]
        self.cmbtext2 = StringVar()
        self.cmbtext2.set("Select Duration")
        self.cmb2 = ttk.Combobox(self.frm1, width=23, textvariable=self.cmbtext2, values=val2,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb2.place(x=810, y=6)
        self.cmb2.bind('<<ComboboxSelected>>', self.select_month)

        self.tree = ttk.Treeview(self.frm2, height=18, columns=4)
        self.tree["show"] = "headings"
        self.tree["columns"] = ['TRANSACTION ID','DONOR ID', 'DONOR NAME','DATE', 'DONOR PHONE NUMBER', 'STATE','BLOOD GROUP','QUANTITY','COST']
        for i in range(9):
            self.tree.heading(i, text=self.tree["columns"][i])
            if i == 0 or i == 1:
                self.tree.column(i, anchor=CENTER, width=110)
            elif i == 2:
                self.tree.column(i, anchor=CENTER, width=180)
            elif i == 3 or i == 4 or i ==7:
                self.tree.column(i, anchor=CENTER, width=168)
            elif i == 5 or 6:
                self.tree.column(i, anchor=CENTER, width=128)
            elif i == 8:
                self.tree.column(i, anchor=CENTER,width=120)

        self.tree.place(x=4, y=4)
        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.tree.yview)
        self.tree["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1275, y=30, height=359)

        self.l1.focus_force()
        self.root.mainloop()
        #self.select_month(1)


    def combo_select(self, e):
        did1 = self.cmbtext1.get()
        print(did1)
        print(type(did1))
        #print(self.cmbtext1.get())
        self.c.close()
        self.c = self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst = self.c.execute('select tid,donor.did,dname,date,phone,state,blood_grp,quantity from donor,donate where donor.did=donate.did and donor.did=?',(did1,))
        for row in lst:
            print(row)
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],0.0))
        self.c.close()

    def select_month(self,e):
        print(self.cmbtext2.get())
        '''if(self.cmbtext2.get()=="Current Month"):
            lst=self.c.execute('select substr(date,6,2)  from donate')
            for row in lst:
                print(row)'''
        date_time = datetime.now()
        print(date_time)
        date_time_str = str(date_time)
        print(date_time_str)
        date_str = date_time_str[5:7]
        print("present month",date_str)


        for i in self.tree.get_children():
            self.tree.delete(i)

        self.c = self.con.cursor()

        if self.cmbtext2.get() == "Current Month":
            """lst = self.c.execute('select substr(date,6,2)  from donate')
            for row in lst:
                print(row[0])
                if(self.date_str==row[0]):
                    lst=self.c.execute('select tid,donor.did,dname,phone,state,blood_grp,quantity from donor,donate where donor.did=donate.did and substr(donate.date,6,2)=?',(self.date_str,))"""


            lst = self.c.execute('select tid,donor.did,dname,date,phone,state,blood_grp,quantity from donor,donate where donor.did=donate.did and cast(substr(donate.date,6,2)as integer)=?',(date_str,))
            for row in lst:
                print(row)
                self.tree.insert('', 0, text=row[0],values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], 0.0))

        if self.cmbtext2.get() == "Previous Month":
            date_new=int(date_str)-1
            print(date_new)
            lst = self.c.execute(
                'select tid,donor.did,dname,donate.date,phone,state,blood_grp,quantity from donor,donate where donor.did=donate.did and cast(substr(donate.date,6,2) as integer)=?',
                (date_new,))

            for row in lst:
                print(row)
                self.tree.insert('', 0, text=row[0],values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], 0.0))

        if (self.cmbtext2.get() == "Last 2 Months"):
            date_new = int(date_str) - 2
            print(date_new)
            lst = self.c.execute(
                'select tid,donor.did,dname,donate.date,phone,state,blood_grp,quantity from donor,donate where donor.did=donate.did and cast(substr(donate.date,6,2) as integer)=?',
                (date_new,))
            for row in lst:
                print(row)
                self.tree.insert('', 0, text=row[0],
                                 values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 0.0))

        if (self.cmbtext2.get() == "Last 3 Months"):
            date_new = int(date_str) - 3
            print(date_new)
            lst = self.c.execute(
                'select tid,donor.did,dname,donate.date,phone,state,blood_grp,quantity from donor,donate where donor.did=donate.did and cast(substr(donate.date,6,2) as integer)=?',
                (date_new,))
            for row in lst:
                print(row)
                self.tree.insert('', 0, text=row[0],
                                 values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 0.0))

        if (self.cmbtext2.get() == "Last 6 Months"):
            date_new = int(date_str) - 6
            print(date_new)
            lst = self.c.execute(
                'select tid,donor.did,dname,donate.date,phone,state,blood_grp,quantity from donor,donate where donor.did=donate.did and cast(substr(donate.date,6,2) as integer)=?',
                (date_new,))
            for row in lst:
                print(row)
                self.tree.insert('', 0, text=row[0],
                                 values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 0.0))

        if (self.cmbtext2.get() == "Current Year"):
            year=date_time_str[:4]
            print(year)
            lst = self.c.execute('select tid,did,date from donate where cast(substr(date,0,4) as integer)=?',(year,))
            for row in lst:
                print(row)

        self.c.close()
#d_trans(1)