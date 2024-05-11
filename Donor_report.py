import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image
import csv
from threading import Thread
from datetime import date

class d_report:
    def __init__(self,con):
        #self.root = Tk()
        self.con = con
        self.c = self.con.cursor()
        #self.p=canvas.Canvas("xyz")
        self.root=Toplevel()
        self.root.geometry("1128x415+200+80")
        self.root.resizable(width=False, height=False)
        self.root.title("DSR Donor_Report")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root, width=1122, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=3, y=3)

        self.frm2 = Frame(self.root, width=1122, height=308, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=3, y=53)

        self.frm3 = Frame(self.root, width=1122, height=50, relief="ridge", bg='#99004d', bd=5)
        self.frm3.place(x=3, y=361)


        self.l1 = Label(self.frm1, text='DONOR REPORT', font=('Helvetica', 15, font.BOLD), bg='#99004d',fg="white")
        self.l1.place(x=5, y=4)

        self.e1 = Entry(self.frm1, width=20, font=('Helvetica', 10, font.BOLD))
        self.e1.place(x=230, y=4)
        #self.e1.bind('<KeyRelease>',self.select_name)
        self.e1.bind('<KeyRelease>', self.name_state)

        self.b1 = Button(self.frm3, text='GENERATE REPORT', width=20, font=('Helvetica', 11, font.BOLD), bd=3, bg="#33BDC4",state=DISABLED,command=self.pdf_name)
        self.b1.place(x=915, y=3)

        self.b2 = Button(self.frm3, text='FULL REPORT', width=20, font=('Helvetica', 11, font.BOLD), bd=3,bg="#33BDC4",command=self.pdf_state)
        self.b2.place(x=710, y=3)

        val = ["None","LADAKH","JAMMU KASHMIR","HIMACHAL PRADESH","UTTARAKHAND","DELHI","UTTAR PRADESH","BIHAR","JHARKHAND","ASSAM","NAGALAND","MANIPUR","MIZORAM","WEST BENGAL","ODISHA","CHATTISGARH","ANDRA PRADESH","TAMIL NADU","KERELA","KARNATAKA","TELENGANA","MAHARASTRA","GUJARAT","RAJASTHAN","MADHYA PRADESH"]
        self.cmbtext = StringVar()
        #print("cmbtext=", self.cmbtext)
        self.cmbtext.set("Select State")
        self.cmb = ttk.Combobox(self.frm1, width=20, textvariable=self.cmbtext, values=val,state='readonly')
        # self.cmb1 = ttk.Combobox(self.frm1,width=32)
        self.cmb.place(x=400, y=4)
        #self.cmb.bind('<<ComboboxSelected>>', self.combo_select)
        self.cmb.bind('<<ComboboxSelected>>', self.name_state)

        self.tree = ttk.Treeview(self.frm2, height=13, columns=4)
        self.tree["show"] = "headings"
        '''
        self.tree["columns"] = ['DONOR NAME', 'DONOR ID', 'BLOOD GROUP','DONOR STATE','PHONE NO','ADDRESS']
        for i in range(6):
            self.tree.heading(i, text=self.tree["columns"][i])
            if i == 0:
                self.tree.column(i, anchor=CENTER, width=200)
            elif i == 1 :
                self.tree.column(i, anchor=CENTER, width=180)
            elif i == 2:
                self.tree.column(i, anchor=CENTER, width=175)
            elif i==3 or i==4 or i==5:
                self.tree.column(i, anchor=CENTER, width=200)
        '''
        self.tree["columns"] = ['DONOR ID', 'DONOR NAME', 'PHONE NO', 'DONOR STATE', 'ADDRESS']
        for i in range(5):
            self.tree.heading(i, text=self.tree["columns"][i])
            if i == 0 or i == 1:
                self.tree.column(i, anchor=CENTER, width=200)
            elif i == 2:
                self.tree.column(i, anchor=CENTER, width=220)
            elif i == 3 or i == 4:
                self.tree.column(i, anchor=CENTER, width=240)

        self.tree.place(x=5, y=5)
        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.tree.yview)
        self.tree["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1089, y=30, height=259)


        self.show()
        #self.pdf_layout()
        self.l1.focus_force()
        self.root.mainloop()

    def pdf_layout(self,p,c,state,did):
        pgcount = c
        #p = canvas.Canvas("Donor_Details.pdf", pagesize=portrait(A4))
        p.setFont('Helvetica', 15, leading=None)
        #p.showPage()
        time = date.today()
        p.drawString(500, 802, str(time.day) + "/" + str(time.month) + "/" + str(time.year))
        p.line(10, 800, 583, 800)
        p.line(10, 30, 583, 30)
        p.line(10, 30, 10, 800)
        p.line(583, 30, 583, 800)

        p.drawCentredString(300, 803, "DONOR DETAILS")
        p.drawCentredString(90, 803, "DSR BLOOD BANK")
        p.drawCentredString(300, 12, str(pgcount))

        cordinate = [20, 58, 200, 300]
        heading = ["STATE : ", "NAME : ", "DONOR ID: "]
        p.drawCentredString(50, 770, heading[0])
        p.drawCentredString(48, 745, heading[1])
        p.drawCentredString(62, 720, heading[2])

        p.line(20, 700, 573, 700)
        p.line(20, 50, 573, 50)
        p.line(20, 50, 20, 700)
        p.line(573, 50, 573, 700)

        p.drawCentredString(45, 680, "Sl No.")
        p.line(68, 700, 68, 50)
        p.drawCentredString(145, 680, "BLOOD GROUP")
        p.line(220, 700, 220, 50)
        p.drawCentredString(284, 680, "QUANTITY")
        p.line(350, 700, 350, 50)
        p.drawCentredString(463, 680, "DATE OF DONATION")
        p.line(20, 670, 573, 670)

        p.drawCentredString(240, 770, str(state))
        p.drawCentredString(240, 720, did)

        #print("pdf_layout created")

    def pdf_cont_layout(self,p):

        pgcount = 1
        #p = canvas.Canvas("Trial.pdf", pagesize=portrait(A4))
        p.setFont('Helvetica', 15, leading=None)
        time = date.today()
        p.drawString(500, 802, str(time.day) + "/" + str(time.month) + "/" + str(time.year))
        p.line(10, 800, 583, 800)
        p.line(10, 30, 583, 30)
        p.line(10, 30, 10, 800)
        p.line(583, 30, 583, 800)

        p.drawCentredString(300, 803, "DONOR DETAILS")
        p.drawCentredString(90, 803, "DSR BLOOD BANK")

        p.line(20, 780, 573, 780)
        p.line(20, 50, 573, 50)
        p.line(20, 50, 20, 780)
        p.line(573, 50, 573, 780)

        p.drawCentredString(45, 758, "Sl No.")
        p.line(68, 780, 68, 50)
        p.drawCentredString(145, 758, "BLOOD GROUP")
        p.line(220, 780, 220, 50)
        p.drawCentredString(284, 758, "QUANTITY")
        p.line(350, 780, 350, 50)
        p.drawCentredString(463, 758, "DATE OF DONATION")
        p.line(20, 748, 573, 748)


    def combo_select(self, e):
        state1=self.cmbtext.get()
        print(state1)
        self.c.close()
        self.c = self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        #lst = self.c.execute('select dname,donate.did,blood_grp,state,phone,address from donor,donate where state=? and donor.did=donate.did',(state1,))
        lst=self.c.execute("select * from donor where state=?",(state1,))
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

    def select_name(self, e):
        self.show()


    def show(self):
        self.c.close()
        self.c=self.con.cursor()
        for i in self.tree.get_children():
            self.tree.delete(i)
        name = self.e1.get()
        self.c.close()
        self.c = self.con.cursor()
        #lst=self.c.execute("select dname,donor.did,blood_grp,state,phone,address from donor,donate where dname like ? and donor.did=donate.did", (name+'%',))
        lst = self.c.execute("select * from donor where dname like ?", (name + '%',))
        self.con.commit()
        for row in lst:
            #print(row)
            self.tree.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4]))
        self.tree.bind('<<TreeviewSelect>>', self.active_btn)
        self.c.close()

    def name_state(self,e):
        if self.e1.get() == "" and (self.cmb.get() == "Select State" or self.cmb.get() == "None") :
            print("none selected")
            self.show()
        elif self.e1.get() == "" and self.cmb.get() != "Select State":
            print("combo selected")
            self.combo_select(1)
        elif self.e1.get() != "" and (self.cmb.get() == "Select State" or self.cmb.get() == "None"):
            print("name selected")
            self.select_name(1)
        else:
            print("both selected")
            name1=self.e1.get()
            state1=self.cmb.get()
            self.c.close()
            self.c = self.con.cursor()
            lst = self.c.execute('select * from donor where dname like ? and state=?',(name1 + '%',state1))
            lst = [row for row in lst]
            print(lst)
            for i in self.tree.get_children():
                self.tree.delete(i)

            for row in lst:
                # print(row)
                self.tree.insert('', 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4]))

            self.con.commit()
            self.c.close()

        #self.pdf_state()
        #self.pdf_name()

    def pdf_name(self):
        count=1
        p = canvas.Canvas("Donor_Details.pdf", pagesize=portrait(A4))
        self.pdf_layout(p,count,"","")


        self.c.close()
        self.c = self.con.cursor()
        t = self.tree.item(self.tree.selection())['values']
        print(t)
        print(t[0])
        lst = self.c.execute('select donor.did,state,dname,blood_grp,quantity,date from Donor,donate where donate.did=donor.did and donor.did=? order by date desc',(t[0],))
        lst = [row for row in lst]
        print(lst)
        print(len(lst))

        name1 = lst[0][2]
        print(name1)
        p.drawCentredString(240, 770, name1)
        state1 = lst[0][1]
        print(state1)
        p.drawCentredString(240, 745, state1)
        did1 = lst[0][0]
        print(did1)
        p.drawCentredString(240, 720, did1)

        m = 1
        y = 650
        for i in range(len(lst)):
            p.drawCentredString(40, y, str(m))
            blood_group = lst[i][3]
            print(lst[i][3])
            p.drawCentredString(125, y, blood_group)
            qty = lst[i][4]
            print(lst[i][4])
            p.drawCentredString(280, y, str(qty))
            date_donation = lst[i][5]
            print(lst[i][5])
            p.drawCentredString(455, y, date_donation)
            y = y - 195
            m = m + 1
            if y<=70:
                p.showPage()
                self.pdf_cont_layout(p)
                y=730



        p.save()

    def pdf_state(self):
        self.c.close()
        self.c = self.con.cursor()
        # page formatting
        # up-down-ri8-left

        count=0
        p = canvas.Canvas("Full_Donor_Report.pdf")
        #self.pdf_layout(p)

        #self.pdf_layout(p, 1, 'jhgfgfhg')
        print("outside all loop")
        lst = self.c.execute("select state,count(*) from donor group by state order by state")
        lst = [row for row in lst]
        print(lst)
        print("number of states=",len(lst))

        for i in range(len(lst)):
            print("inside i loop")
            n=0
            print("state in loop=",lst[i][n])
            #p.drawCentredString(240, y - 10, lst[i][n])
            #y = y - 25


            did_lst = self.c.execute("select donor.did,count(*) from donate,donor where donor.did=donate.did and state=? group by donor.did",(lst[i][n],))
            did_lst = [row for row in did_lst]
            print(did_lst)
            print(lst[i][0])
            #self.pdf_layout(p,"",lst[i][0],"")
            #p.showPage()

            #print(len(did_lst))
            for j in range(len(did_lst)):
                print("inside j loop")
                count=count+1
                all_lst = self.c.execute("select * from donate where did=?",(did_lst[j][0],))
                all_lst = [row for row in all_lst]
                print(all_lst)
                print(len(all_lst))
                print(did_lst[j][0])
                self.pdf_layout(p,count,lst[i][0],did_lst[j][0])

                name_lst = self.c.execute("select dname from donor where did=?", (did_lst[j][0],))
                name_lst = [row for row in name_lst]
                print(name_lst[0][0])
                p.drawCentredString(240, 745, name_lst[0][0])
                y=650
                sl_no=1
                for k in all_lst:
                    p.setFont('Helvetica', 15, leading=None)
                    #self.pdf_layout(p, count, lst[i][0], did_lst[j][0])
                    print(k)
                    print("tid=",k[0])
                    print("did=",k[1])

                    print("blood_grp=",k[2])
                    p.drawCentredString(125, y, k[2])
                    print("qty=",k[3])
                    p.drawCentredString(280, y, str(k[3]))
                    print("date=",k[4])
                    p.drawCentredString(455, y, k[4])
                    p.drawCentredString(40, y, str(sl_no))
                    y=y-20
                    sl_no = sl_no+1
                p.showPage()




#d_report()

        # print("no of names in ", lst[i][0], "=", len(did_lst))

        ''' prev_did = str(0)
         y = 650
         sl_no=0
         for j in range(len(name_lst)):

             if prev_did == name_lst[j][0]:

                 print("blood_grp=", name_lst[j][3])
                 p.drawCentredString(125, y-20, name_lst[j][3])
                 print("quantity=", name_lst[j][4])
                 p.drawCentredString(280, y-20, str(name_lst[j][4]))
                 print("date of donation=", name_lst[j][5])
                 p.drawCentredString(455, y-20, name_lst[j][5])
                 y=y-20
                 p.drawCentredString(40, y, str(sl_no))
                 sl_no = sl_no + 1
                 print(count,'00000000000000')
                 #return
             else:
                 sl_no = 1
                 if prev_did!='0':
                     count=count+1
                     p.showPage()
                 p.showPage()
                 p.pagesize=portrait(A4)
                 self.pdf_layout(p,count)
                 print("did=", name_lst[j][0])
                 p.drawCentredString(240, 720, name_lst[j][0])
                 print("name=", name_lst[j][1])
                 p.drawCentredString(240, 745, name_lst[j][1])
                 print("state=", name_lst[j][2])
                 p.drawCentredString(240, 770, name_lst[j][2])
                 print("blood_grp=", name_lst[j][3])
                 p.drawCentredString(125, 650, name_lst[j][3])
                 print("quantity=", name_lst[j][4])
                 p.drawCentredString(280, 650, str(name_lst[j][4]))
                 print("date of donation=", name_lst[j][5])
                 p.drawCentredString(455, 650, name_lst[j][5])
                 p.drawCentredString(40, 650, str(sl_no))
                 #print("serial no=", sl_no)
                 sl_no=sl_no+1

                 #p.showPage()
                 #self.pdf_layout(p,count)
                 prev_did = name_lst[j][0]'''

        p.save()

