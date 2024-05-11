from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image
from tkinter import messagebox as msg

class contact:
    def __init__(self):
        self.root=Toplevel()
        ######self.root = Tk()
        self.root.geometry("915x465+300+120")
        self.root.resizable(width=False,height=False)
        self.root.title("DSR Contact_Us")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root,width=910,height=55, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=3, y=0)

        self.frm2 = Frame(self.root, width=598, height=408, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=3, y=55)

        self.frm3 = Frame(self.root, width=312, height=408, relief="ridge", bg='#99004d', bd=5)
        self.frm3.place(x=601, y=55)

        self.l1 = Label(self.frm1, text="CONTACT US", font=('Helvetica', 23, font.BOLD), width=20, bg='#99004d', fg="white")
        self.l1.place(x=250, y=3)

        self.l2 = Label(self.frm3, text="Helpline No.", font=('Helvetica', 17, font.BOLD), width=12, bg='#99004d',fg="white")
        self.l2.place(x=8, y=20)

        self.l3 = Label(self.frm3, text="98565 69535 / 85974 25489", font=('Helvetica', 12, font.BOLD), width=20, bg="white")
        self.l3.place(x=18, y=51)

        self.l4 = Label(self.frm3, text="Email Id", font=('Helvetica', 17, font.BOLD), width=8, bg='#99004d',fg="white")
        self.l4.place(x=8, y=100)

        self.l5 = Label(self.frm3, text="dsr_2000@gmail.com", font=('Helvetica', 12, font.BOLD), width=20, bg="white")
        self.l5.place(x=18, y=135)

        self.l6 = Label(self.frm3, text="Address", font=('Helvetica', 17, font.BOLD), width=9, bg='#99004d',fg="white")
        self.l6.place(x=8, y=184)

        self.l7 = Label(self.frm3, text="79/A,Bylane,Keoratola(Opp.Abahan Hall)", font=('Helvetica', 11, font.BOLD), width=31, bg="white")
        self.l7.place(x=11, y=219)

        #self.img = ImageTk.PhotoImage(file="E:\\python_projects\\blood_bank\\images\\image21.jpeg")
        self.img = ImageTk.PhotoImage(file="images/image21.jpeg")
        print(self.img)
        l_img = Label(self.frm2, height=390, width=580, image=self.img)
        l_img.place(x=1, y=1)

        self.l1.focus_force()
        self.root.mainloop()
#contact()