import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from datetime import datetime
from random import randint
from PIL import ImageTk,Image
from tkinter import messagebox as msg
class Donation:
    def __init__(self,con):
        self.con=con
        self.c = self.con.cursor()
       # self.root=Tk()
        self.root = Toplevel()
        self.root.geometry("1010x650+200+70")
        self.root.resizable(width=False,height=False)
        self.root.title("DSR Donation")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root,width=440,height=290,relief="ridge",bg='#99004d',bd=5)
        self.frm1.place(x=568,y=0)

        self.frm2 = Frame(self.root, relief=RIDGE, bd=5, bg='#99004d', width=1006, height=305)
        self.frm2.place(x=2, y=290)

        self.frm3= Frame(self.root,width=1006,height=50,relief="ridge",bg='#99004d',bd=5)
        self.frm3.place(x=2,y=595)

        self.l1=Label(self.frm1,text="DONATION",font=('Helvetica',15,font.BOLD),width=20,bg='#99004d',fg="white")
        self.l1.place(x=80,y=6)

        self.l2=Label(self.frm1,text="Transaction_Id",font=('Helvetica',12,font.BOLD),width=12,bg='#99004d',fg="white")
        self.l2.place(x=10,y=50)

        self.l3=Label(self.frm1,text="Donor_Id",font=('Helvetica',12,font.BOLD),width=9,bg='#99004d',fg="white")
        self.l3.place(x=10,y=90)

        self.l4=Label(self.frm1,text="Blood_Group",font=('Helvetica',12,font.BOLD),width=12,bg='#99004d',fg="white")
        self.l4.place(x=10,y=130)

        self.l5=Label(self.frm1,text="Quantity",font=('Helvetica',12,font.BOLD),width=8,bg='#99004d',fg="white")
        self.l5.place(x=10,y=170)

        self.l6=Label(self.frm1,text="Date",font=('Helvetica',12,font.BOLD),width=5,bg='#99004d',fg="white")
        self.l6.place(x=12,y=210)

        self.e1=Entry(self.frm1,width=30,font=('Helvetica',10,font.BOLD),state=DISABLED)
        self.e1.place(x=160,y=50)

        '''self.l7 = Label(self.frm1, font=('Helvetica', 12, font.BOLD), width=21, bg="white")
        self.l7.place(x=160, y=50)'''

        #val1 = ["Select Donor_Id"]

        self.cmbtext1 = StringVar()
        self.cmbtext1.set("Select Donor_Id")
        self.c = self.con.cursor()
        lst = self.c.execute('select did from Donor order by did desc ')
        val1 = [row[0] for row in lst]
        self.cmb1 = ttk.Combobox(self.frm1, width=32, textvariable=self.cmbtext1, values=val1,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb1.place(x=160, y=90)


        '''self.e2=Entry(self.frm1,width=30,font=('Helvetica',10,font.BOLD))
        self.e2.place(x=160,y=90)'''


        val2 = ["A+", "B+", "AB+", "O+","A-", "B-", "AB-", "O-"]
        self.cmbtext2 = StringVar()
        self.cmbtext2.set("Select Blood_grp")
        self.cmb2= ttk.Combobox(self.frm1,width=32, textvariable=self.cmbtext2, values=val2,state='readonly')
        #self.cmb2 = ttk.Combobox(self.frm1,width=32)
        self.cmb2.place(x=160, y=130)

        self.e3 = Entry(self.frm1, width=30, font=('Helvetica', 10, font.BOLD))
        self.e3.place(x=160, y=170)

        self.l7=Label(self.frm1,width=26,font=('Helvetica',10,font.BOLD))
        self.l7.place(x=160,y=210)
        self.date_time = datetime.now()
        print(self.date_time)
        self.date_time_str = str(self.date_time)
        print(self.date_time_str)
        self.date_str = self.date_time_str[0:10]
        print(self.date_str)
        self.l7.config(text=self.date_str)

        self.b1=Button(self.frm1,text='ADD',width=5,font=('Helvetica',11,font.BOLD),bd=4,bg="#33BDC4",command=self.data_entry)
        self.b1.place(x=365,y=240)
        
        self.b2=Button(self.frm3,text='UPDATE',width=7,font=('Helvetica',11,font.BOLD),bd=3,bg="#33BDC4",state=DISABLED,command=self.update_info)
        self.b2.place(x=5,y=3)

        self.b3 = Button(self.frm3, text='DELETE', width=7, font=('Helvetica', 11, font.BOLD), bd=3, bg="#33BDC4",command=self.delete_info,state=DISABLED)
        self.b3.place(x=914, y=3)

        self.tree = ttk.Treeview(self.frm2, height=13, columns=5)
        self.tree["show"] = "headings"
        self.tree["columns"] = ['Transaction_Id','Donor_Id', 'Donor_Name', 'Blood_Group', 'Quantity','Date']
        for i in range(6):
                    self.tree.heading(i, text=self.tree["columns"][i])
                    if i == 0 or 1:
                        self.tree.column(i, anchor=CENTER, width=157)
                    elif i == 2 :
                        self.tree.column(i, anchor=CENTER, width=1)
                    elif  i == 2 or i==3:
                        self.tree.column(i, anchor=CENTER, width=200)
                    if i==4:
                        self.tree.column(i, anchor=CENTER, width=200)
        self.tree.place(x=5, y=5)

        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.tree.yview)
        self.tree["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=973, y=30, height=260)


        #self.img = ImageTk.PhotoImage(file="E:\\python_projects\\blood_bank\\images\\image27.jpeg")
        self.img = ImageTk.PhotoImage(file="images/image27.jpeg")
        print(self.img)
        l_img = Label(self.root, height=280, width=560, image=self.img)
        l_img.place(x=4, y=3)


        self.l1.focus_force()
        self.show()
        self.auto_gen()
        self.root.mainloop()

    def data_entry(self):
        if (self.b1['text'] == "ADD"):
            tid = self.e1.get()
            did = self.cmb1.get()
            blood_grp1 = self.cmb2.get()
            qty = int(self.e3.get())
            dat=self.l7.cget("text")

            if tid == "":
                msg.showerror('ERROR', "Please fill the Donor_Id", parent=self.root)
                return
                self.root.destroy()
            elif qty=="":
                msg.showerror('ERROR', "Please fill the Donor_Id", parent=self.root)
                return
                self.root.destroy()
            elif did == "Select Donor_Id":
                msg.showerror('ERROR', "Please select state", parent=self.root)
                return
                self.root.destroy()
            elif blood_grp1 == "Select Blood_grp":
                msg.showerror('ERROR', "Please select state", parent=self.root)
                return
                self.root.destroy()
            #print(tid +","+ did + ","+ blood_grp1+ ","+ qty + ","+ dat)

            self.c = self.con.cursor()
            self.c.execute("INSERT INTO donate VALUES(?,?,?,?,?)", (tid, did,blood_grp1, qty, dat))
            msg.showinfo('Information', "Data Added Successfully", parent=self.root)
            self.c.execute("UPDATE stock SET quantity=quantity+? WHERE blood_group=?",(qty,blood_grp1,))
            msg.showinfo('Information', "Data Added Successfully in stock", parent=self.root)
            self.con.commit()

            '''self.e2.delete(0, END)
            self.e2.insert(0, "")'''
            self.e3.delete(0, END)
            self.e3.insert(0, "")
            '''self.a1.delete('1.0', END)
            self.a1.insert('1.0', "")'''
            self.cmbtext1.set("Select Donor_Id")
            self.cmbtext2.set("Select Blood_grp")

            self.auto_gen()
            self.show()
            self.c.close()

        else:
            tid1 = self.e1.get()
            did1 = self.cmb1.get()
            blood_grp1 = self.cmb2.get()
            qty1 = self.e3.get()
            dat1 = self.l7.cget("text")
            self.c = self.con.cursor()
            self.c.execute("update donate set did=?, blood_grp=?,quantity=?, date=? where tid=?",
                           (did1, blood_grp1, qty1, dat1, tid1))
            msg.showinfo('Information', "Data Updated Successfully", parent=self.root)
            self.con.commit()
            self.c.close()

            '''self.e2.delete(0, END)
            self.e2.insert(0, "")'''
            self.e3.delete(0, END)
            self.e3.insert(0, "")
            '''self.a1.delete('1.0', END)
            self.a1.insert('1.0', "")'''
            self.cmbtext1.set("Select Donor_Id")
            self.cmbtext2.set("Select Blood_grp")

            self.show()
            self.auto_gen()
            self.b1.config(text="ADD")
            self.b2.config(state=DISABLED)
            self.b3.config(state=DISABLED)

    def show(self):
        self.c.close()
        self.c=self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst=self.c.execute('select tid,donate.did,donor.dname,blood_grp,quantity,donate.date from donate,donor where donate.did=donor.did')
        for row in lst:
            ###print(row)
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5]))
        self.tree.bind('<<TreeviewSelect>>', self.active_btn)
        self.c.close()

    def auto_gen(self):
        self.e1.config(state=NORMAL)
        self.c.close()
        self.c = self.con.cursor()
        lst=self.c.execute('select tid from donate order by tid desc ')
        lst=[row for row in lst]
        print(lst)
        if len(lst)==0:
            str1='Tid001'
        else:
            #max=0
            a=int(lst[0][0][3:])+1
            if(a<10):
                str1 = 'Tid00' + str(a)
            elif a<=99:
                str1 = 'Tid0' + str(a)
            else:
                str1 = 'Tid' + str(a)
        self.e1.delete(0, END)
        self.e1.insert(0, str1)
        self.e1.config(state=DISABLED)

    def delete_info(self):
        t = self.tree.item(self.tree.selection())['text']
        self.c.close()
        self.c=self.con.cursor()
        self.c.execute("delete from donate where tid=?",(t,))
        self.con.commit()
        msg.showinfo('Information', "Data Deleted Successfully", parent=self.root)
        self.show()
        self.b3.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.auto_gen()

    def update_info(self):
        t=self.tree.item(self.tree.selection())['values']
        self.c.close()
        print(t)
        self.cmbtext1.set(t[1])
        self.cmbtext2.set(t[2])
        #self.a1.insert('1.0', t[4])
        self.e1.config(state=NORMAL)
        self.e1.delete(0, END)
        self.e1.insert(0,t[0])
        self.e1.config(state=DISABLED)
        self.b1.config(text="EDIT")
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.e3.insert(0, t[3])
        #self.e3.insert(0, t[2])


    def active_btn(self,e):
        #print(" dfgv")
        #if(x=1):
        if self.tree.item(self.tree.selection())['text']!="":
            self.b3.config(state=NORMAL)
            self.b2.config(state=NORMAL)
        else:
            self.b3.config(state=DISABLED)
            self.b2.config(state=DISABLED)



#Donation()