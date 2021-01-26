# Register System with Python GUI and MySQL
import mysql.connector
from tkinter import messagebox as mb
from tkinter import *
from datetime import *
import os

db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()


admin_login = Tk()
admin_login.resizable(False, False)
admin_login.title("Admin")


#Welcome intro









def login():
    User = UserEnt.get()
    p = adUps.get()
    sql = "select * from admin where username=%s and password=%s"
    cursor.execute(sql, [(User), (p)])
    datab = cursor.fetchall()

    if datab:
        mb.showinfo("Login", "login successful")
        admin_login.destroy()
        import tkinter_gui.admin_rights_FE
    else:
        mb.showerror("Unsuccessful", "Login failed")

def back():
    admin_login.destroy()
    import main



Loginbtn = Button(admin_login, text="Back", command=back)
Privilegebtn = Button(admin_login, text="Login", command=login)

UserAddlabel = Label(admin_login, text="User/Admin Name:", fg="white", bg="black")
UserEnt = Entry(admin_login)
UserAddPassword = Label(admin_login, text="Password", fg="white", bg="black")
adUps = Entry(admin_login)
UserAddlabel.place(x=20, y=100)
UserEnt.place(x=150, y=100)
UserAddPassword.place(x=20, y=140)
adUps.place(x=150, y=140)
Privilegebtn.place(x=20, y=180)
Loginbtn.place(x=320, y=180)



#Center gui on screen
window_height = 240
window_width = 400

screen_width = admin_login.winfo_screenwidth()
screen_height = admin_login.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

admin_login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
admin_login.geometry("400x240")
admin_login.configure(bg="black")
admin_login.mainloop()


