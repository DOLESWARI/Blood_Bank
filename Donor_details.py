import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image
from tkinter import messagebox as msg
class Donor_details:
    def __init__(self,con):
        self.con=con
        self.c=self.con.cursor()
        self.root=Toplevel()
        ########self.root = Tk()
        self.root.geometry("905x640+300+50")
        self.root.resizable(width=False,height=False)
        self.root.title("DSR Donor_Details")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=470, height=280, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=430, y=0)

        self.frm2 = Frame(self.root, relief=RIDGE, bd=5, bg='#99004d', width=900, height=305)
        self.frm2.place(x=0, y=280)

        self.frm3= Frame(self.root,width=900,height=50,relief="ridge",bg='#99004d',bd=5)
        self.frm3.place(x=0,y=585)


        self.l1=Label(self.frm1,text="DONOR DETAILS",font=('Helvetica',15,font.BOLD),width=20,bg='#99004d',fg="white")
        self.l1.place(x=100,y=10)

        self.l2=Label(self.frm1,text="Donor_Id",font=('Helvetica',12,font.BOLD),width=9,bg='#99004d',fg="white")
        self.l2.place(x=0,y=50)

        self.l3=Label(self.frm1,text="Donor_Name",font=('Helvetica',12,font.BOLD),width=10,bg='#99004d',fg="white")
        self.l3.place(x=8,y=90)

        self.l4 = Label(self.frm1, text="Donor_Ph_No", font=('Helvetica', 12, font.BOLD), width=12, bg='#99004d',fg="white")
        self.l4.place(x=2, y=130)

        self.l5=Label(self.frm1,text="State",font=('Helvetica',12,font.BOLD),width=5,bg='#99004d',fg="white")
        self.l5.place(x=2,y=170)

        self.l6=Label(self.frm1,text="Donor_Address",font=('Helvetica',12,font.BOLD),width=12,bg='#99004d',fg="white")
        self.l6.place(x=10,y=210)

        self.e1=Entry(self.frm1,width=30,font=('Helvetica',10,font.BOLD))
        self.e1.place(x=160,y=50)

        '''self.l7 = Label(self.frm1, font=('Helvetica', 12, font.BOLD), width=21, bg="white")
        self.l7.place(x=160, y=50)'''

        self.e2=Entry(self.frm1,width=30,font=('Helvetica',10,font.BOLD))
        self.e2.place(x=160,y=90)

        self.e3=Entry(self.frm1,width=30,font=('Helvetica',10,font.BOLD))
        self.e3.place(x=160,y=130)

        '''self.e4 = Entry(self.frm1, width=30, font=('Helvetica', 10, font.BOLD))
        self.e4.place(x=160, y=170)'''

        val = [ "LADAKH", "JAMMU KASHMIR", "HIMACHAL PRADESH", "UTTARAKHAND", "DELHI", "UTTAR PRADESH",
               "BIHAR", "JHARKHAND", "ASSAM", "NAGALAND", "MANIPUR", "MIZORAMNM", "WEST BENGAL", "ODISHA",
               "CHATTISGRARH", "ANDRA PRADESH", "TAMIL NADU", "KERELA", "KARNATAKA", "TELENGANA", "MAHARASTRA",
               "GUJARAT", "RAJASTHAN", "MADHYA PRADESH"]
        self.cmbtext = StringVar()
        self.cmbtext.set("Select State")
        self.cmb1 = ttk.Combobox(self.frm1, width=32, textvariable=self.cmbtext, values=val,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb1.place(x=160, y=170)

        self.a1=Text(self.frm1,width=30,height=3,font=('Helvetica',10,font.BOLD))
        self.a1.place(x=160,y=210)

        self.b1=Button(self.frm1,text='ADD',width=6,font=('Helvetica',11,font.BOLD),bd=4,bg="#33BDC4",command=self.data_entry)
        self.b1.place(x=385,y=230)


        self.b2=Button(self.frm3,text='UPDATE',width=7,font=('Helvetica',11,font.BOLD),bd=3,bg="#33BDC4",state=DISABLED,command=self.update_info)
        self.b2.place(x=4,y=3)

        '''self.b4 = Button(self.frm3, text='CANCEL', width=7, font=('Helvetica', 11, font.BOLD), bd=3, bg="#33BDC4")
        self.b4.place(x=400, y=3)'''

        self.b3 = Button(self.frm3, text='DELETE', width=7, font=('Helvetica', 11, font.BOLD), bd=3, bg="#33BDC4",state=DISABLED,command=self.delete_info)
        self.b3.place(x=810, y=3)
        #self.b3.bind('<KeyPress>', lambda x: active(x, 1))

        self.tree = ttk.Treeview(self.frm2, height=13, columns=4)
        self.tree["show"] = "headings"
        self.tree["columns"] = ['DONOR ID', 'DONOR NAME', 'DONOR PHONE NUMBER', 'STATE','DONOR ADDRESS']
        for i in range(5):
            self.tree.heading(i, text=self.tree["columns"][i])
            if i == 0:
                self.tree.column(i, anchor=CENTER, width=110)
            elif i == 1 :
                self.tree.column(i, anchor=CENTER, width=180)
            elif i==2 :
                self.tree.column(i, anchor=CENTER, width=150)
            elif i == 3 :
                self.tree.column(i, anchor=CENTER, width=180)
            elif i == 4:
                self.tree.column(i, anchor=CENTER, width=260)

        self.tree.place(x=5, y=5)
        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.tree.yview)
        self.tree["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=868, y=30, height=260)

        #self.img = ImageTk.PhotoImage(file="E:\\python_projects\\blood_bank\\images\\image17.jpeg")
        self.img = ImageTk.PhotoImage(file="images/image17.jpeg")
        print(self.img)
        l_img = Label(self.root, height=268, width=420, image=self.img)
        l_img.place(x=3, y=3)
        self.l1.focus_force()
        self.show()
        self.auto_gen()
        self.root.mainloop()


    def data_entry(self):
        #print(self.b1['text'])
        if(self.b1['text']=="ADD"):
            did = self.e1.get()
            dname = self.e2.get()
            phone = self.e3.get()
            combo = self.cmb1.get()
            address = self.a1.get('1.0',END)

            if did == "":
                msg.showerror('ERROR', "Please fill the Donor_Id",parent=self.root)
                return
                self.root.destroy()
                #break

            elif dname == "":
                msg.showerror('ERROR', "Please fill the Donor_Name",parent=self.root)
                return
                self.root.destroy()

            elif phone == "":
                msg.showerror('ERROR', "Please fill the Donor_Phone_Number",parent=self.root)
                return
                self.root.destroy()

            elif address == "":
                msg.showerror('ERROR', "Please fill the Donor_Address",parent=self.root)
                return
                self.root.destroy()

            #####elif self.cmb1.get() == "Select State":
            elif combo == "Select State":
                msg.showerror('ERROR', "Please select state",parent=self.root)
                return
                self.root.destroy()
            self.c = self.con.cursor()
            self.c.execute("INSERT INTO donor VALUES(?,?,?,?,?)", (did, dname, phone,combo, address))
            self.con.commit()
            self.c.close()
            #self.msg["text"] = "Data Added Successfully"
            msg.showinfo('Information', "Data Added Successfully",parent=self.root)


            self.e2.delete(0, END)
            self.e2.insert(0, "")
            self.e3.delete(0, END)
            self.e3.insert(0, "")
            '''self.e1.delete(0, END)
            self.e1.insert(0, "")'''
            self.a1.delete('1.0',END)
            self.a1.insert('1.0',"")
            self.cmbtext.set("Select State")
            self.show()
            self.auto_gen()
        else:
            did1 = self.e1.get()
            dname1 = self.e2.get()
            phone1 = self.e3.get()
            combo1 = self.cmb1.get()
            address1 = self.a1.get('1.0', END)
            self.c = self.con.cursor()
            self.c.execute("update donor set dname=?, phone=?,state=?, address=? where did=?",(dname1,phone1,combo1,address1,did1))
            msg.showinfo('Information', "Data Updated Successfully",parent=self.root)
            self.con.commit()
            self.c.close()

            self.e2.delete(0, END)
            self.e2.insert(0, "")
            self.e3.delete(0, END)
            self.e3.insert(0, "")

            self.a1.delete('1.0', END)
            self.a1.insert('1.0', "")
            self.cmbtext.set("Select State")
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
        lst=self.c.execute('select * from Donor order by did desc')
        for row in lst:
            ###print(row)
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4]))
        self.tree.bind('<<TreeviewSelect>>', self.active_btn)
        self.c.close()

    def auto_gen(self):
        self.e1.config(state=NORMAL)
        self.c.close()
        self.c = self.con.cursor()
        lst=self.c.execute('select did from Donor order by did desc ')
        lst=[row for row in lst]
        print(lst)
        if len(lst)==0:
            str1='Did001'
        else:
            #max=0
            a=int(lst[0][0][3:])+1
            if(a<10):
                str1 = 'Did00' + str(a)
            elif a<=99:
                str1 = 'Did0' + str(a)
            else:
                str1 = 'Did' + str(a)
        self.e1.delete(0, END)
        self.e1.insert(0, str1)
        self.e1.config(state=DISABLED)

    def active_btn(self,e):
        print(" dfgv")
        #if(x=1):
        if self.tree.item(self.tree.selection())['text']!="":
            self.b3.config(state=NORMAL)
            self.b2.config(state=NORMAL)
        else:
            self.b3.config(state=DISABLED)
            self.b2.config(state=DISABLED)

    def delete_info(self):
        t = self.tree.item(self.tree.selection())['text']
        self.c.close()
        self.c=self.con.cursor()
        self.c.execute("delete from donor where did=?",(t,))
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
        self.e2.insert(0,t[1])
        self.e3.insert(0, t[2])
        self.cmbtext.set(t[3])
        self.a1.insert('1.0', t[4])
        self.e1.config(state=NORMAL)
        self.e1.delete(0, END)
        self.e1.insert(0,t[0])
        self.e1.config(state=DISABLED)
        self.b1.config(text="EDIT")
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)

####Donor_details()