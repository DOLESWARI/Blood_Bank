import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from datetime import datetime
from random import randint
from PIL import ImageTk,Image
from tkinter import messagebox as msg
class BLOOD_CLAIM:
    '''def select(e):
        print(cmbvar.get())'''

    def __init__(self,con):
        #########self.root = Tk()
        self.con=con
        self.lst=0
        self.root = Toplevel()
        self.root.geometry("1000x680+300+40")
        self.root.resizable(width=False,height=False)
        self.root.title("BLOOD CLAIM")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=440, height=320, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=555, y=0)

        self.frm2 = Frame(self.root, relief=RIDGE, bd=5, bg='#99004d', width=995, height=305)
        self.frm2.place(x=0, y=320)

        self.frm3= Frame(self.root,width=995,height=50,relief="ridge",bg='#99004d',bd=5)
        self.frm3.place(x=0,y=625)

        self.l1=Label(self.frm1,text="BLOOD CLAIM",font=('Helvetica',15,font.BOLD),width=20,bg='#99004d',fg="white")
        self.l1.place(x=100,y=6)

        self.l2 = Label(self.frm1, text="Claim_Id", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l2.place(x=10, y=50)

        self.l3 = Label(self.frm1, text="Buyer_Id", font=('Helvetica', 12, font.BOLD), bg='#99004d', fg="white")
        self.l3.place(x=10, y=90)

        self.l4 = Label(self.frm1, text="Blood Group", font=('Helvetica', 12, font.BOLD), bg='#99004d',fg="white")
        self.l4.place(x=10, y=130)

        self.l5 = Label(self.frm1, text="Quantity", font=('Helvetica',12, font.BOLD), bg='#99004d',fg="white")
        self.l5.place(x=10, y=170)

        self.l6 = Label(self.frm1, text="Date", font=('Helvetica', 12, font.BOLD), width=3, bg='#99004d', fg="white")
        self.l6.place(x=12, y=210)

        self.l7 = Label(self.frm1, text="Cost", font=('Helvetica', 12, font.BOLD), bg='#99004d',fg="white")
        self.l7.place(x=10, y=250)

        self.l8 = Label(self.frm1, text=" *inc GST@5%", font=('Helvetica', 8, font.BOLD), bg='#99004d', fg="white")
        self.l8.place(x=10, y=270)

        self.e1 = Entry(self.frm1, width=29, font=('Helvetica', 10, font.BOLD))
        self.e1.place(x=140, y=50)


        self.cmbtext1 = StringVar()
        self.cmbtext1.set("Select Buyer_Id")
        self.c = self.con.cursor()
        lst = self.c.execute('select bid from Buyer order by bid desc ')
        val1 = [row[0] for row in lst]
        self.cmb1 = ttk.Combobox(self.frm1, width=31, textvariable=self.cmbtext1,values=val1,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb1.place(x=140, y=90)



        val2 = ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"]
        self.cmbtext2 = StringVar()
        self.cmbtext2.set("Select Blood Group")
        self.cmb2 = ttk.Combobox(self.frm1, width=31, textvariable=self.cmbtext2, values=val2,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb2.bind('<<ComboboxSelected>>',self.combo_select)
        self.cmb2.place(x=140, y=130)


        ###self.l8 = Label(self.frm1,text="hvjh", font=('Helvetica', 12, font.BOLD), bg="white")
        self.l8 = Label(self.frm1, font=('Helvetica', 12, font.BOLD), bg='#99004d',fg="white")
        self.l8.place(x=360, y=130)




        self.e2 = Entry(self.frm1, width=29, font=('Helvetica', 10, font.BOLD))
        self.e2.place(x=140, y=170)
        self.e2.bind("<KeyRelease>",self.blood_choice)
        self.e2.delete(0, END)
        self.e2.insert(0, "0")



        self.l6 = Label(self.frm1, width=25, font=('Helvetica', 10, font.BOLD))
        self.l6.place(x=140, y=210)
        self.date_time = datetime.now()
        print(self.date_time)
        self.date_time_str = str(self.date_time)
        print(self.date_time_str)
        self.date_str = self.date_time_str[0:10]
        print(self.date_str)
        self.l6.config(text=self.date_str)

        #self.l9=Label(self.frm1,text='dsdgfvh', font=('Helvetica', 10, font.BOLD), width=5, bg="white")
        self.l9 = Label(self.frm1, font=('Helvetica', 10, font.BOLD), width=5, bg='#99004d',fg="white")
        self.l9.place(x=360, y=170)



        self.l7 = Label(self.frm1,text='0.0', font=('Helvetica', 12, font.BOLD), width=20, bg="white")
        self.l7.place(x=140, y=250)

        self.b1 = Button(self.frm1, text='ADD', width=6, font=('Helvetica', 11, font.BOLD), bd=4, bg="#33BDC4",command=self.data_entry)
        self.b1.place(x=358, y=270)

        self.b2=Button(self.frm3,text='UPDATE',width=7,font=('Helvetica',11,font.BOLD),bd=3,bg="#33BDC4",state=DISABLED,command=self.update_info)
        self.b2.place(x=4,y=3)

        self.b3 = Button(self.frm3, text='DELETE', width=7, font=('Helvetica', 11, font.BOLD), bd=3, bg="#33BDC4",state=DISABLED,command=self.delete_info)
        self.b3.place(x=908, y=3)

        self.tree = ttk.Treeview(self.frm2, height=13, columns=4)
        self.tree["show"] = "headings"
        self.tree["columns"] = ['CLAIM ID','BUYER ID','BUYER NAME','BLOOD GROUP','QUANTITY','DATE','COST']
        for i in range(7):
            self.tree.heading(i,text=self.tree["columns"][i])
            if i==0 or i==1 or i==3 or i==5:
                 self.tree.column(i, anchor=CENTER,width=120)
            elif i==4 :
                 self.tree.column(i, anchor=CENTER, width=120)
            elif i == 2:
                 self.tree.column(i, anchor=CENTER, width=175)
            elif i==6:
                 self.tree.column(i, anchor=CENTER, width=198)

        self.tree.place(x=5,y=5)
        self.scrol = ttk.Scrollbar( self.frm2, orient=VERTICAL,command= self.tree.yview)
        self.tree["yscrollcommand"] =  self.scrol.set
        self.scrol.place(x=962,y=29,height=260)


        #self.img = ImageTk.PhotoImage(file="E:\\python_projects\\blood_bank\\images\\image15.jpeg")
        self.img = ImageTk.PhotoImage(file="images\\image15.jpeg")
        print(self.img)
        l_img = Label(self.root, height=313, width=547, image=self.img)
        l_img.place(x=3, y=3)

        self.l1.focus_force()
        self.auto_gen()
        self.show()

        self.root.mainloop()



    def data_entry(self):
        if (self.b1['text'] == "ADD"):
            claim_id1 = self.e1.get()
            bid1 = self.cmb1.get()
            s_date1=self.l6.cget("text")
            blood_grp1=self.cmb2.get()
            quantity1 = self.e2.get()
            cost1 = self.l7.cget("text")

            if claim_id1 == "":
                msg.showerror('ERROR', "Please fill the Claim_Id",parent=self.root)
                return
                self.root.destroy()

            elif bid1 == "Select Buyer_Id":
                msg.showerror('ERROR', "Please fill the Buyer_Name",parent=self.root)
                return
                self.root.destroy()

                '''elif s_date1 == "":
                msg.showerror('ERROR', "Please fill the Donor_Phone_Number",parent=self.root)
                return
                self.root.destroy()'''

            elif blood_grp1 == "Select Blood Group":
                msg.showerror('ERROR', "Please fill the Blood Group",parent=self.root)
                self.e2.delete(0, END)
                return
            elif quantity1 == "" or quantity1 == "0" or quantity1 == " ":
                msg.showerror('ERROR', "Please fill the Quantity",parent=self.root)
                return
                self.root.destroy()

            elif cost1 == "" or cost1 == "0.0":
                msg.showerror('ERROR', "Please fill the Cost",parent=self.root)
                return
                self.root.destroy()

            self.c = self.con.cursor()
            self.c.execute("INSERT INTO blood_claim VALUES(?,?,?,?,?,?)", (claim_id1, bid1, s_date1,blood_grp1,quantity1, cost1))
            #self.msg["text"] = "Data Added Successfully"
            msg.showinfo('Information', "Data Added Successfully",parent=self.root)
            self.c.execute("UPDATE stock SET quantity=quantity-? WHERE blood_group=?", (quantity1, blood_grp1,))
            msg.showinfo('Information', "Data Added Successfully in stock", parent=self.root)
            self.con.commit()
            self.c.close()

            self.e1.delete(0,END)
            self.e1.insert(0,"")
            self.e2.delete(0, END)
            self.e2.insert(0, "0")
            self.cmbtext1.set("Select Buyer_Id")
            self.cmbtext2.set("Select Blood Group")
            self.l7.config(text="")
            self.l8.config(text="")
            self.l9.config(text="")
            self.auto_gen()
            self.show()
        else:
            claim_id1 = self.e1.get()
            bid1 = self.cmb1.get()
            s_date1 = self.l6.cget("text")
            blood_grp1 = self.cmb2.get()
            quantity1 = self.e2.get()
            cost1 = self.l7.cget("text")
            self.c = self.con.cursor()
            self.c.execute("update blood_claim set bid=?,s_date=?, blood_grp=?,quantity=?,cost=? where sid=?",
                           (bid1, s_date1, blood_grp1, quantity1,cost1,claim_id1))
            msg.showinfo('Information', "Data Updated Successfully", parent=self.root)
            self.con.commit()
            self.c.close()
            self.e1.delete(0, END)
            self.e1.insert(0, "")
            self.e2.delete(0, END)
            self.e2.insert(0, "")
            self.cmbtext1.set("Select Buyer_Id")
            self.cmbtext2.set("Select Blood Group")
            self.l7.config(text="")
            self.l8.config(text="")
            self.l9.config(text="")
            self.auto_gen()
            self.b1.config(text="ADD")
            self.b2.config(state=DISABLED)
            self.b3.config(state=DISABLED)
            self.auto_gen()
            self.show()

    def show(self):
        self.c.close()
        self.c=self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst=self.c.execute('select sid,buyer.bid,bname,blood_grp,quantity,blood_claim.s_date,cost from blood_claim,buyer where buyer.bid=blood_claim.bid order by sid desc')
        for row in lst:
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        self.tree.bind('<<TreeviewSelect>>', self.active_btn)
        self.c.close()

    def auto_gen(self):
        self.e1.config(state=NORMAL)
        self.c.close()
        self.c = self.con.cursor()
        lst=self.c.execute('select sid from blood_claim order by sid desc ')
        lst=[row for row in lst]
        print(lst)
        if len(lst)==0:
            str1='Sid001'
        else:
            #max=0
            a=int(lst[0][0][3:])+1
            if(a<10):
                str1 = 'Sid00' + str(a)
            elif a<=99:
                str1 = 'Sid0' + str(a)
            else:
                str1 = 'Sid' + str(a)
        self.e1.delete(0, END)
        self.e1.insert(0, str1)
        self.e1.config(state=DISABLED)

    def blood_choice(self,e):
        if self.cmbtext2.get()== "Select Blood Group":
                msg.showerror('ERROR', "Please fill the Blood Group",parent=self.root)
                self.e2.delete(0, END)
                self.e2.insert(0, "00")
                return 'break'
        self.c = self.con.cursor()
        if self.e2.get()=="":
            a=0
        else :
            a=int(self.e2.get())
        if a>self.lst[0][1]:
            msg.showinfo('Information', "Quantity should not exceed", parent=self.root)
            return 'break'
        self.l7.config(text=self.lst[0][0]*a)
        self.con.commit()
        self.c.close()


    def combo_select(self,e):
        self.c = self.con.cursor()
        self.lst = self.c.execute('select cost,quantity from stock where blood_group=?', (self.cmbtext2.get(),))
        self.lst = [a for a in self.lst]
        print(self.lst)
        self.l8.config(text=self.lst[0][0])
        self.l9.config(text=self.lst[0][1])

        self.c.close()
    def delete_info(self):
        t = self.tree.item(self.tree.selection())['text']
        self.c.close()
        self.c=self.con.cursor()
        self.c.execute("delete from blood_claim where sid=?",(t,))
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
        self.e1.config(state=NORMAL)
        self.e1.delete(0, END)
        self.e1.insert(0, t[0])
        self.e1.config(state=DISABLED)
        self.e2.insert(0,t[4])
        self.cmbtext1.set(t[2])
        self.cmbtext2.set(t[3])
        self.l7.config(text=t[6])
        '''self.e3.insert(0, t[2])
        self.a1.insert('1.0', t[4])
        '''
        self.b1.config(text="EDIT")
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.combo_select(1)

    def active_btn(self,e):
        #print(" dfgv")
        #if(x=1):
        if self.tree.item(self.tree.selection())['text']!="":
            self.b3.config(state=NORMAL)
            self.b2.config(state=NORMAL)
        else:
            self.b3.config(state=DISABLED)
            self.b2.config(state=DISABLED)

########BLOOD_CLAIM(1)

#qty = int(self.e2.get())
