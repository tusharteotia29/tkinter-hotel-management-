import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import END

Height1=700
Width1=900

root=tk.Tk()
root.title("Hotel Management System")#to define title of window

canvas=tk.Canvas(root,height=Height1,width=Width1)#to define window size
canvas.pack()

photo_window=tk.PhotoImage(file="download.png")
root.iconphoto(False,photo_window)

background_image=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame1=tk.Frame(root,bd=4,relief="raised")
frame1.place(relx=0.5,rely=0.1,relwidth=0.9,relheight=0.89,anchor="n")

frame2=tk.Frame(frame1,bd=4,relief="sunken",bg="powder blue")
frame2.place(relx=0.45,rely=0.01,relwidth=0.54,relheight=0.5)

frame3=tk.Frame(frame1,bd=4,relief="sunken")
frame3.place(relx=0.45,rely=0.53,relwidth=0.55,relheight=0.46)

label_title=tk.Label(root,text="Hotel Management",font=40,bg="#80c1ff")
label_title.place(relx=0.5,relwidth=0.3,relheight=0.1,anchor="n")

#-------------------------------------------------------------------------inside frame1-----------------------------------------------------------------------------
label_custid=tk.Label(frame1,text="Customer Id:",font=10,relief="raised",justify="left")
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

label_dob=tk.Label(frame1,text="Date of Birth:",font=10,relief="raised",justify="left")
label_dob.place(rely=0.24,relwidth=0.19,relheight=0.07)
entry_dob=tk.Entry(frame1,bd=5,relief="sunken",font=20)
entry_dob.place(rely=0.24,relx=0.2,relwidth=0.24,relheight=0.07)

label_phoneno=tk.Label(frame1,text="Mobile no:",font=10,relief="raised",justify="left")
label_phoneno.place(rely=0.32,relwidth=0.19,relheight=0.07)
entry_mobile=tk.Entry(frame1,bd=5,relief="sunken",font=20)
entry_mobile.place(rely=0.32,relx=0.2,relwidth=0.24,relheight=0.07)

label_email=tk.Label(frame1,text="E-mail:",font=10,relief="raised",justify="left")
label_email.place(rely=0.4,relwidth=0.19,relheight=0.07)
entry_email=tk.Entry(frame1,bd=5,relief="sunken",font=20)
entry_email.place(rely=0.4,relx=0.2,relwidth=0.24,relheight=0.07)

label_nationality=tk.Label(frame1,text="Nationality:",font=10,relief="raised",justify="left")
label_nationality.place(rely=0.48,relwidth=0.19,relheight=0.07)
entry_nationality=tk.Entry(frame1,bd=5,font=20,relief="sunken")
entry_nationality.place(rely=0.48,relx=0.2,relwidth=0.24,relheight=0.07)

label_gender=tk.Label(frame1,text="Gender:",font=10,relief="raised",justify="left")
label_gender.place(rely=0.56,relwidth=0.19,relheight=0.07)
entry_gender=tk.Entry(frame1,bd=5,font=10,relief="sunken")
entry_gender.place(rely=0.56,relx=0.2,relwidth=0.24,relheight=0.07)

label_checkin=tk.Label(frame1,text="CheckIn Date:",font=10,relief="raised",justify="left")
label_checkin.place(rely=0.64,relwidth=0.19,relheight=0.07)
entry_checkin=tk.Entry(frame1,bd=5,relief="sunken",font=20)
entry_checkin.place(rely=0.64,relx=0.2,relwidth=0.24,relheight=0.07)

label_checkout=tk.Label(frame1,text="CheckOut Date:",font=10,relief="raised")
label_checkout.place(rely=0.72,relwidth=0.19,relheight=0.07)
entry_checkout=tk.Entry(frame1,bd=5,relief="sunken",font=20)
entry_checkout.place(rely=0.72,relx=0.2,relwidth=0.24,relheight=0.07)

label_typeid=tk.Label(frame1,text="ID of Customer:",font=10,relief="raised")
label_typeid.place(rely=0.8,relwidth=0.19,relheight=0.07)
entry_typeofid=tk.Entry(frame1,bd=5,font=10,relief="sunken")
entry_typeofid.place(rely=0.8,relx=0.2,relwidth=0.24,relheight=0.07)

label_roomno=tk.Label(frame1,text="Room no:",font=10,relief="raised",justify="left")
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

def exit():
    exit()

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
#----------------------------------------------------------------------------inside frame2----------------------------------------------------------
label_commandbox=tk.Label(frame2,text="CHOOSE A COMMAND BELOW..",font=10,bg="powder blue")
label_commandbox.place(relx=0.13,rely=0.01,relwidth=0.8,relheight=0.1)

add_button=tk.Button(frame2,text="ADD DATA",relief="raised",font=10,bg="red",command=booking_func)
add_button.place(relx=0.35,rely=0.2,relwidth=0.3,relheight=0.15)

reset_button=tk.Button(frame2,text="RESET",relief="raised",font=10,bg="cyan",command=reset)
reset_button.place(relx=0.35,rely=0.36,relwidth=0.3,relheight=0.15)

back_button=tk.Button(frame2,text="BACK",relief="raised",font=10)
back_button.place(relx=0.35,rely=0.52,relwidth=0.3,relheight=0.15)

exit_button=tk.Button(frame2,text="EXIT",relief="raised",font=10,bg="red",command=exit)
exit_button.place(relx=0.35,rely=0.68,relwidth=0.3,relheight=0.15)

root.mainloop()


