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
HeadingLable = Label(TopHeadingFrame,text='Mesdicine Management System - Delete Mesdicine ',font=('Helvetica,24'),fg='red',bg='black')
HeadingLable.grid(row=0,column=0,padx=10,pady=10)
MidFrame = Frame(window,width = 600,bd=1)
MidFrame.pack(side=TOP)


Label(MidFrame, text="Medicine Name:", font=('Helvetica', 18)).grid(row=0, column=0, padx=10, pady=10)
MedicineName = Entry(MidFrame, font=('Helvetica', 18))
MedicineName.grid(row=0, column=1, padx=10, pady=10)


def delete():
    medicine_name = MedicineName.get().strip()
    if not medicine_name:
        msg.showerror("Error", "Please enter a medicine name to delete!")
        return

    try:
        conn = sqlite3.connect('medicin.db')  # Ensure the database file exists
        cursor = conn.cursor()
        cursor.execute("DELETE FROM medicine WHERE MedicineName = ?", (medicine_name,))
        conn.commit()

        if cursor.rowcount > 0:
            msg.showinfo("Success", f"Medicine '{medicine_name}' deleted successfully!")
        else:
            msg.showwarning("Not Found", f"No medicine found with the name '{medicine_name}'.")

    except sqlite3.Error as e:
        msg.showerror("Database Error", f"An error occurred: {str(e)}")
    finally:
        conn.close()


delete_btn = Button(
    MidFrame,
    text='DELETE MEDICINE',
    command=delete,
    font=('Helvetica', 18),
    fg='black',
    bg='green'
)
delete_btn.grid(row=1, column=1, padx=10, pady=10)
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
back_btn.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()