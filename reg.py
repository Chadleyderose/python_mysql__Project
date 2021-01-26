from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
from datetime import *




Register = Tk()
Register.title("Create student")
Register.resizable(False, False)



db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

def show():
    Password.config(show="")

#Welcome intro



Full_name = Label(Register, text="Full Name:", fg="white", bg="black")
full_name = Entry(Register)
Username_label = Label(Register, text="Username:", fg="white", bg="black")
Password_label = Label(Register, text="Password:", fg="white", bg="black")

Username = Entry(Register)
Password = Entry(Register, show='*')

def addUser():
    try:
        user_info = (full_name.get(), str(Username.get()), str(Password.get()))
        comm = "INSERT INTO users (fullname, username, password) VALUES (%s, %s, %s)"

        cursor.execute(comm, user_info)

        db.commit()
        mb.showinfo("Confirmation", "User Created Successfully")
        Register.destroy()


    except :
        mb.showerror("Well Done", "You Have logged in ")
    Register.destroy()

def back():
    Register.destroy()
    import main

Createbtn = Button(Register, text="Create student", command=addUser)
Backbtn = Button(Register, text="Back", command=back)
ShowPassword = Checkbutton(Register, text="Show Password", command=show, fg="white", bg="black")

Full_name.place(x=10, y=100)
full_name.place(x=90, y=100)
Username_label.place(x=10, y=140)
Username.place(x=90, y=140)
Password_label.place(x=10, y=180)
Password.place(x=90, y=180)
Createbtn.place(x=10, y=220)
Backbtn.place(x=350, y=220)
ShowPassword.place(x=250, y=140)


#Center Gui to screen
window_height = 270
window_width = 400

screen_width = Register.winfo_screenwidth()
screen_height = Register.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

Register.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


Register.config(bg="black")
Register.geometry("400x270")
Register.mainloop()
