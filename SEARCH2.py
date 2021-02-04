import tkinter as tk
from tkinter.constants import END
import tkinter.messagebox

Height1=800
Width1=1500

root=tk.Tk()
root.title("Hotel Management System")#to define title of window

canvas=tk.Canvas(root,height=Height1,width=Width1)#to define window size
canvas.pack()

photo_window=tk.PhotoImage(file="download.png")
root.iconphoto(True,photo_window)

background_image=tk.PhotoImage(file="kisscc0-starry-sky-nature-landscape-nature-landscape-5c99fb13a4a398.2031479415535951556744.png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

label_title=tk.Label(root,text="Hotel Management",font=40,bg="#80c1ff")
label_title.place(relx=0.5,relwidth=0.3,relheight=0.1,anchor="n")

frame1=tk.Frame(root,bd=4,relief="ridge")
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
        root.destroy()
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
search_button=tk.Button(frame1,text="SEARCH DATA",relief="raised",font=20,bg="cyan",command=search_func)
search_button.place(relx=0.36,rely=0.92)

reset_button=tk.Button(frame1,text="RESET",relief="raised",font=10,command=reset)
reset_button.place(relx=0.48,rely=0.92)

exit_button=tk.Button(frame1,text="EXIT",relief="raised",font=20,bg="red",command=exitbut2)
exit_button.place(relx=0.55,rely=0.92)

root.mainloop()