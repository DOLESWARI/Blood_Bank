import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image
from datetime import datetime

class stock:
    def __init__(self,con):
        self.con=con
        self.c = self.con.cursor()
        self.root = Tk()
        ######self.root=Toplevel()
        self.root.geometry("585x370+450+130")
        self.root.resizable(width=False, height=False)
        self.root.title("DSR Display_Stock")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=579, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=3, y=3)

        self.frm2 = Frame(self.root, width=579, height=308, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=3, y=53)

        self.l1 = Label(self.frm1, text="Date", font=('Helvetica', 12, font.BOLD), width=5, bg='#99004d', fg="white")
        self.l1.place(x=405, y=8)

        self.l2 = Label(self.frm1, width=10, font=('Helvetica', 12, font.BOLD),bg='#99004d', fg="white")
        self.l2.place(x=460, y=8)
        self.date_time = datetime.now()
        print(self.date_time)
        self.date_time_str = str(self.date_time)
        print(self.date_time_str)
        self.date_str = self.date_time_str[0:10]
        print(self.date_str)
        self.l2.config(text=self.date_str)

        self.l3 = Label(self.frm1, text="Blood_Group", font=('Helvetica', 12, font.BOLD), width=12, bg='#99004d',fg="white")
        self.l3.place(x=7, y=8)

        val = ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"]
        self.cmbtext = StringVar()
        self.cmbtext.set('SELECT')
        print("cmbtext=",self.cmbtext.get())
        self.cmb1 = ttk.Combobox(self.frm1, width=15, textvariable=self.cmbtext, values=val,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)

        self.cmb1.place(x=140, y=8)
        self.cmb1.bind('<<ComboboxSelected>>', self.combo_select)

        self.tree = ttk.Treeview(self.frm2, height=13, columns=4)
        self.tree["show"] = "headings"
        self.tree["columns"] = ['BLOOD GROUP', 'QUANTITY', 'COST']
        for i in range(3):
            self.tree.heading(i, text=self.tree["columns"][i])
            if i == 0:
                self.tree.column(i, anchor=CENTER, width=130)
            elif i == 1:
                self.tree.column(i, anchor=CENTER, width=190)
            elif i == 2:
                self.tree.column(i, anchor=CENTER, width=242)

        self.tree.place(x=2, y=5)
        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.tree.yview)
        self.tree["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=547, y=29, height=260)

        self.l1.focus_force()
        self.show()
        self.root.mainloop()


    def show(self):
        self.c.close()
        self.c=self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst=self.c.execute('select blood_group,quantity,cost from stock')
        for row in lst:
            ###print(row)
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2]))
        self.c.close()

    def combo_select(self, e):
        bld_grp = self.cmb1.get()
        #print(self.cmb1.get())
        #print(bld_grp,self.cmbtext.get())
        #print(type(bld_grp))
        #print(self.cmbtext.get())
        self.c.close()
        self.c = self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst = self.c.execute('select * from stock where blood_group=?',(bld_grp,))
        #lst = self.c.execute('select * from stock where blood_group=?', ("A+",))
        for row in lst:
            print(row)
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2]))
        self.c.close()



#stock()