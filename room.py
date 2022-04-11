from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Booking ")
        self.root.geometry("1125x500+232+226")

        #====================Variables =================

        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()



        # -------------------     TITLE -----------------------------------
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="#708090",fg="#0C090A", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)

        # -----------------   LOGO   -----------------------------------
        img2 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\logo_ume.jpg")  # import image
        img2 = img2.resize((100, 40), Image.ANTIALIAS)  # resizing image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=5, width=100, height=40)

        # ---------------label frame -----------------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=440)

        # -------------------------- labels and enteries ------------------
        # customer contact
        lbl_cust_contact = Label(labelframeleft, text="Customer  Contact ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=18,font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)

        # Fetch Data buttton
        btnFetchData = Button(labelframeleft, text="Fetch Data",command=self.Fetch_contact,font=("arial", 11, "bold"), bg="black", fg="gold",width=8, )
        btnFetchData.place(x=330,y=4)

        # customer checkin data
        check_in_data = Label(labelframeleft, text="Check In Data ", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_data.grid(row=1, column=0, sticky=W)
        txtcheck_in_data = ttk.Entry(labelframeleft,textvariable=self.var_checkin , width=26, font=("arial", 13, "bold"))
        txtcheck_in_data.grid(row=1, column=1)

        # customer check out data
        check_out_data = Label(labelframeleft, text="Check Out Data ", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_data.grid(row=2, column=0, sticky=W)
        txtcheck_out_data = ttk.Entry(labelframeleft, textvariable=self.var_checkout,width=26, font=("arial", 13, "bold"))
        txtcheck_out_data.grid(row=2, column=1)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="ume2119",
            database="management",

        )
        my_cursor = conn.cursor()
        my_cursor.execute("select roomType from details")
        roomTypedata = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft,  textvariable=self.var_roomtype,width=26, font=("arial", 12, "bold"),state="readonly")
        combo_RoomType["value"] = roomTypedata
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Avaliable room
        lblAvaliableRoom = Label(labelframeleft, text="Avaliable Room", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAvaliableRoom.grid(row=4, column=0, sticky=W)
        # txtAvaliableRoom = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, width=26, font=("arial", 13, "bold"))
        # txtAvaliableRoom.grid(row=4, column=1)

        #Creating data base to fetch data from details data base
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="ume2119",
            database="management",

        )
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()



        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, width=26,font=("arial", 12, "bold"), state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # # Meal
        lblMeal = Label(labelframeleft, text="Meal", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft,textvariable=self.var_meal, width=26, font=("arial", 13, "bold"))
        txtMeal.grid(row=5, column=1)

        # No of days
        lblNoOfDays = Label(labelframeleft, text="No Of Days", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, width=26, font=("arial", 13, "bold"))
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        # lblNoOfDays = Label(labelframeleft, text="Paid Tax", font=("arial", 12, "bold"), padx=2, pady=6)
        # lblNoOfDays.grid(row=7, column=0, sticky=W)
        # txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_paidtax ,width=26, font=("arial", 13, "bold"))
        # txtNoOfDays.grid(row=7, column=1)

        # Sub Total
        lblNoOfDays = Label(labelframeleft, text="Sub Total", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal,width=26, font=("arial", 13, "bold"))
        txtNoOfDays.grid(row=8, column=1)

        # Total Cost
        lblNoOfDays = Label(labelframeleft, text="Total Cost", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=9, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_total ,width=26, font=("arial", 13, "bold"))
        txtNoOfDays.grid(row=9, column=1)


        #====================Bill Button+++++++++++++++=

        btnBill = Button(labelframeleft, text="Bill",command=self.total ,font=("arial", 13, "bold"), bg="black", fg="gold",
                        width=9, )
        btnBill.grid(row=10, column=0, padx=1,sticky=W)

        # ----------------------------------Buttons-----------------------

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=370, width=414, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data ,font=("arial", 13, "bold"), bg="black", fg="gold",
                        width=9, )
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update ,font=("arial", 13, "bold"), bg="black",
                           fg="gold", width=9, )
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelet = Button(btn_frame, text="Delete", command=self.delete ,font=("arial", 13, "bold"), bg="black",
                          fg="gold", width=9, )
        btnDelet.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset , font=("arial", 13, "bold"), bg="black",
                          fg="gold", width=9, )
        btnReset.grid(row=0, column=3, padx=1)

        #==============================Right Side Image===========================

        img3 = Image.open(r"C:\Users\UMER\Desktop\UMER\Hotel_management\hotel images\bed.jpg")  # import image
        img3 = img3.resize((300, 300), Image.ANTIALIAS)  # resizing image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=820, y=55, width=300, height=250)




        # ----------------------- Table framesearch system -------------------------------------
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM",
                                 font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=433, y=250, width=693, height=240)

        lblSearchBy = Label(Table_Frame, text="SEARCH BY", bg="gold", fg="white", font=("arial", 12, "bold"))
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, width=20, textvariable=self.search_var, font=("arial", 12, "bold"),
                                    state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        txtIdSearch = ttk.Entry(Table_Frame, textvariable=self.text_search, width=20, font=("arial", 13, "bold"))
        txtIdSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("arial", 13, "bold"), bg="black",
                           fg="gold", width=9, )
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show ",command=self.fetch_data,font=("arial", 13, "bold"), bg="black",
                            fg="gold", width=9, )
        btnShowAll.grid(row=0, column=4, padx=1)

        # ------------------   Show Data Table --------------------------

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=683, height=160)

        # Scroll bar creation   for x and y
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.room_table= ttk.Treeview(details_table, columns=(
            "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal",
            "noOfdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Checkin")
        self.room_table.heading("checkout", text="Checkout")
        self.room_table.heading("roomtype", text="RoomType")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")

        # --------------TO show ------------------------------------
        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays",width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


        #==========add button================

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error","All Fields are required ....",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username = "root",
                    password = "ume2119",
                    database = "management" ,

                    )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values (%s , %s,%s , %s,%s , %s,%s  )",(
                                            self.var_contact.get(),
                                            self.var_checkin.get(),
                                            self.var_checkout.get(),
                                            self.var_roomtype.get(),
                                            self.var_roomavailable.get(),
                                            self.var_meal.get(),
                                            self.var_noofdays.get()

                                                      ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent = self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong : {str(es)}",parent = self.root)



    #=================To Fetch dat ================

    def fetch_data(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="ume2119",
            database="management",

        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows :
                self.room_table.insert("",END,values=i)

            conn.commit()
            conn.close()

    #==================Get Cursor==============

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])


    #===================Update ===================
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error","Please Enter Mobile Number.",parent=self.root)

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ume2119",
                database="management",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s , check_out=%s , roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s where Contact =%s",(

                                                                self.var_checkin.get(),
                                                                self.var_checkout.get(),
                                                                self.var_roomtype.get(),
                                                                self.var_roomavailable.get(),
                                                                self.var_meal.get(),
                                                                self.var_noofdays.get(),
                                                                self.var_contact.get()

                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details Has Been Updated Successfully.",parent=self.root)

    #=====================delete Function =============================

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System","Do You Want To Delete This Customer",parent = self.root)
        if delete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ume2119",
                database="management",
            )
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    #=================Reset function

    def reset(self):
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        # self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_contact.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")




    #============Calculation Function for total============
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        if(self.var_meal.get()=="BreakFast" or self.var_roomtype.get()=="Laxuary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" %((q5)*0.9))
            subtotal = "Rs."+str("%.2f" %((q5)))
            Total= "Rs."+str("%.2f" %(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(Total)

        elif (self.var_meal.get() == "BreakFast" or self.var_roomtype.get() == "Double"):
            q1 = float(100)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.9))
            subtotal = "Rs." + str("%.2f" % ((q5)))
            Total = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(Total)
        else:
            q1 = float(100)
            q2 = float(200)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.9))
            subtotal = "Rs." + str("%.2f" % ((q5)))
            Total = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(Total)





    #================ALL DATA FETCH IN BOX =========================

    def Fetch_contact(self):
        if self.var_contact.get()== "":
            messagebox.showerror("Error","Please Enter Contact Number.",parent=self.root)

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ume2119",
                database="management",
            )
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            values = (self.var_contact.get(),)
            my_cursor.execute(query,values)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","This Number is Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe = Frame(self.root,border=4,relief=RIDGE,padx=2)
                showDataframe.place(x=455,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name :",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90, y=0)

                #========For gender ==========
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ume2119",
                    database="management",
                )
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                values = (self.var_contact.get(),)
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender :", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)
                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                # ========For Email ==========
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ume2119",
                    database="management",
                )
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                values = (self.var_contact.get(),)
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email :", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)
                lbl3 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                # ========For Address ==========
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ume2119",
                    database="management",
                )
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                values = (self.var_contact.get(),)
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataframe, text="Address :", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=90)
                lbl4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                # ========For Id NUmber ==========
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ume2119",
                    database="management",
                )
                my_cursor = conn.cursor()
                query = ("select idnumber from customer where Mobile=%s")
                values = (self.var_contact.get(),)
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()

                lblidnumber = Label(showDataframe, text="IdNumber:", font=("arial", 12, "bold"))
                lblidnumber.place(x=0, y=120)
                lbl5 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)

                # ========For Id Proof Type ==========
                # conn = mysql.connector.connect(
                #     host="localhost",
                #     username="root",
                #     password="ume2119",
                #     database="management",
                # )
                # my_cursor = conn.cursor()
                # query = ("select idproof from customer where Mobile=%s")
                # values = (self.var_contact.get(),)
                # my_cursor.execute(query, values)
                # row = my_cursor.fetchone()
                #
                # lblidproof = Label(showDataframe, text="IdProof:", font=("arial", 12, "bold"))
                # lblidproof.place(x=0, y=150)
                # lbl6 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                # lbl6.place(x=90, y=150)












        #call object in main function
if __name__ == '__main__':
    root = Tk()
    obj = Roombooking(root) #class name
    root.mainloop()