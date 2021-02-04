import tkinter as tk



def exit1():
    exit()


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

button_add=tk.Button(frame1,text="BOOKING/ADD DATA",bd=5,font=20)
button_add.place(rely=0.25,relx=0.35,relwidth=0.3,relheight=0.1)

button_search=tk.Button(frame1,text="SEARCH DATA",bd=5,font=20)
button_search.place(rely=0.36,relx=0.35,relwidth=0.3,relheight=0.1)

button_update=tk.Button(frame1,text="UPDATE DATA",bd=5,font=20)
button_update.place(rely=0.47,relx=0.35,relwidth=0.3,relheight=0.1)

button_delete=tk.Button(frame1,text="DELETE DATA",bd=5,font="20")
button_delete.place(rely=0.58,relx=0.35,relwidth=0.3,relheight=0.1)

button_view=tk.Button(frame1,text="VIEW DATA",bd=5,font=20,command=exit1)
button_view.place(rely=0.69,relx=0.35,relwidth=0.3,relheight=0.1)

button_exit=tk.Button(frame1,text="EXIT",bd=5,font=20,command=exit1)
button_exit.place(rely=0.8,relx=0.35,relwidth=0.3,relheight=0.1)

root.mainloop()









