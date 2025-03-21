from tkinter import *
import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')
reg_image = PhotoImage(file ='register bg.png')
bg_lable =Label(window,image=reg_image)
bg_lable.place(x=0,y=0, relwidth=1,relheight=1)
window.title("Medicine Management System")
window.iconbitmap('icon.ico')
TopHeadingFrame = Frame(window,width = 700,bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLable = Label(TopHeadingFrame,text='Mesdicine Management System - Add Mesdicine ',font=('Helvetica,24'),fg='red',bg='black')
HeadingLable.grid(row=0,column=0,padx=10,pady=10)
MidFrame = Frame(window,width = 600,bd=1)
MidFrame.pack(side=TOP)

conn = sqlite3.connect('medicin.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'medicine' 
(MedicineName text,MedicineID int,BrandName text,ChemicalComponent text,MFG_Date text,EXP_Date text,Price int)""")
conn.commit()

medicine_name=StringVar()
medicine_name.set('')
medicine_nameLable = Label(MidFrame,text='Medicine Name',font=('Helvetica,16'),fg='orange',bg='black')
medicine_nameLable.grid(row=0,column=0,padx=10,pady=10)
medicine_nameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_name)
medicine_nameTextBox.grid(row=0,column=1,padx=10,pady=10)

medicine_id=IntVar()
medicine_id.set('')
medicine_idLable = Label(MidFrame,text='Medicine ID',font=('Helvetica,16'),fg='orange',bg='black')
medicine_idLable.grid(row=1,column=0,padx=10,pady=10)
medicine_idTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_id)
medicine_idTextBox.grid(row=1,column=1,padx=10,pady=10)

brand_name=StringVar()
brand_name.set('')
brand_nameLable = Label(MidFrame,text='Brand Name',font=('Helvetica,16'),fg='orange',bg='black')
brand_nameLable.grid(row=2,column=0,padx=10,pady=10)
brand_nameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=brand_name)
brand_nameTextBox.grid(row=2,column=1,padx=10,pady=10)

chemical_component=StringVar()
chemical_component.set('')
chemical_componentLable = Label(MidFrame,text='Chemical Component',font=('Helvetica,16'),fg='orange',bg='black')
chemical_componentLable.grid(row=3,column=0,padx=10,pady=10)
chemical_componentTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=chemical_component)
chemical_componentTextBox.grid(row=3,column=1,padx=10,pady=10)

mfg=StringVar()
mfg.set('')
mfgLable = Label(MidFrame,text='MFG_Date',font=('Helvetica,16'),fg='orange',bg='black')
mfgLable.grid(row=4,column=0,padx=10,pady=10)
mfgTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=mfg)
mfgTextBox.grid(row=4,column=1,padx=10,pady=10)

exp=StringVar()
exp.set('')
expLable = Label(MidFrame,text='EXP_Date',font=('Helvetica,16'),fg='orange',bg='black')
expLable.grid(row=5,column=0,padx=10,pady=10)
expTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=exp)
expTextBox.grid(row=5,column=1,padx=10,pady=10)

price=IntVar()
price.set('')
priceLable = Label(MidFrame,text='Price',font=('Helvetica,16'),fg='orange',bg='black')
priceLable.grid(row=6,column=0,padx=10,pady=10)
priceTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=price)
priceTextBox.grid(row=6,column=1,padx=10,pady=10)

def add():
    conn = sqlite3.connect('medicin.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'medicine' (MedicineName,MedicineID,BrandName,ChemicalComponent,MFG_Date,EXP_Date,Price) values(?,?,?,?,?,?,?)""",
                   (str(medicine_name.get()),str(medicine_id.get()),str(brand_name.get()),str(chemical_component.get()),str(mfg.get()),str(exp.get()),str(price.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('ADD MEDICINE','New Medicine added',icon='info')
    else:
        msg.showinfo('Error','New Medicine not added',icon='warning')
        window.destroy()
        import home

def back():
    window.destroy()
    import home

add_btn = Button(MidFrame,text='ADD',command=add,font=('Helvetica,18'),fg='black',bg='green')
add_btn.grid(row=7,column=1,padx=10,pady=10)

back_btn = Button(MidFrame,text='BACK',command=back,font=('Helvetica,18'),fg='black',bg='blue')
back_btn.grid(row=8,column=1,padx=10,pady=10)

window.mainloop()