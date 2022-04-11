from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Customer_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1125x500+232+226")


        #----------------------variables ------------------------
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_natinality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # -------------------     TITLE -----------------------------------
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="#708090",fg="#0C090A", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)

        # -----------------   LOGO   -----------------------------------
        img2 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\logo_ume.jpg")  # import image
        img2 = img2.resize((100, 40), Image.ANTIALIAS)  # resizing image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=5, width=100, height=40)

        #---------------label frame -----------------------
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=440)

        #-------------------------- labels and enteries ------------------
        #customer refrence
        lbl_cust_ref = Label(labelframeleft,text="Customer Ref ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref,width=26,state="readonly",font=("arial",13,"bold"))
        entry_ref.grid(row=0,column=1)

        #customer name
        cname = Label(labelframeleft, text="Customer Name ", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name, width=26, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)


        ##mother name
        # lblname = Label(labelframeleft, text="Mother Name ", font=("arial", 12, "bold"), padx=2, pady=6)
        # lblname.grid(row=2, column=0, sticky=W)
        # txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother ,width=26, font=("arial", 13, "bold"))
        # txtmname.grid(row=2, column=1)

        #gender
        label_gender = Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=26,font=("arial", 12, "bold"),state="readonly")
        combo_gender["value"] =("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #post code
        lblPostCode = Label(labelframeleft, text="Post Code ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post,width=26, font=("arial", 13, "bold"))
        txtPostCode.grid(row=4, column=1)

        #Mobile number
        lblMobile = Label(labelframeleft, text="Mobile Number ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile,width=26, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        #email
        lblEmail = Label(labelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email,width=26, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        #nationality
        # lblNationality = Label(labelframeleft, text="Nationality ", font=("arial", 12, "bold"), padx=2, pady=6)
        # lblNationality.grid(row=7, column=0, sticky=W)
        #
        # combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_natinality, width=26, font=("arial", 12, "bold"), state="readonly")
        # combo_Nationality["value"] = ("Indian", "British", "American")
        # combo_Nationality.current(0)
        # combo_Nationality.grid(row=7, column=1)

        #idproof type
        lblIdProof = Label(labelframeleft, text="Id Proof Type ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_Id = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof,width=26, font=("arial", 12, "bold"), state="readonly")
        combo_Id["value"] = ("PassPort", "Adhaar", "Driving License","Pan Card")
        combo_Id.current(0)
        combo_Id.grid(row=8, column=1)


        #id number
        lblIdNumber = Label(labelframeleft, text="Id Proof Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number,width=26, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        #address
        lblAddress = Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_address, width=26, font=("arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)


        #----------------------------------Buttons-----------------------

        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=370,width=414,height=40)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("arial", 13, "bold"),bg="black",fg="gold",width=9,)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update ,font=("arial", 13, "bold"), bg="black", fg="gold", width=9, )
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelet = Button(btn_frame, text="Delete",command=self.delete ,font=("arial", 13, "bold"), bg="black", fg="gold", width=9, )
        btnDelet.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset ,font=("arial", 13, "bold"), bg="black", fg="gold", width=9, )
        btnReset.grid(row=0, column=3, padx=1)


        #----------------------- Table framesearch system -------------------------------------
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM",
                                    font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=433, y=50, width=693, height=440)

        lblSearchBy = Label(Table_Frame, text="SEARCH BY", bg="gold",fg="white",font=("arial", 12, "bold"))
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, width=20,textvariable=self.search_var ,font=("arial", 12, "bold"), state="readonly")
        combo_Search["value"] = ("Ref NO.", "Mobile No.")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        self.text_search = StringVar()
        txtIdSearch = ttk.Entry(Table_Frame,textvariable=self.text_search, width=20, font=("arial", 13, "bold"))
        txtIdSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search,font=("arial", 13, "bold"), bg="black", fg="gold", width=9, )
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show ",command=self.fetch_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9, )
        btnShowAll.grid(row=0, column=4, padx=1)

        #------------------   Show Data Table --------------------------

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=683, height=320)

        #Scroll bar creation   for x and y
        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.Cust_Details_Table = ttk.Treeview(details_table,columns=(
            "ref", "name","mother", "gender","post","mobile",
            "email","nationality",
            "idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No.")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        #--------------TO show ------------------------------------
        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_mobile.get() == "" or self.var_cust_name.get() == "":
            messagebox.showerror("Error","All Fields are required ....",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username = "root",
                    password = "ume2119",
                    database = "management" ,
                    # auth_plugin = "mysql_native_password"       
                    )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values (%s , %s,%s , %s,%s , %s,%s , %s,%s , %s,%s )",(
                                                            self.var_ref.get(),
                                                            self.var_cust_name.get(),
                                                            self.var_mother.get(),
                                                            self.var_gender.get(),
                                                            self.var_post.get(),
                                                            self.var_mobile.get(),
                                                            self.var_email.get(),
                                                            self.var_natinality.get(),
                                                            self.var_id_proof.get(),
                                                            self.var_id_number.get(),
                                                            self.var_address.get()
                                                      ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent = self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong : {str(es)}",parent = self.root)


    #-----------To fetch data from data base and show in the frame -----------------------

    def fetch_data(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="ume2119",
            database="management",
            # auth_plugin = "mysql_native_password"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows :
                self.Cust_Details_Table.insert("",END,values=i)

            conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_natinality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    #------------------Update function ----------------------

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error","Please Enter Mobile Number.",parent=self.root)

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ume2119",
                database="management",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s , Mother= %s,Gender=%s,PostCode=%s,Mobile=%s ,Email=%s,Nationality=%s,idproof=%s,idnumber=%s,Address=%s where Ref=%s",(

                                                                self.var_cust_name.get(),
                                                                self.var_mother.get(),
                                                                self.var_gender.get(),
                                                                self.var_post.get(),
                                                                self.var_mobile.get(),
                                                                self.var_email.get(),
                                                                self.var_natinality.get(),
                                                                self.var_id_proof.get(),
                                                                self.var_id_number.get(),
                                                                self.var_address.get(),
                                                                self.var_ref.get()
                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Has Been Updated Successfully.",parent=self.root)


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
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_natinality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="ume2119",
            database="management",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.text_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()













        #call object in main function
if __name__ == '__main__':
    root = Tk()
    obj = Customer_Window(root) #class name
    root.mainloop()