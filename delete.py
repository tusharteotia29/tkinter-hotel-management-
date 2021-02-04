import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import END

root=tk.Tk()
root.title("Hotel Management System")#to define title of window
Height1=400
Width1=500

canvas=tk.Canvas(root,height=Height1,width=Width1)#to define window sizecanvas.pack()
canvas.pack()

photo_window=tk.PhotoImage(file="download.png")
root.iconphoto(False,photo_window)

background_image=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame1=tk.Frame(root,bd=4,relief="raised")
frame1.place(relx=0.5,rely=0.1,relwidth=0.99,relheight=0.89,anchor="n")

frame2=tk.Frame(frame1,bd=4,relief="sunken")
frame2.place(rely=0.01,relheight=0.45,relwidth=0.99)

frame3=tk.Frame(frame1,bd=4,relief="sunken")
frame3.place(rely=0.49,relheight=0.47,relwidth=0.99)

lsthotel=tk.Listbox(frame3,width=43,height=10,font=1)
lsthotel.grid(row=3,column=2,padx=1,sticky='nsew')
    
    
#insideframe1
comment_label=tk.Label(frame2,text="Enter Customer ID",font=10,fg="red")
comment_label.place(relx=0.2,rely=0.01,relwidth=0.6,relheight=0.15)

del_custid=tk.Label(frame2,text="CustomerID",relief="raised",font=10)
del_custid.place(relx=0.01,rely=0.30,relwidth=0.3,relheight=0.3)

del_custidentry=tk.Entry(frame2,bd=5,relief="ridge",font=20)
del_custidentry.place(relx=0.32,rely=0.30,relwidth=0.4,relheight=0.3)


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

delete_but=tk.Button(frame2,text="DELETE RECORD",relief="raised",font=5,bg="red",command=delete_func)
delete_but.place(relx=0.01,rely=0.68)

reset_but=tk.Button(frame2,text="RESET",relief="raised",font=10,bg="cyan",command=reset1)
reset_but.place(relx=0.48,rely=0.68)

exit_but=tk.Button(frame2,text="EXIT",relief="raised",font=10,bg="red",command=exit)
exit_but.place(relx=0.73,rely=0.68)

def exit():
    exit()
#inside frame2

root.mainloop()