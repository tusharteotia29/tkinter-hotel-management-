from enum import EnumMeta
import tkinter as tk
from tkinter.constants import END
import tkinter.messagebox

Height1=700
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

frame1=tk.Frame(root,bd=4,relief="raised")
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
        root.destroy()
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
view_button=tk.Button(frame1,text="VIEW DATA",relief="raised",font=20,bg="cyan",command=view_func)
view_button.place(relx=0.4,rely=0.92)

exit_button=tk.Button(frame1,text="EXIT",relief="raised",font=20,bg="red",command=exitbut2)
exit_button.place(relx=0.55,rely=0.92)

root.mainloop()
