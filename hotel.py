from tkinter import *
# for importing images "pip install pillow for installition "
from PIL import Image, ImageTk
#from filename imprt className
from customer import Customer_Window #importing customer
from room import Roombooking #importing Room
from developer import Developer
from details import DetailsRoom



class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ---------------- IST IMAGE --------------------------------
        img1 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\hotel images\umer2222222.jpg") #import image
        img1 = img1.resize((1550, 140), Image.ANTIALIAS) #resizing image
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4,relief=RIDGE) #To show image on window we use label
        lblimg.place(x=0,y=0,width=1550,height=140)                        #Where to show image on the window

        # -----------------   LOGO   -----------------------------------
        img2 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\hotel images\logo_ume.jpg")  # import image
        img2 = img2.resize((230, 140), Image.ANTIALIAS)  # resizing image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)  # To show image on window we use label
        lblimg.place(x=0, y=0, width=230, height=140)                       # Where to show image on the window

        #-------------------     TITLE -----------------------------------
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="#708090",fg="#0C090A",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        #----------------------   MAIN FRAME -----------------------------
        main_frame = Frame(self.root, bd=4 , relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #------------------------    Menu ---------------------------------------
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="#708090",fg="#0C090A", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ----------------------   BUTTON FRAME -----------------------------
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER",command=self.cust_details, width=22,font=("times new roman", 14, "bold"), bg="#708090",fg="#0C090A",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking ,width=22, font=("times new roman", 14, "bold"), bg="#708090",fg="#0C090A", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS" ,command=self.detailsRoom,width=22, font=("times new roman", 14, "bold"), bg="#708090",fg="#0C090A", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0,pady=1)

        report_btn = Button(btn_frame, text="DEVELOPER",command=self.developer ,width=22, font=("times new roman", 14, "bold"), bg="#708090",fg="#0C090A", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="#708090",fg="#0C090A", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0,pady=1)


        #------------------------ RIGHT SIDE IMAGE -------------------------------------
        img3 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\hotel images\umerrrrrrrrrr.jpg")  # import image
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)  # resizing image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)  # To show image on window we use label
        lblimg1.place(x=225, y=0, width=1310, height=590)

        #---------- two images below buttons ----------------------------------------------
        img4 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\hotel images\pexels-castorly-stock-3761182.jpg")  # import image
        img4 = img4.resize((230, 180), Image.ANTIALIAS)  # resizing image
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)  # To show image on window we use label
        lblimg1.place(x=0, y=225, width=230, height=180)

        img5 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\hotel images\pexels-daniel-frese-2983472.jpg")  # import image
        img5 = img5.resize((230, 180), Image.ANTIALIAS)  # resizing image
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)  # To show image on window we use label
        lblimg1.place(x=0, y=400, width=230, height=180)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Window(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def detailsRoom(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)









    #call object in main function
if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()