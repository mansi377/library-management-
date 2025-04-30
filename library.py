from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime




#variable
self.member_var=StringVar()
self.commember_var=StringVar()
self.prn_var=StringVar()
self.title_var=StringVar()
self.firstname_var=StringVar()
self.lastname_var=StringVar()
self.stream_var=StringVar()
self.commember_var=StringVar()
self.dept_var=StringVar()
self.mobile_var=StringVar()
self.booktitle_var=StringVar()
self.author_var=StringVar()
self.db_var=StringVar()
self.dd_var=StringVar()
self.daysonbook=StringVar()
self.lrf_var=StringVar()
self.dod=StringVar()
self.ap=StringVar()

class LibraryManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")





        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("Rockwell", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)


        #DataFrameLeft
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="powder blue", fg="Black", bd=12, relief=RIDGE, font=("Gill Sans MT", 16, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("Gill Sans MT",12,"bold"),textvariable=self.member_var,padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.commember_var,width=27,state="readonly")
        comMember["value"]=("Admin","Teaching Staff","Students")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN NO",font=("Gill Sans MT",12,"bold"),textvariable=self.prn_var,padx=2,pady=3)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)

        lbltitle=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.title_var,text="ID No : ",padx=2,pady=3,bg="powder blue")
        lbltitle.grid(row=2,column=0,sticky=W)
        txtTiltle=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtTiltle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.firstname_var,text="Enter Your First Name : ",padx=2,pady=3,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.lastname_var,text="Enter Your Last Name : ",padx=2,pady=3,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblStream=Label(DataFrameLeft,bg="powder blue",text="Enter Your Stream",font=("Gill Sans MT",12,"bold"),textvariable=self.stream_var,padx=2,pady=3)
        lblStream.grid(row=5,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.commember_var,width=27,state="readonly")
        comMember["value"]=("Commerce","Science","Arts")
        comMember.grid(row=5,column=1)

        lblDept=Label(DataFrameLeft,bg="powder blue",text="Choice your Department",font=("Gill Sans MT",12,"bold"),textvariable=self.dept_var,padx=2,pady=3)
        lblDept.grid(row=6,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Bsc.I.T","B-Tech","BAMMC","COMPUTER SCIENCE")
        comMember.grid(row=6,column=1)

        lblMobile=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=mobile_var,text="Enter Your Mobile No : ",padx=2,pady=3,bg="powder blue")
        lblMobile.grid(row=7,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtMobile.grid(row=7,column=1)

        lblBookTitle=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.booktitle_var,text="Enter Book Title : ",padx=2,pady=3,bg="powder blue")
        lblBookTitle.grid(row=8,column=0,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtBookTitle.grid(row=8,column=1)

        lblAuthor=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.author,text="Enter Author Name : ",padx=2,pady=3,bg="powder blue")
        lblAuthor.grid(row=9,column=0,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtAuthor.grid(row=9,column=1)

        lblDB=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.db,text="Date Borrowed : ",padx=2,pady=3,bg="powder blue")
        lblDB.grid(row=0,column=2,sticky=W)
        txtDB=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtDB.grid(row=0,column=3)

        lblDD=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.dd,text="Date Due : ",padx=2,pady=3,bg="powder blue")
        lblDD.grid(row=1,column=2,sticky=W)
        txtDD=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtDD.grid(row=1,column=3)

        lblDaysonBook=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.daysonbook_var,text="Days on Book : ",padx=2,pady=3,bg="powder blue")
        lblDaysonBook.grid(row=2,column=2,sticky=W)
        txtDaysonBook=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtDaysonBook.grid(row=2,column=3)

        lblLRF=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.lrf_var,text="Late Return Fine : ",padx=2,pady=3,bg="powder blue")
        lblLRF.grid(row=3,column=2,sticky=W)
        txtLRF=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtLRF.grid(row=3,column=3)

        lblDOD=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.dod_var,text="Date Over Date : ",padx=2,pady=3,bg="powder blue")
        lblDOD.grid(row=4,column=2,sticky=W)
        txtDOD=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtDOD.grid(row=4,column=3)

        lblAP=Label(DataFrameLeft,font=("Gill Sans MT",12,"bold"),textvariable=self.ap_var,text="Actual Price : ",padx=2,pady=3,bg="powder blue")
        lblAP.grid(row=5,column=2,sticky=W)
        txtAP=Entry(DataFrameLeft,font=("Gill Sans MT",12,"bold"),width=29)
        txtAP.grid(row=5,column=3)


        #DataFrameRight
        DataFrameRight=LabelFrame(frame,text ="Book Details", bg="powder blue", fg="Black", bd=12, relief=RIDGE, font=("Gill Sans MT", 16, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("Gill Sans MT",12,"bold"),width=32,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Python Programming','Computer Network','Applied Mathematics','Data Structures','Operating System','Numerical Methods',
                   'Core Java','Linux','C and C++','Website Development','Discrete Mathematics','Machines','DBMS','MYSQL','Green IT',
                   'Micro Processor','HTML and CSS']
        

#backend data entry

        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection))
            x=value
            if (x=="Python Programming"):
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("Python Manual")

                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 1020")

                elif (x=="Computer Network"):
                self.bookid_var.set("BKID9234")
                self.booktitle_var.set("Computer Network")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 560")



                elif (x=="Applied Mathematics"):
                self.bookid_var.set("BKID19834")
                self.booktitle_var.set("Applied Mathematics")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 920")


                elif (x=="Data Structures"):
                self.bookid_var.set("BKID9854")
                self.booktitle_var.set("Data Structures")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 450")


                elif(x=="Operating System"):
                self.bookid_var.set("BKID7894")
                self.booktitle_var.set("Operating System")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 670")


                elif(x=="Numerical Method"):
                self.bookid_var.set("BKID784")
                self.booktitle_var.set("Numerical Method")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 800")


                elif(x=="Core Java"):
                self.bookid_var.set("BKID6734")
                self.booktitle_var.set("Core Java")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 900")


                elif(x=="Linux"):
                self.bookid_var.set("BKID7651")
                self.booktitle_var.set("Linux")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 750")


                elif(x=="C and C++"):
                self.bookid_var.set("BKID89344")
                self.booktitle_var.set("C and C++")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 475")



                elif(x=="Website Development"):
                self.bookid_var.set("BKID8765")
                self.booktitle_var.set("Website Development")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 650")



                elif(x=="Discrete Mathematics"):
                self.bookid_var.set("BKID98734")
                self.booktitle_var.set("Discrete Mathematics")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 200")


                elif(x=="Machines"):
                self.bookid_var.set("BKID96534")
                self.booktitle_var.set("Machines")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 780")


                elif(x=="DBMS"):
                self.bookid_var.set("BKID19874")
                self.booktitle_var.set("DBMS")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 800")



                elif(x=="MYSQL"):
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("MYSQL")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 760")


                elif(x=="Green IT"):
                self.bookid_var.set("BKID84634")
                self.booktitle_var.set("Green IT")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 560")


                elif(x=="Micro Processor"):
                self.bookid_var.set("BKID8943")
                self.booktitle_var.set("Micro Processor")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 600")



                elif(x=="HTML and CSS"):
                self.bookid_var.set("BKID2312")
                self.booktitle_var.set("HTML and CSS")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latefine_var.set("Rs 500")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs 300")











        
        listBox=Listbox(DataFrameRight,font=("Gill Sans MT",12,"bold"),width=20,height=15)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)




        #Button Frames
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("Gill Sans MT",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("Gill Sans MT",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update Data",font=("Gill Sans MT",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete Data",font=("Gill Sans MT",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.rest,text="Reset Data",font=("Gill Sans MT",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("Gill Sans MT",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=5)


         #Information Frames
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","idno","firstname","lastname","stream","department",
                                                            "mobile","booktitle","author","dateborrowed","datedue","days","latereturnfine",
                                                            "dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)




        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("idno",text="ID No")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("stream",text="Stream")
        self.library_table.heading("department",text="Department")
        self.library_table.heading("mobile",text="Mobile No")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("stream",width=100)
        self.library_table.column("department",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
def adda_data(self):
    conn=mysql.connector.connect(host='localhost',username='root',password='Aadarsh@123',database='addy')
    my_cursor=connection.cursor()
    my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                             
self.member_var.get(),
self.commember_var.get(),
self.prn_var.get(),
self.title_var.get(),
self.firstname_var.get(),
self.lastname_var.get(),
self.stream_var.get(),
self.commember_var.get(),
self.dept_var.get(),
self.mobile_var.get(),
self.booktitle_var.get(),
self.author_var.get(),
self.db_var.get(),
self.dd_var.get(),
self.daysonbook.get(),
self.lrf_var.get(),
self.dod.get(),
self.ap.get(),
    ))
    

    conn.commit()
    self.fatch_data()
    conn.close()
     


    messagebox.showinfo("Success","Member has been setted succesfully")

    def update(self):
     conn=mysql.connector.connect(host='localhost',username='root',password='Aadarsh@123',database='addy')
    my_cursor=connection.cursor()
    my_cursor.execute("update library set member=%s,commember=%s,prn=%s,title=%s,firstname=%s,lastname=%s,stream=%s,commemeber=%s,dept=%s,mobile=%s,booktitle=%s,author=%s,db=%s,dd=%s,daysonbook=%s,lrf=%s,dod=%s,ap=%s where PRN_NO=%s",(
      

                                                                                self.member_var.get(),
                                                                                self.commember_var.get(),
                                                                                self.prn_var.get(),
                                                                                self.title_var.get(),
                                                                                self.firstname_var.get(),
                                                                                self.lastname_var.get(),
                                                                                self.stream_var.get(),
                                                                                self.commember_var.get(),
                                                                                self.dept_var.get(),
                                                                                self.mobile_var.get(),
                                                                                self.booktitle_var.get(),
                                                                                self.author_var.get(),
                                                                                self.db_var.get(),
                                                                                self.dd_var.get(),
                                                                                self.daysonbook.get(),
                                                                                self.lrf_var.get(),
                                                                                self.dod.get(),
                                                                                self.ap.get(),
                                                                                self.prn_var.get(),


                                         ))
conn.commit()
self.fatch_data()
self.reset()
conn.close()
            

messagebox.showinfo("Success","Memeber has been Updated")





def fatch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Aadarsh@123',database='addy')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
          self.library_table.delete(*self.library_table.get_children())
          for i in rows:
            self.library_table.insert("",END,values=i)
            conn.commit()
            conn.close()
      
     
def get_cursor(self,event=""):
       cursor_row=self.library_table.focus()
       content=self.library_table.item(cursor_row)
       row=content['value']

       
self.member_var.set(row[0])
self.commember_var.set(row[1])
self.prn_var.set(row[2])
self.title_var.set(row[3])
self.firstname_var.set(row[4])
self.lastname_var.set(row[5])
self.stream_var.set(row[6])
self.commember_var.set(row[7])
self.dept_var.set(row[8])
self.mobile_var.set(row[9])
self.booktitle_var.set(row[10])
self.author_var.set(row[11])
self.db_var.set(row[12])
self.dd_var.set(row[13])
self.daysonbook.set(row[14])
self.lrf_var.set(row[15])
self.dod.set(row[16])
self.ap.set(row[17])


def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"commember Type\t\t"+ self.commember_var.get() + "\n")
        self.txtBox.insert(END,"prn Type\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"title Type\t\t"+ self.title_var.get() + "\n")
        self.txtBox.insert(END,"firstname Type\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"lastname Type\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"stream Type\t\t"+ self.stream_var.get() + "\n")
        self.txtBox.insert(END,"commember Type\t\t"+ self.commember_var.get() + "\n")
        self.txtBox.insert(END,"dept Type\t\t"+ self.dept_var.get() + "\n")
        self.txtBox.insert(END,"mobile Type\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"booktitle Type\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"author Type\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"db Type\t\t"+ self.db_var.get() + "\n")
        self.txtBox.insert(END,"dd Type\t\t"+ self.dd_var.get() + "\n")
        self.txtBox.insert(END,"daysonbook Type\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"lrf Type\t\t"+ self.lrf_var.get() + "\n")
        self.txtBox.insert(END,"dod Type\t\t"+ self.dod_var.get() + "\n")
        self.txtBox.insert(END,"ap Type\t\t"+ self.ap_var.get() + "\n")
    

def reset(self):
            self.member_var.set(""),
            self.commember_var.set(""),
            self.prn_var.set(""),
            self.title_var.set(""),
            self.firstname_var.set(""),
            self.lastname_var.set(""),
            self.stream_var.set(""),
            self.commember_var.set(""),
            self.dept_var.set(""),
            self.mobile_var.set(""),
            self.booktitle_var.set(""),
            self.author_var.set(""),
            self.db_var.set(""),
            self.dd_var.set(""),
            self.daysonbook_var.set(""),
            self.lrf_var.set(""),
            self.dod_var.set(""),
            self.ap_var.set("")
            self.txtbox.delete("1.0",END)


def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management system","Do you want to exit")
        if iexit>0:
           self.root.destroy()
           return
     


def delete(self):
         if self.prn_var.get()=="" or self.id_var.get()=="":
             messagebox.showerror("Error","First Select the Memeber")
         else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Aadarsh@123',database='addy')
            my_cursor=connection.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")

if _name_ == "_main_":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()