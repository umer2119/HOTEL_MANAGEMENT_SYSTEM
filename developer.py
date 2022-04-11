from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Developer Details")
        self.root.geometry("1125x500+232+226")
        # -------------------     TITLE -----------------------------------
        lbl_title = Label(self.root, text="ABOUT DEVELOPER", font=("times new roman", 18, "bold"), bg="#708090",
                          fg="#0C090A", bd=10, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)

        # -------------------     TITLE -----------------------------------
        lbl_title = Label(self.root, text="ABOUT DEVELOPER", font=("times new roman", 18, "bold"), bg="#708090",
                          fg="#0C090A", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)

        # -----------------   LOGO   -----------------------------------
        img2 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\logo_ume.jpg")  # import image
        img2 = img2.resize((100, 40), Image.ANTIALIAS)  # resizing image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=5, width=100, height=40)

        # ---------------label frame -----------------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ABOUT ME ",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=500, height=350)

        # -------------------------- labels and enteries ------------------
        # Developer Name
        lbl_d_name = Label(labelframeleft, text="Name : UMER FAROOQ ", font=("arial", 20, "bold"),
                          fg="#0C090A", padx=2, pady=6)
        lbl_d_name.grid(row=0, column=0, sticky=W)

        # s/0
        lbl_d_name = Label(labelframeleft, text="S/O: FAROOQ AHMAD LONE", font=("arial", 20, "bold"),
                           fg="#0C090A", padx=2, pady=6)
        lbl_d_name.grid(row=1, column=0, sticky=W)

        # Branch Sem
        lbl_d_name = Label(labelframeleft, text="Cse - 7th SEM ", font=("arial", 20, "bold"),
                           fg="#0C090A", padx=2, pady=6)
        lbl_d_name.grid(row=2, column=0, sticky=W)

        # College
        lbl_d_name = Label(labelframeleft, text="College : SSM COLLEGE OF ENG & TECH.", font=("arial", 18, "bold"),
                           fg="#0C090A", padx=2, pady=6)
        lbl_d_name.grid(row=3, column=0, sticky=W)

        # email
        lbl_d_name = Label(labelframeleft, text="Email: dumkdmi19@gmail.com", font=("arial", 20, "bold"),
                           fg="#0C090A", padx=2, pady=6)
        lbl_d_name.grid(row=4, column=0, sticky=W)

        # contact
        lbl_d_name = Label(labelframeleft, text="Contact: 9541130064", font=("arial", 20, "bold"),
                           fg="#0C090A", padx=2, pady=6)
        lbl_d_name.grid(row=5, column=0, sticky=W)

        # ----------------------- Table framesearch system -------------------------------------
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="UMEI 2109",
                                 font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=520, height=350)

        img6 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\1813-picsay.jpg")  # import image
        img6 = img6.resize((550, 320))  # resizing image
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg = Label(Table_Frame, image=self.photoimg6, bd=0, relief=RAISED)
        lblimg.place(x=5, y=5, width=550, height=320)

        # -------------------     TITLE -----------------------------------
        lbl_title = Label(self.root, text="UMER FAROOQ ", font=("times new roman", 18, "bold"), bg="#708090",
                          fg="#0C090A", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=420, width=1125, height=50)
















#call object in main function
if __name__ == '__main__':
    root = Tk()
    obj = Developer(root) #class name
    root.mainloop()