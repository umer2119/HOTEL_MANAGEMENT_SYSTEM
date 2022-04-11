from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Details ")
        self.root.geometry("1125x500+232+226")
        # -------------------     TITLE -----------------------------------
        lbl_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 18, "bold"), bg="#708090",
                          fg="#0C090A", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)

        # -----------------   LOGO   -----------------------------------
        img2 = Image.open(r"C:\Users\UMER\Desktop\UMER\HOTE_MANAGEMENT_FINAL\logo_ume.jpg")  # import image
        img2 = img2.resize((100, 40), Image.ANTIALIAS)  # resizing image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=5, width=100, height=40)

        # ---------------label frame -----------------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=500, height=350)

        # -------------------------- labels and enteries ------------------
        # floor
        lbl_floor = Label(labelframeleft, text="Floor ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor ,width=18, font=("arial", 13, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)


        # Room No
        lbl_RoomNo = Label(labelframeleft, text="Room No. ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)
        self.var_roomNo = StringVar()
        entry_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_roomNo ,width=18, font=("arial", 13, "bold"))
        entry_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_RoomType = StringVar()
        entry_RoomType = ttk.Entry(labelframeleft,textvariable=self.var_RoomType ,width=18, font=("arial", 13, "bold"))
        entry_RoomType.grid(row=2, column=1, sticky=W)

        # ----------------------------------Buttons-----------------------

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=280, width=414, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data , font=("arial", 13, "bold"), bg="black", fg="gold",
                        width=9, )
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update ,font=("arial", 13, "bold"), bg="black",
                           fg="gold", width=9, )
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelet = Button(btn_frame, text="Delete",command=self.delete , font=("arial", 13, "bold"), bg="black",
                          fg="gold", width=9, )
        btnDelet.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset_fun, font=("arial", 13, "bold"), bg="black",
                          fg="gold", width=9, )
        btnReset.grid(row=0, column=3, padx=1)

        # ----------------------- Table framesearch system -------------------------------------
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",
                                 font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=520, height=350)

        # Scroll bar creation   for x and y
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(Table_Frame, columns=(
            "floor", "roomno", "roomType"
        ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="RoomNo")
        self.room_table.heading("roomType", text="RoomType")


        # --------------TO show ------------------------------------
        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomType", width=100)


        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # -------------------     TITLE -----------------------------------
        lbl_title = Label(self.root, text="UMER FAROOQ ", font=("times new roman", 18, "bold"), bg="#708090",
                          fg="#0C090A", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=420, width=1125, height=50)


    #==============addd data ==============
    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
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
                my_cursor.execute("insert into details values (%s , %s,%s   )",(
                                            self.var_floor.get(),
                                            self.var_roomNo.get(),
                                            self.var_RoomType.get()


                                                      ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully!",parent = self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong : {str(es)}",parent = self.root)

    #=========Fetch ============

    def fetch_data(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="ume2119",
            database="management",

        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows :
                self.room_table.insert("",END,values=i)

            conn.commit()
            conn.close()

    #============get Cursor ============

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])

    #============= Update

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error","Please Enter Floor Prefectly!.",parent=self.root)

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ume2119",
                database="management",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s ,roomType=%s where RoomNo=%s",(

                                                                self.var_floor.get(),
                                                                self.var_RoomType.get(),
                                                                self.var_roomNo.get(),


                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room Details Has Been Updated Successfully.",parent=self.root)

    #reset

    def reset_fun(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")


    #======Delete=========

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System","Do You Want To Delete!",parent = self.root)
        if delete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="ume2119",
                database="management",
            )
            my_cursor = conn.cursor()
            query = "delete from details where RoomNo=%s"
            value = (self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()






















        #call object in main function
if __name__ == '__main__':
    root = Tk()
    obj = DetailsRoom(root) #class name
    root.mainloop()