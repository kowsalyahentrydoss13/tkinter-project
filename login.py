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
HeadingLable = Label(TopHeadingFrame,text='Mesdicine Management System - Login',font=('Helvetica,24'),fg='red',bg='black')
HeadingLable.grid(row=0,column=0,padx=10,pady=10)
MidFrame = Frame(window,width = 600,bd=1)
MidFrame.pack(side=TOP)



name=StringVar()
name.set('')
NameLable = Label(MidFrame,text='Name',font=('Helvetica,16'),fg='orange',bg='black')
NameLable.grid(row=0,column=0,padx=10,pady=10)
NameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=name)
NameTextBox.grid(row=0,column=1,padx=10,pady=10)

password=StringVar()
password.set('')
PasswordLable = Label(MidFrame,text='Password',font=('Helvetica,16'),fg='orange',bg='black')
PasswordLable.grid(row=2,column=0,padx=10,pady=10)
PasswordTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=password)
PasswordTextBox.grid(row=2,column=1,padx=10,pady=10)
def login():
    conn = sqlite3.connect('medicin.db')
    cursor = conn.cursor()
    cursor.execute("""select * from 'userdata' where Name = ? and Password = ?""",
                   (name.get(),password.get()))
    conn.commit()
    if len(list(cursor.fetchall())) >0:
        msg.showinfo('Success', 'Login successful', icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo('Error', 'Invalid name or password', icon='warning')
def register():
    window.destroy()
    import register


submit_btn = Button(MidFrame,text='Login',command=login,font=('Helvetica,18'),fg='black',bg='blue')
submit_btn.grid(row=3,column=1,padx=10,pady=10)

NotuserLable = Label(MidFrame,text='Not a user get ?',font=('Helvetica,16'),fg='orange',bg='black')
NotuserLable.grid(row=4,column=0,padx=10,pady=10)

register_btn = Button(MidFrame,text='Register',command=register,font=('Helvetica,18'),fg='black',bg='red')
register_btn.grid(row=4,column=1,padx=10,pady=10)

window.mainloop()