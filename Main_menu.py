import sqlite3
from tkinter import *
from PIL import Image,ImageTk
from tkinter import font
from tkinter import Menu

from Donor_details import Donor_details
from Buyer_details import Buyer_details
from Donate_details import Donation
from Donor_report import d_report
from Stock import stock
from Donor_transaction import d_trans
from buyer_transaction import b_trans
from Blood_claim import BLOOD_CLAIM
from contact_us import contact
from Buyer_report import b_report
from about_us import about
class main_menu:
    def __init__(self):
        self.con=sqlite3.connect('database/bloodbank.db')
        self.c=self.con.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS donor(did text primary key,dname text,phone number,state text,address text)')
        self.c.execute('CREATE TABLE IF NOT EXISTS buyer(bid text primary key,bname text,phone number,state text,address text)')
        self.c.execute('CREATE TABLE IF NOT EXISTS donate(tid text primary key,did text references donor(did),blood_grp text,quantity number,date text)')
        self.c.execute('CREATE TABLE IF NOT EXISTS blood_claim(sid text primary key,bid text references buyer(bid),s_date text,blood_grp text,quantity number,cost number)')
        self.c.execute('CREATE TABLE IF NOT EXISTS stock(blood_group,quantity number,cost number)')

        self.c.close()
        self.root=Tk()
        self.root.geometry('1520x782+0+0')
        self.root.title('DSR Blood Bank')
        self.root.resizable(width=False, height=False)

        self.menubar=Menu(self.root)

        self.admin=Menu(self.menubar,tearoff=False)
        self.donor=Menu(self.menubar,tearoff=False)
        self.buyer = Menu(self.menubar,tearoff=False)
        self.help = Menu(self.menubar,tearoff=1)


        self.menubar.add_cascade(label='Admin', menu=self.admin)
        #######self.admin.add_cascade(label='Donor Details',command=self.click)
        self.admin.add_cascade(label='Display Stock',command=lambda:self.click('New Display'))
        self.t_submenu=Menu(self.admin,tearoff=False)
        self.t_submenu.add_command(label="Donor Transactions",command=lambda:self.click('d_transaction'))
        self.t_submenu.add_command(label="Buyer Transactions",command=lambda:self.click('b_transaction'))
        self.admin.add_cascade(label='Display Transactions Historys',menu=self.t_submenu)
        self.admin.add_separator()
        self.admin.add_cascade(label='EXIT',command = self.root.destroy)


        self.menubar.add_cascade(label='Donor', menu=self.donor)
        self.donor.add_cascade(label='Donor Details Entry',command=lambda:self.click('New Donor'))
        ####self.donor.add_cascade(label='Donor Details Entry')
        self.donor.add_cascade(label='Donation Details',command=lambda:self.click('Donation'))
        self.donor.add_cascade(label='Donor Report',command=lambda:self.click('Donor_Report'))


        self.menubar.add_cascade(label='Buyer', menu=self.buyer)
        self.buyer.add_cascade(label='Buyer Details Entry',command=lambda:self.click('New Buyer'))
        self.buyer.add_cascade(label='Blood Claim Details',command=lambda:self.click('Blood Claim'))
        #self.buyer.add_cascade(label='Blood Claim Details')
        self.buyer.add_cascade(label='Buyer Report',command=lambda:self.click('Buyer Report'))

        self.menubar.add_cascade(label='Help', menu=self.help)
        self.help.add_cascade(label='About Us',command=lambda:self.click('about_us'))
        self.help.add_cascade(label='Contact Us',command=lambda:self.click('Contact'))

        self.root.config(menu=self.menubar,bg='#99004d')


        self.img=ImageTk.PhotoImage(file="images/23.jpg")
        self.l = Label(self.root,image=self.img)
        self.l.place(x=55, y=10)
        self.l.focus_force()
        self.root.mainloop()

    def click(self,text):
        if text=='New Donor':
            Donor_details(self.con)
        if text == 'Donation':
            Donation(self.con)
        if text == 'Donor_Report':
            d_report(self.con)
        if text=='New Buyer':
            Buyer_details(self.con)
        if text == 'Buyer Report':
            b_report(self.con)
        if text=='Blood Claim':
            BLOOD_CLAIM(self.con)
        if text=='New Display':
            stock(self.con)
        if text=='Contact':
            contact()
        if text=='d_transaction':
            d_trans(self.con)
        if text=='b_transaction':
            b_trans(self.con)
        if text == 'about_us':
            about()




#main_menu()