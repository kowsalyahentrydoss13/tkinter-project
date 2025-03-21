from tkinter import *
import sqlite3
import tkinter.messagebox as msg
from tkinter import ttk 

from register import cursor

window = Tk()
window.geometry('900x600')
reg_image = PhotoImage(file ='register bg.png')
bg_lable =Label(window,image=reg_image)
bg_lable.place(x=0,y=0, relwidth=1,relheight=1)
window.title("Medicine Management System")
window.iconbitmap('icon.ico')
TopHeadingFrame = Frame(window,width = 700,bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLable = Label(TopHeadingFrame,text='Mesdicine Management System - View Mesdicine ',font=('Helvetica,24'),fg='red',bg='black')
HeadingLable.grid(row=0,column=0,padx=10,pady=1)
MidFrame = Frame(window,width = 700,bd=1)
MidFrame.pack(side=TOP)


view_frame = Frame(window,bd=1)
view_frame.pack(side=TOP,fill=X)

tv=ttk.Treeview(view_frame,columns=
('MedicineName','MedicineID','BrandName','ChemicalComponent','MFG_Date','EXP_Date','Price'))
tv.heading('#1',text='MedicineName')
tv.heading('#2',text='MedicineID')
tv.heading('#3',text='BrandName')
tv.heading('#4',text='ChemicalComponent')
tv.heading('#5',text='MFGDate')
tv.heading('#6',text='EXPDate')
tv.heading('#7',text='Price')
tv.column('#0',width=0,stretch=NO)
tv.column('#1',width=50)
tv.column('#2',width=50)
tv.column('#3',width=50)
tv.column('#4',width=50)
tv.column('#5',width=50)
tv.column('#6',width=50)
tv.column('#7',width=50)

tv.pack(fill=X)


try:
    conn = sqlite3.connect('medicin.db')
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM medicine")
    data = cursor.fetchall()


    for row in data:
        tv.insert("", 'end', values=row)

except sqlite3.Error as e:
    msg.showerror("Database Error", f"An error occurred: {e}")
finally:
    if conn:
        conn.close()

def back():
    window.destroy()
    import home


back_btn = Button(
    MidFrame,
    text='BACK',
    command=back,
    font=('Helvetica', 18),
    fg='black',
    bg='blue',
)
back_btn.grid(row=8, column=1, padx=10, pady=10)



window.mainloop()