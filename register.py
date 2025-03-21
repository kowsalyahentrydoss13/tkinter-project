from tkinter import *
import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')
reg_image = PhotoImage(file ='register bg.png')
bg_lable =Label(window,image=reg_image)
bg_lable.place(x=0,y=0, relwidth=1,relheight=1)
window.title("Medicine Management System")
TopHeadingFrame = Frame(window,width = 700,bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLable = Label(TopHeadingFrame,text='Mesdicine Management System - Register',font=('Helvetica,24'),fg='red',bg='black')
HeadingLable.grid(row=0,column=0,padx=10,pady=10)
MidFrame = Frame(window,width = 600,bd=1)
MidFrame.pack(side=TOP)

conn = sqlite3.connect('medicin.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'userdata' 
(Name text,ID int,Number int,Email text,Password text,Confirmpassword text)""")
conn.commit()

name=StringVar()
name.set('')
NameLable = Label(MidFrame,text='Name',font=('Helvetica,16'),fg='orange',bg='black')
NameLable.grid(row=0,column=0,padx=10,pady=10)
NameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=name)
NameTextBox.grid(row=0,column=1,padx=10,pady=10)

id=IntVar()
id.set('')
IdLable = Label(MidFrame,text='ID',font=('Helvetica,16'),fg='orange',bg='black')
IdLable.grid(row=1,column=0,padx=10,pady=10)
IdTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=id)
IdTextBox.grid(row=1,column=1,padx=10,pady=10)

number=IntVar()
number.set('')
NumberLable = Label(MidFrame,text='Number',font=('Helvetica,16'),fg='orange',bg='black')
NumberLable.grid(row=2,column=0,padx=10,pady=10)
NumberTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=number)
NumberTextBox.grid(row=2,column=1,padx=10,pady=10)

email=StringVar()
email.set('')
EmailLable = Label(MidFrame,text='Email',font=('Helvetica,16'),fg='orange',bg='black')
EmailLable.grid(row=3,column=0,padx=10,pady=10)
EmailTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=email)
EmailTextBox.grid(row=3,column=1,padx=10,pady=10)

password=StringVar()
password.set('')
PasswordLable = Label(MidFrame,text='Password',font=('Helvetica,16'),fg='orange',bg='black')
PasswordLable.grid(row=4,column=0,padx=10,pady=10)
PasswordTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=password)
PasswordTextBox.grid(row=4,column=1,padx=10,pady=10)

confirmpassword=StringVar()
confirmpassword.set('')
ConfirmpasswordLable = Label(MidFrame,text='Confirm Password',font=('Helvetica,16'),fg='orange',bg='black')
ConfirmpasswordLable.grid(row=5,column=0,padx=10,pady=10)
ConfirmpasswordTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=confirmpassword)
ConfirmpasswordTextBox.grid(row=5,column=1,padx=10,pady=10)

def register():
    conn = sqlite3.connect('medicin.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'userdata' (Name,ID,Number,Email,Password,Confirmpassword) values(?,?,?,?,?,?)""",
                   (str(name.get()),str(id.get()),str(number.get()),str(email.get()),str(password.get()),str(confirmpassword.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('Confirmation','New user added',icon='info')
    else:
        msg.showinfo('Error','New user not added',icon='warning')
        window.destroy()
        import home

def login():
    window.destroy()
    import login

submit_btn = Button(MidFrame,text='Submit',command=register,font=('Helvetica,18'),fg='black',bg='green')
submit_btn.grid(row=6,column=1,padx=10,pady=10)

AlreadyuserLable = Label(MidFrame,text='Already a user',font=('Helvetica,16'),fg='orange',bg='black')
AlreadyuserLable.grid(row=7,column=0,padx=10,pady=10)

login_btn = Button(MidFrame,text='Login',command=login,font=('Helvetica,18'),fg='black',bg='blue')
login_btn.grid(row=7,column=1,padx=10,pady=10)
window.mainloop()





