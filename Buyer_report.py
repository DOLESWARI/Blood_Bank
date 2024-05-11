import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image

class b_report:
    def __init__(self,con):
        #self.root = Tk()
        self.root=Toplevel()
        self.con = con
        self.c = self.con.cursor()
        self.root.geometry("1130x418+200+80")
        self.root.resizable(width=False, height=False)
        self.root.title("DSR Buyer_Report")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=1123, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=3, y=3)

        self.frm2 = Frame(self.root, width=1123, height=308, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=3, y=53)

        self.frm3 = Frame(self.root, width=1123, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm3.place(x=3, y=361)

        #self.rbvar = IntVar()
        #self.rbvar.set(0)
        #self.rb1 = Radiobutton(self.frm1, text='Male', variable=rbvar, bg='#456398', value=1, command=selectRadio)
        '''self.rb1 = Radiobutton(self.frm1, text='DONOR',font=('Helvetica', 11, font.BOLD), value=1,bd=3, bg="#33BDC4")
        self.rb1.place(x=10, y=4)'''

        self.l1 = Label(self.frm1, text='BUYER REPORT', font=('Helvetica', 15, font.BOLD), bg='#99004d',fg="white")
        self.l1.place(x=18, y=4)

        #self.rb2 = Radiobutton(self.frm1, text='Female', variable=rbvar, bg='#456398', value=2, command=selectRadio)
        '''self.rb2 = Radiobutton(self.frm1, text='BUYER', font=('Helvetica', 11, font.BOLD), value=2,bd=3, bg="#33BDC4")
        self.rb2.place(x=150, y=4)'''

        self.e1 = Entry(self.frm1, width=20, font=('Helvetica', 10, font.BOLD))
        self.e1.place(x=230, y=4)
        self.e1.bind('<KeyRelease>', self.select_name)

        self.b1 = Button(self.frm3, text='GENERATE REPORT', width=20, font=('Helvetica', 11, font.BOLD), bd=3, bg="#33BDC4",state=DISABLED)
        self.b1.place(x=915, y=3)

        val = ["LADAKH","JAMMU KASHMIR","HIMACHAL PRADESH","UTTARAKHAND","DELHI","UTTAR PRADESH","BIHAR","JHARKHAND","ASSAM","NAGALAND","MANIPUR","MIZORAM","WEST BENGAL","ODISHA","CHATTISGRARH","ANDRA PRADESH","TAMIL NADU","KERELA","KARNATAKA","TELENGANA","MAHARASTRA","GUJARAT","RAJASTHAN","MADHYA PRADESH"]
        self.cmbtext = StringVar()
        self.cmbtext.set("Select State")
        self.cmb = ttk.Combobox(self.frm1, width=20, textvariable=self.cmbtext, values=val,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb.place(x=450, y=4)
        self.cmb.bind('<<ComboboxSelected>>', self.combo_select)

        self.tree = ttk.Treeview(self.frm2, height=13, columns=4)
        self.tree["show"] = "headings"
        self.tree["columns"] = ['BUYER ID','BUYER NAME', 'PHONE NO', 'BUYER STATE','ADDRESS']
        for i in range(5):
            self.tree.heading(i, text=self.tree["columns"][i])
            if i == 0 or i==1:
                self.tree.column(i, anchor=CENTER, width=200)
            elif i == 2:
                self.tree.column(i, anchor=CENTER, width=220)
            elif i == 3 or i==4:
                self.tree.column(i, anchor=CENTER, width=240)

        self.tree.place(x=5, y=5)
        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.tree.yview)
        self.tree["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1088, y=30, height=259)

        self.show()
        self.l1.focus_force()
        self.root.mainloop()

    def combo_select(self, e):
        state1=self.cmbtext.get()
        print(state1)
        self.c.close()
        self.c = self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst = self.c.execute('select * from buyer where state=?',(state1,))
        #lst=self.c.execute('select dname,did,state from donor where state="WEST BENGAL"')
        for row in lst:
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4]))
        self.tree.bind('<<TreeviewSelect>>', self.active_btn)
        self.c.close()


    def active_btn(self,e):
        #print(" dfgv")
        #if(x=1):
        if self.tree.item(self.tree.selection())['text']!="":
            self.b1.config(state=NORMAL)
            self.b1.config(state=NORMAL)
        else:
            self.b1.config(state=DISABLED)
            self.b1.config(state=DISABLED)

    def show(self):
        self.c.close()
        self.c=self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        name = self.e1.get()
        self.c.close()
        self.c = self.con.cursor()
        lst=self.c.execute("select * from buyer where bname like ?", (name+'%',))
        self.con.commit()
        for row in lst:
            print(row)
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4]))
        self.tree.bind('<<TreeviewSelect>>', self.active_btn)
        self.c.close()

    def select_name(self, e):
        self.show()
#b_report()