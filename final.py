import tkinter as tk
import tkinter.messagebox
from tkinter.constants import END

def booking():

    Height1=700
    Width1=900

    root1=tk.Toplevel(root)
    root1.title("Hotel Management System")#to define title of window

    canvas=tk.Canvas(root1,height=Height1,width=Width1)#to define window size
    canvas.pack()

    photo_window=tk.PhotoImage(file="download.png")
    root1.iconphoto(False,photo_window)

    background_image1=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
    background_label1=tk.Label(root1,image=background_image1)
    background_label1.place(relwidth=1,relheight=1)

    frame1=tk.Frame(root1,bd=4,relief="raised")
    frame1.place(relx=0.5,rely=0.1,relwidth=0.9,relheight=0.89,anchor="n")

    frame2=tk.Frame(frame1,bd=4,relief="ridge",bg="yellow")
    frame2.place(relx=0.45,rely=0.01,relwidth=0.54,relheight=0.5)

    frame3=tk.Frame(frame1,bd=4,relief="ridge")
    frame3.place(relx=0.45,rely=0.53,relwidth=0.54,relheight=0.45)

    label_title=tk.Label(root1,text="Hotel Management",font=40)
    label_title.place(relx=0.5,relwidth=0.3,relheight=0.1,anchor="n")

    #inside frame1
    label_custid=tk.Label(frame1,text="Customer Id*:",font=10,relief="raised",justify="left")
    label_custid.place(relwidth=0.19,relheight=0.07)
    entry_custid=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_custid.place(relx=0.2,relwidth=0.24,relheight=0.07)

    label_firstname=tk.Label(frame1,text="Customer Name*:",font=10,relief="raised")
    label_firstname.place(rely=0.08,relwidth=0.19,relheight=0.07)
    entry_custname=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_custname.place(rely=0.08,relx=0.2,relwidth=0.24,relheight=0.07)

    label_address=tk.Label(frame1,text="Address*:",font=10,relief="raised",justify="left")
    label_address.place(rely=0.16,relwidth=0.19,relheight=0.07)
    entry_address=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_address.place(rely=0.16,relx=0.2,relwidth=0.24,relheight=0.07)

    label_dob=tk.Label(frame1,text="Date of Birth*:",font=10,relief="raised",justify="left")
    label_dob.place(rely=0.24,relwidth=0.19,relheight=0.07)
    entry_dob=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_dob.place(rely=0.24,relx=0.2,relwidth=0.24,relheight=0.07)

    label_phoneno=tk.Label(frame1,text="Mobile no*:",font=10,relief="raised",justify="left")
    label_phoneno.place(rely=0.32,relwidth=0.19,relheight=0.07)
    entry_mobile=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_mobile.place(rely=0.32,relx=0.2,relwidth=0.24,relheight=0.07)

    label_email=tk.Label(frame1,text="E-mail:",font=10,relief="raised",justify="left")
    label_email.place(rely=0.4,relwidth=0.19,relheight=0.07)
    entry_email=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_email.place(rely=0.4,relx=0.2,relwidth=0.24,relheight=0.07)

    label_nationality=tk.Label(frame1,text="Nationality*:",font=10,relief="raised",justify="left")
    label_nationality.place(rely=0.48,relwidth=0.19,relheight=0.07)
    entry_nationality=tk.Entry(frame1,bd=5,font=20,relief="sunken")
    entry_nationality.place(rely=0.48,relx=0.2,relwidth=0.24,relheight=0.07)

    label_gender=tk.Label(frame1,text="Gender:",font=10,relief="raised",justify="left")
    label_gender.place(rely=0.56,relwidth=0.19,relheight=0.07)
    entry_gender=tk.Entry(frame1,bd=5,font=10,relief="sunken")
    entry_gender.place(rely=0.56,relx=0.2,relwidth=0.24,relheight=0.07)

    label_checkin=tk.Label(frame1,text="CheckIn Date*:",font=10,relief="raised",justify="left")
    label_checkin.place(rely=0.64,relwidth=0.19,relheight=0.07)
    entry_checkin=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_checkin.place(rely=0.64,relx=0.2,relwidth=0.24,relheight=0.07)

    label_checkout=tk.Label(frame1,text="CheckOut Date*:",font=10,relief="raised")
    label_checkout.place(rely=0.72,relwidth=0.19,relheight=0.07)
    entry_checkout=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_checkout.place(rely=0.72,relx=0.2,relwidth=0.24,relheight=0.07)

    label_typeid=tk.Label(frame1,text="ID of Customer*:",font=10,relief="raised")
    label_typeid.place(rely=0.8,relwidth=0.19,relheight=0.07)
    entry_typeofid=tk.Entry(frame1,bd=5,font=10,relief="sunken")
    entry_typeofid.place(rely=0.8,relx=0.2,relwidth=0.24,relheight=0.07)

    label_roomno=tk.Label(frame1,text="Room no*:",font=10,relief="raised",justify="left")
    label_roomno.place(rely=0.88,relwidth=0.19,relheight=0.07)
    entry_room=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_room.place(rely=0.88,relx=0.2,relwidth=0.24,relheight=0.07)


    label_details=tk.Label(frame3,text='STATUS...',font=10,justify="left",width=8)
    label_details.grid(rows=1,column=0)

    '''scrollbar=tk.Scrollbar(frame3)
    scrollbar.grid(row=2,column=4,columnspan=17)'''
    lsthotel=tk.Listbox(frame3,width=39,height=10,font=1)
    lsthotel.grid(row=3,column=0,padx=1,sticky='nsew')
    #lsthotel.config(yscrollcommand = scrollbar.set) 
    #scrollbar.config(command = lsthotel.yview)

    def booking_func():
        try:
            custid=entry_custid.get()
            custname=entry_custname.get()
            address=entry_address.get()
            dob=entry_dob.get()
            mobile=entry_mobile.get()
            email=entry_email.get()
            nationality=entry_nationality.get()
            gender=entry_gender.get()
            checkindate=entry_checkin.get()
            checkoutdate=entry_checkout.get()
            typeofid=entry_typeofid.get()
            roomnumber=entry_room.get()
            import mysql.connector
            main1=mysql.connector.connect(host="localhost",user="root",password="tiger")
            mycursor=main1.cursor()
            #creating database
            mycursor.execute("create database if not exists hotelmanagement")
            mycursor.execute("use hotelmanagement")
            #creating required table 
            mycursor.execute("create table if not exists bookinghotel(cust_id varchar(6) primary key,cust_name varchar(30),\
                        address varchar(30),dob varchar(10),mobilenum varchar(10),email varchar(20),nationality varchar(20),gender varchar(8),\
                        checkin varchar(12),checkout varchar(12),typeofid varchar(20),roomno varchar(20))")
            main1.commit()
            sql="insert into bookinghotel (cust_id, cust_name, address, dob, mobilenum, email, nationality, gender, checkin, checkout, typeofid, roomno) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(custid,custname,address,dob,mobile,email,nationality,gender,checkindate,checkoutdate,typeofid,roomnumber))
            main1.commit()
            print("record inserted")
            lsthotel.insert(END,"RECORD INSERTED")
        
        except:
            lsthotel.insert(END,"ERROR")

    def exitbut():
        exitbut=tkinter.messagebox.askyesno('Hotel Database Management System',"Confirm if you want to exit")
        if exitbut>0 :
            root1.destroy()
            return

    def reset():
        entry_custid.delete(0,'end')
        entry_custname.delete(0,'end')
        entry_address.delete(0,'end')
        entry_dob.delete(0,'end')
        entry_mobile.delete(0,'end')
        entry_email.delete(0,'end')
        entry_nationality.delete(0,'end')
        entry_gender.delete(0,'end')
        entry_checkin.delete(0,'end')
        entry_checkout.delete(0,'end')
        entry_typeofid.delete(0,'end')
        entry_room.delete(0,'end')
        print("VALUES RESETTED")
        lsthotel.insert(END,"ENTRIES RESETTED")
    #inside frame2
    label_commandbox=tk.Label(frame2,text="CHOOSE A COMMAND BELOW..",font=10,bg="yellow")
    label_commandbox.place(relx=0.13,rely=0.01,relwidth=0.8,relheight=0.1)

    add_button=tk.Button(frame2,text="ADD DATA",relief="raised",font=10,bg="blue",command=booking_func)
    add_button.place(relx=0.35,rely=0.2,relwidth=0.3,relheight=0.15)

    reset_button=tk.Button(frame2,text="RESET",relief="raised",font=10,bg="green",command=reset)
    reset_button.place(relx=0.35,rely=0.36,relwidth=0.3,relheight=0.15)

    exit_button=tk.Button(frame2,text="EXIT",relief="raised",bg="red",font=10,command=exitbut)
    exit_button.place(relx=0.35,rely=0.52,relwidth=0.3,relheight=0.15)

def search():
    Height1=800
    Width1=1500

    root2=tk.Toplevel(root)
    root2.title("Hotel Management System")#to define title of window

    canvas=tk.Canvas(root2,height=Height1,width=Width1)#to define window size
    canvas.pack()

    photo_window=tk.PhotoImage(file="download.png")
    root2.iconphoto(True,photo_window)

    background_image=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
    background_label=tk.Label(root2,image=background_image)
    background_label.place(relwidth=1,relheight=1)

    label_title=tk.Label(root2,text="Hotel Management",font=40)
    label_title.place(relx=0.5,relwidth=0.3,relheight=0.1,anchor="n")

    frame1=tk.Frame(root2,bd=4,relief="ridge")
    frame1.place(relx=0.5,rely=0.1,relwidth=0.99,relheight=0.89,anchor="n")

    frame2=tk.Frame(frame1,bd=4,relief="ridge")
    frame2.place(rely=0.01,relwidth=1,relheight=0.1)

    frame3=tk.Frame(frame1,bd=4,relief="ridge")
    frame3.place(rely=0.11,relwidth=1,relheight=0.8)

    frame4=tk.Frame(frame3,bd=4,relief="ridge")
    frame4.place(rely=0.87,relheight=0.13,relwidth=1)

    lable_head=tk.Label(frame2,text="CustomerID\tCustomername\tADDRESS\tDOB\tMobile\tEmail\tNationality\tGender\tCheckin\tCheckout\tTypeofID\tRoomno",relief="sunken",font=5)
    lable_head.place(relwidth=1,relheight=1)

    label_custid=tk.Label(frame4,text="Customer Id:",font=10,relief="raised",justify="left")
    label_custid.place(relx=0.01,rely=0.1,relwidth=0.1,relheight=0.7)
    entry_custid=tk.Entry(frame4,bd=5,relief="ridge",font=20)
    entry_custid.place(rely=0.1,relx=0.11,relwidth=0.12,relheight=0.7)

    label_firstname=tk.Label(frame4,text="Customer Name:",font=10,relief="raised")
    label_firstname.place(relx=0.3,rely=0.1,relwidth=0.13,relheight=0.7)
    entry_custname=tk.Entry(frame4,bd=5,relief="ridge",font=20)
    entry_custname.place(rely=0.1,relx=0.43,relwidth=0.15,relheight=0.7)


    '''scrollbar=tk.Scrollbar(frame3)
    scrollbar.grid(row=0,column=0,columnspan=17)'''
    lsthotel=tk.Listbox(frame3,width=133,height=20,font=5)
    #lsthotel.bind('<<ListboxSelect>>',search_func)
    lsthotel.grid(row=0,column=0,padx=1,sticky='nsew')
    #scrollbar.config(command=lsthotel.xview)

    def exitbut2():
        exitbut=tkinter.messagebox.askyesno('Hotel Database Management System',"Confirm if you want to exit")
        if exitbut>0 :
            root2.destroy()
            return
    def search_func():
        custid=entry_custid.get()
        custname=entry_custname.get()
        import mysql.connector
        main1=mysql.connector.connect(host="localhost",user="root",password="tiger")
        mycursor=main1.cursor()
        #creating database
        mycursor.execute("create database if not exists hotelmanagement")
        mycursor.execute("use hotelmanagement")
        mycursor.execute("create table if not exists bookinghotel(cust_id varchar(6) primary key,cust_name varchar(30),\
                    address varchar(30),dob varchar(10),mobilenum varchar(10),email varchar(20),nationality varchar(20),gender varchar(8),\
                    checkin varchar(12),checkout varchar(12),typeofid varchar(20),roomno varchar(20))")
        main1.commit()
        sql1="select * from bookinghotel where cust_id=%s or cust_name=%s"
        mycursor.execute(sql1,(custid,custname))
        comm=mycursor.fetchall()
        for i in comm:
            print(i)
            print("DATA FOUND")
            lsthotel.insert(END,i)


    def reset():
        entry_custid.delete(0,'end')
        entry_custname.delete(0,'end')
        print("VALUES RESETTED")

    #frame1
    search_button=tk.Button(frame1,text="SEARCH DATA",relief="raised",font=20,bg="blue",command=search_func)
    search_button.place(relx=0.36,rely=0.92)

    reset_button=tk.Button(frame1,text="RESET",relief="raised",bg="green",font=10,command=reset)
    reset_button.place(relx=0.48,rely=0.92)

    exit_button=tk.Button(frame1,text="EXIT",relief="raised",font=20,bg="red",command=exitbut2)
    exit_button.place(relx=0.55,rely=0.92)

def update():
    Height2=700
    Width2=900

    root3=tk.Toplevel(root)
    root3.title("Hotel Management System")#to define title of window

    canvas=tk.Canvas(root3,height=Height2,width=Width2)#to define window size
    canvas.pack()

    photo_window=tk.PhotoImage(file="download.png")
    root3.iconphoto(False,photo_window)

    background_image2=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
    background_label2=tk.Label(root3,image=background_image2)
    background_label2.place(relwidth=1,relheight=1)

    frame1=tk.Frame(root3,bd=4,relief="raised")
    frame1.place(relx=0.5,rely=0.1,relwidth=0.9,relheight=0.89,anchor="n")

    frame2=tk.Frame(frame1,bd=4,relief="ridge",bg="yellow")
    frame2.place(relx=0.45,rely=0.01,relwidth=0.54,relheight=0.5)

    frame3=tk.Frame(frame1,bd=4,relief="ridge")
    frame3.place(relx=0.45,rely=0.53,relwidth=0.54,relheight=0.45)

    label_title=tk.Label(root3,text="Hotel Management",font=40)
    label_title.place(relx=0.5,relwidth=0.3,relheight=0.1,anchor="n")
     
    label_custid=tk.Label(frame1,text="Customer Id*:",font=10,relief="raised",justify="left")
    label_custid.place(relwidth=0.19,relheight=0.07)
    entry_custid=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_custid.place(relx=0.2,relwidth=0.24,relheight=0.07)

    label_firstname=tk.Label(frame1,text="Customer Name:",font=10,relief="raised")
    label_firstname.place(rely=0.08,relwidth=0.19,relheight=0.07)
    entry_custname=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_custname.place(rely=0.08,relx=0.2,relwidth=0.24,relheight=0.07)

    label_address=tk.Label(frame1,text="Address:",font=10,relief="raised",justify="left")
    label_address.place(rely=0.16,relwidth=0.19,relheight=0.07)
    entry_address=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_address.place(rely=0.16,relx=0.2,relwidth=0.24,relheight=0.07)

    label_email=tk.Label(frame1,text="E-mail:",font=10,relief="raised",justify="left")
    label_email.place(rely=0.24,relwidth=0.19,relheight=0.07)
    entry_email=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_email.place(rely=0.24,relx=0.2,relwidth=0.24,relheight=0.07)

    label_nationality=tk.Label(frame1,text="Nationality:",font=10,relief="raised",justify="left")
    label_nationality.place(rely=0.32,relwidth=0.19,relheight=0.07)
    entry_nationality=tk.Entry(frame1,bd=5,relief="sunken",font=20)
    entry_nationality.place(rely=0.32,relx=0.2,relwidth=0.24,relheight=0.07)

    label_gender=tk.Label(frame1,text="Gender:",font=10,relief="raised",justify="left")
    label_gender.place(rely=0.4,relwidth=0.19,relheight=0.07)
    entry_gender=tk.Entry(frame1,font=20,bd=5,relief='sunken')
    entry_gender.place(rely=0.4,relx=0.2,relwidth=0.24,relheight=0.07)

    lsthotel=tk.Listbox(frame3,width=38,height=10,font=1)
    lsthotel.grid(row=3,column=0,padx=1,sticky='nsew')

    def update_func():
        
        try:
            custid=entry_custid.get()
            custname=entry_custname.get()
            address=entry_address.get()
            email=entry_email.get()
            nationality=entry_nationality.get()
            gender=entry_gender.get()
            import mysql.connector
            main1=mysql.connector.connect(host="localhost",user="root",password="tiger")
            mycursor=main1.cursor()
            #creating database
            mycursor.execute("create database if not exists hotelmanagement")
            mycursor.execute("use hotelmanagement")
            #creating required table 
            mycursor.execute("create table if not exists bookinghotel(cust_id varchar(6) primary key,cust_name varchar(30),\
                        address varchar(30),dob varchar(10),mobilenum varchar(10),email varchar(20),nationality varchar(20),gender varchar(8),\
                        checkin varchar(12),checkout varchar(12),typeofid varchar(20),roomno varchar(20))")
            main1.commit()
            sql="Update bookinghotel set cust_name=%s, address=%s,email=%s, nationality=%s, gender=%s where cust_id=%s"
            mycursor.execute(sql,(custname,address,email,nationality,gender,custid))
            main1.commit()
            print("RECORD UPDATTED")
            lsthotel.insert(END,"RECORD UPDATED")
        
        except:
            lsthotel.insert(END,"ERROR")

    def reset():
        entry_custid.delete(0,'end')
        entry_custname.delete(0,'end')
        entry_address.delete(0,'end')
        entry_email.delete(0,'end')
        entry_nationality.delete(0,'end')
        entry_gender.delete(0,'end')
        print("VALUES RESETTED")
        lsthotel.insert(END,"ENTRIES RESETTED")
    
    def exitbut3():
        exitbut=tkinter.messagebox.askyesno('Hotel Database Management System',"Confirm if you want to exit")
        if exitbut>0 :
            root3.destroy()
            return

    #inside frame2
    label_commandbox=tk.Label(frame2,text="CHOOSE A COMMAND BELOW..",bg="yellow",font=10)
    label_commandbox.place(relx=0.13,rely=0.01,relwidth=0.8,relheight=0.1)

    update_button=tk.Button(frame2,text="UPDATE DATA",relief="raised",font=10,bg="blue",command=update_func)
    update_button.place(relx=0.32,rely=0.2,relwidth=0.35,relheight=0.15)

    reset_button=tk.Button(frame2,text="RESET",relief="raised",bg="green",font=10,command=reset)
    reset_button.place(relx=0.32,rely=0.36,relwidth=0.35,relheight=0.15)

    exit_button=tk.Button(frame2,text="EXIT",relief="raised",bg="red",font=10,command=exitbut3)
    exit_button.place(relx=0.32,rely=0.52,relwidth=0.35,relheight=0.15)

def delete():

    root4=tk.Toplevel(root)
    root4.title("Hotel Management System")#to define title of window
    Height1=400
    Width1=500

    canvas=tk.Canvas(root4,height=Height1,width=Width1)#to define window sizecanvas.pack()
    canvas.pack()

    photo_window=tk.PhotoImage(file="download.png")
    root4.iconphoto(False,photo_window)

    background_image=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
    background_label=tk.Label(root4,image=background_image)
    background_label.place(relwidth=1,relheight=1)

    frame1=tk.Frame(root4,bd=4,relief="raised")
    frame1.place(relx=0.5,rely=0.1,relwidth=0.99,relheight=0.89,anchor="n")

    frame2=tk.Frame(frame1,bd=4,relief="ridge")
    frame2.place(rely=0.01,relheight=0.45,relwidth=0.99)

    frame3=tk.Frame(frame1,bd=4,relief="ridge")
    frame3.place(rely=0.49,relheight=0.47,relwidth=0.99)

    #insideframe1
    comment_label=tk.Label(frame2,text="Enter Customer ID",font=10,fg="red")
    comment_label.place(relx=0.2,rely=0.01,relwidth=0.6,relheight=0.15)

    del_custid=tk.Label(frame2,text="CustomerID",relief="raised",font=10)
    del_custid.place(relx=0.01,rely=0.30,relwidth=0.3,relheight=0.3)

    del_custidentry=tk.Entry(frame2,bd=5,relief="sunken",font=20)
    del_custidentry.place(relx=0.32,rely=0.30,relwidth=0.4,relheight=0.3)

    lsthotel=tk.Listbox(frame3,width=43,height=10,font=1)
    lsthotel.grid(row=3,column=2,padx=1,sticky='nsew')

    def delete_func():
        
        try:
            delete=del_custidentry.get()
            import mysql.connector
            main1=mysql.connector.connect(host="localhost",user="root",password="tiger")
            mycursor=main1.cursor()
            #creating database
            mycursor.execute("create database if not exists hotelmanagement")
            mycursor.execute("use hotelmanagement")
            #creating required table 
            mycursor.execute("create table if not exists bookinghotel(cust_id varchar(6) primary key,cust_name varchar(30),\
                        address varchar(30),dob varchar(10),mobilenum varchar(10),email varchar(20),nationality varchar(20),gender varchar(8),\
                        checkin varchar(12),checkout varchar(12),typeofid varchar(20),roomno varchar(20))")
            main1.commit()
            sql="DELETE FROM bookinghotel WHERE cust_id=%s"
            mycursor.execute(sql,(delete,))
            main1.commit()
            print("record deleted")
            lsthotel.insert(END,"RECORD DELETED")
        
        except:
            lsthotel.insert(END,"ERROR")

    def reset1():
        del_custidentry.delete(0,'end')
        lsthotel.insert(END,"ENTRY RESETTED")

    def exitbut2():
        exitbut=tkinter.messagebox.askyesno('Hotel Database Management System',"Confirm if you want to exit")
        if exitbut>0 :
            root4.destroy()
            return

    delete_but=tk.Button(frame2,text="DELETE RECORD",relief="raised",font=5,bg="blue",command=delete_func)
    delete_but.place(relx=0.01,rely=0.68)

    reset_but=tk.Button(frame2,text="RESET",relief="raised",font=10,bg="green",command=reset1)
    reset_but.place(relx=0.48,rely=0.68)

    exit_but=tk.Button(frame2,text="EXIT",relief="raised",font=10,bg="red",command=exitbut2)
    exit_but.place(relx=0.73,rely=0.68)

def view():
    Height1=700
    Width1=1500

    root5=tk.Toplevel(root)
    root5.title("Hotel Management System")#to define title of window

    canvas=tk.Canvas(root5,height=Height1,width=Width1)#to define window size
    canvas.pack()

    photo_window=tk.PhotoImage(file="download.png")
    root5.iconphoto(True,photo_window)

    background_image3=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
    background_label3=tk.Label(root5,image=background_image3)
    background_label3.place(relwidth=1,relheight=1)

    label_title=tk.Label(root5,text="Hotel Management",font=40)
    label_title.place(relx=0.5,relwidth=0.3,relheight=0.1,anchor="n")

    frame1=tk.Frame(root5,bd=4,relief="raised")
    frame1.place(relx=0.5,rely=0.1,relwidth=0.99,relheight=0.89,anchor="n")

    frame2=tk.Frame(frame1,bd=4,relief="ridge")
    frame2.place(rely=0.01,relwidth=1,relheight=0.1)

    frame3=tk.Frame(frame1,bd=4,relief="ridge")
    frame3.place(rely=0.11,relwidth=1,relheight=0.8)

    lable_head=tk.Label(frame2,text="CustomerID\tCustomername\tADDRESS\tDOB\tMobile\tEmail\tNationality\tGender\tCheckIn\tCheckOut\t TypeofID\tRoomno",relief="sunken",font=5)
    lable_head.place(relwidth=1,relheight=0.999,relx=0.001,rely=0.001)

    '''scrollbar=tk.Scrollbar(frame3)
    scrollbar.grid(row=0,column=0,columnspan=17)'''
    lsthotel=tk.Listbox(frame3,width=133,height=20,font=5)
    #lsthotel.bind('<<ListboxSelect>>')
    lsthotel.grid(row=0,column=0,padx=1,sticky='nsew')
    #scrollbar.config(command=lsthotel.xview)

    def exitbut2():
        exitbut=tkinter.messagebox.askyesno('Hotel Database Management System',"Confirm if you want to exit")
        if exitbut>0 :
            root5.destroy()
            return
    def view_func():
        import mysql.connector
        main1=mysql.connector.connect(host="localhost",user="root",password="tiger")
        mycursor=main1.cursor()
        #creating database
        mycursor.execute("create database if not exists hotelmanagement")
        mycursor.execute("use hotelmanagement")
        mycursor.execute("select * from bookinghotel")
        sql1=mycursor.fetchall()
        for i in sql1:
            print(i)  
            lsthotel.insert(END,i) 

    #frame1
    view_button=tk.Button(frame1,text="VIEW DATA",relief="raised",font=20,bg="blue",command=view_func)
    view_button.place(relx=0.4,rely=0.92)

    exit_button=tk.Button(frame1,text="EXIT",relief="raised",font=20,bg="red",command=exitbut2)
    exit_button.place(relx=0.55,rely=0.92)

def exitbutf():
    exitbut=tkinter.messagebox.askyesno('Hotel Database Management System',"Confirm if you want to exit")
    if exitbut>0 :
        root.destroy()
        return

Height1=700
Width1=900

root=tk.Tk()
root.title("Hotel Management System")#to define title of window

canvas=tk.Canvas(root,height=Height1,width=Width1)#to define window size
canvas.pack()

photo_window=tk.PhotoImage(file="download.png")
root.iconphoto(True,photo_window)

background_image=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame1=tk.Frame(root,bd=4)
frame1.place(relx=0.5,rely=0.1,relwidth=0.9,relheight=0.89,anchor="n")

label_title=tk.Label(root,text="Hotel Management",font=40,bg="#80c1ff")
label_title.place(relx=0.5,relwidth=0.3,relheight=0.1,anchor="n")

label_intro=tk.Label(frame1,text="Welcome to HOTEL MANAGEMENT SYSTEM!!!",font=40,fg="red")
label_intro.place(relx=0.22,relwidth=0.6,relheight=0.1)

label_instruct=tk.Label(frame1,text="PLEASE SELECT A OPTION BELOW.....",font=20)
label_instruct.place(rely=0.1,relx=0.26,relwidth=0.5,relheight=0.1)

button_add=tk.Button(frame1,text="BOOKING/ADD DATA",bd=5,font=20,command=booking)
button_add.place(rely=0.25,relx=0.35,relwidth=0.3,relheight=0.1)

button_search=tk.Button(frame1,text="SEARCH DATA",bd=5,font=20,command=search)
button_search.place(rely=0.36,relx=0.35,relwidth=0.3,relheight=0.1)

button_update=tk.Button(frame1,text="UPDATE DATA",bd=5,font=20,command=update)
button_update.place(rely=0.47,relx=0.35,relwidth=0.3,relheight=0.1)

button_delete=tk.Button(frame1,text="DELETE DATA",bd=5,font="20",command=delete)
button_delete.place(rely=0.58,relx=0.35,relwidth=0.3,relheight=0.1)

button_view=tk.Button(frame1,text="VIEW DATA",bd=5,font=20,command=view)
button_view.place(rely=0.69,relx=0.35,relwidth=0.3,relheight=0.1)

button_exit=tk.Button(frame1,text="EXIT",bd=5,font=20,command=exitbutf)
button_exit.place(rely=0.8,relx=0.35,relwidth=0.3,relheight=0.1)

label_details=tk.Label(frame1,text="* means that field cannot be left none",fg="red",font=20)
label_details.place(rely=0.92,relx=0.25,relwidth=1,relheight=0.1)

root.mainloop()
