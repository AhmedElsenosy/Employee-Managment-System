from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")


root = Tk()
root.title('Employee Managment System')
root.geometry("1240x615+0+0")
root.resizable(False,False)
root.configure(bg='#2c3e50')

name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

logo = PhotoImage(file='image.png')
lbl_logo = Label(root, image=logo,bg='#2c3e50')
lbl_logo.place(x=80,y=520)



# Entery frame

Entery_frame = Frame(root, bg='#2c3e50')
Entery_frame.place(x=1,y=1,width=360,height=510)
title = Label(Entery_frame,text='Employee Company',font=('Calibri',18,'bold'),bg='#2c3e50',fg='white')
title.place(x=10,y=1)

lb_name = Label(Entery_frame,text="Name",font=('Calibri',16),bg='#2c3e50',fg='white')
lb_name.place(x=10,y=50)
txt_name = Entry(Entery_frame,textvariable=name,width=20,font=('Calibri',16))
txt_name.place(x=120,y=50)

lb_jop = Label(Entery_frame,text="Jop",font=('Calibri',16),bg='#2c3e50',fg='white')
lb_jop.place(x=10,y=90)
txt_jop = Entry(Entery_frame,textvariable=job,width=20,font=('Calibri',16))
txt_jop.place(x=120,y=90)

lb_gender = Label(Entery_frame,text="Gender",font=('Calibri',16),bg='#2c3e50',fg='white')
lb_gender.place(x=10,y=130)
combo_gen = ttk.Combobox(Entery_frame,textvariable=gender,state='readonly',width=18,font=('Calibri',16))
combo_gen['values']= ("Male","Female")
combo_gen.place(x=120,y=130)

lb_age = Label(Entery_frame,text="Age",font=('Calibri',16),bg='#2c3e50',fg='white')
lb_age.place(x=10,y=170)
txt_age = Entry(Entery_frame,textvariable=age,width=20,font=('Calibri',16))
txt_age.place(x=120,y=170)

lb_email = Label(Entery_frame,text="Email",font=('Calibri',16),bg='#2c3e50',fg='white')
lb_email.place(x=10,y=210)
txt_email = Entry(Entery_frame,textvariable=email,width=20,font=('Calibri',16))
txt_email.place(x=120,y=210)

lb_contact = Label(Entery_frame,text="Contact",font=('Calibri',16),bg='#2c3e50',fg='white')
lb_contact.place(x=10,y=250)
txt_contact = Entry(Entery_frame,width=20,textvariable=contact,font=('Calibri',16))
txt_contact.place(x=120,y=250)

lb_address = Label(Entery_frame,text="Address:",font=('Calibri',16),bg='#2c3e50',fg='white')
lb_address.place(x=10,y=290)
txt_address= Text(Entery_frame,width=30,height=2,font=('Calibri',16))
txt_address.place(x=10,y=330)

# Define

def hide():
    root.geometry("360x515+0+0")


def show():
    root.geometry("1240x615+0+0")

btn_hide=Button(Entery_frame,text='HIDE',bg='white',bd=1,relief=SOLID,cursor='hand2',command=hide)
btn_hide.place(x=270,y=10)

btn_show=Button(Entery_frame,text='SHOW',bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btn_show.place(x=310,y=10)

def get_data(event):
    sel_row = tv.focus()
    data = tv.item(sel_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txt_address.delete(1.0,END)
    txt_address.insert(END,row[7])

def dis_all():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)



def delete():
    db.remove(row[0])
    clear()
    dis_all()

def clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txt_address.delete(1.0,END)

def add_employee():
    if txt_name.get() == "" or txt_age.get() == "" or txt_jop.get() == "" or txt_email.get() == "" or combo_gen.get() == "" or txt_contact.get() == "" or txt_address.get(1.0,END) == "":
        messagebox.showerror("ERROR","Please fill all the Entries")
        return
    db.insert(
        txt_name.get(),
        txt_age.get(),
        txt_jop.get(),
        txt_email.get(),
        combo_gen.get(),
        txt_contact.get(),
        txt_address.get(1.0,END))
    messagebox.showinfo("Success","Added new Employee")
    clear()
    dis_all()

def update():
    if txt_name.get() == "" or txt_age.get() == "" or txt_jop.get() == "" or txt_email.get() == "" or combo_gen.get() == "" or txt_contact.get() == "" or txt_address.get(1.0,END) == "":
        messagebox.showerror("ERROR","Please fill all the Entries")
        return
    
    db.update(row[0],
            txt_name.get(),
            txt_age.get(),
            txt_jop.get(),
            txt_email.get(),
            combo_gen.get(),
            txt_contact.get(),
            txt_address.get(1.0,END)
            )
    messagebox.showinfo('Success','The Employee data is updata')
    clear()
    dis_all()

# Buttons Frame

btn_frame = Frame(Entery_frame,bg='#2c3e50',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)

btn_add= Button(btn_frame,
                text='Add Details',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#16a085',
                bd=0,
                command=add_employee
                ).place(x=4,y=5)

btn_edit= Button(btn_frame,
                text='Update Details',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#2980b9',
                bd=0,
                command=update
                ).place(x=4,y=50)

btn_delete= Button(btn_frame,
                text='Delete Details',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#c0392b',
                bd=0,
                command=delete
                ).place(x=170,y=5)

btn_clear= Button(btn_frame,
                text='Clear Details',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#f39c12',
                bd=0,
                command=clear
                ).place(x=170,y=50)


# Table Frame

table_frame = Frame(root,bg='white')
table_frame.place(x=365,y=1,width=875,height=610)
style = ttk.Style()
style.configure("mystyle.Treeview",font=('calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('calibri',13))

tv = ttk.Treeview(table_frame, columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text='ID')
tv.column("1",width=40)

tv.heading("2",text='Name')
tv.column("2",width=140)

tv.heading("3",text='Age')
tv.column("3",width=50)

tv.heading("4",text='Jop')
tv.column("4",width=120)

tv.heading("5",text='Email')
tv.column("5",width=150)

tv.heading("6",text='Gender')
tv.column("6",width=90)

tv.heading("7",text='Contact')
tv.column("7",width=150)

tv.heading("8",text='Address')
tv.column("8",width=150)

tv['show']= 'headings'
tv.bind("<ButtonRelease-1>",get_data)

tv.place(x=1,y=1,height=610,width=875)

dis_all()


root.mainloop()