from tkinter import*
from tkinter import ttk
from tkinter import font
from random import randint
from PIL import ImageTk,Image
from tkinter import messagebox as msg

class about:
    def __init__(self):
        self.root=Toplevel()
        #######self.root = Tk()
        self.root.geometry("950x310+300+180")
        self.root.resizable(width=False,height=False)
        self.root.title("DSR About_Us")
        self.root.config(bg="lightblue")

        self.frm1 = Frame(self.root,width=945,height=55, relief="ridge", bg='#99004d', bd=5)
        self.frm1.place(x=3, y=0)

        self.frm2 = Frame(self.root, width=580, height=252, relief="ridge", bg='#99004d', bd=5)
        self.frm2.place(x=3, y=55)

        self.frm3 = Frame(self.root, width=365, height=252, relief="ridge", bg='#99004d', bd=5)
        self.frm3.place(x=583, y=55)

        self.l1 = Label(self.frm1, text="ABOUT US", font=('Helvetica', 23, font.BOLD), width=20, bg='#99004d', fg="white")
        self.l1.place(x=280, y=3)

        self.l2 = Label(self.frm3, text="Give the Gift of Life.....\n Donate Blood\n DSR is aimed to highlight the importance of \n giving blood and plasma regularly so that \n patients can recieve timely treatments.\n\n The need for blood is \n Universal,but access to\n blood is not.", font=('Helvetica', 12, font.BOLD), width=34,height=12, bg='white',fg="black")
        self.l2.place(x=3, y=3)

        #self.img = ImageTk.PhotoImage(file="E:\\python_projects\\blood_bank\\images\\image3.jpeg")
        self.img = ImageTk.PhotoImage(file="images/image3.jpeg")
        print(self.img)
        l_img = Label(self.frm2, height=235, width=563, image=self.img)
        l_img.place(x=1, y=1)


        self.l1.focus_force()
        self.root.mainloop()
####about()