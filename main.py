from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
from datetime import *


db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()
cursor.execute("create database if not exists lifechoicesonline")
db.commit()
cursor.execute("use lifechoicesonline")
db.commit()
cursor.execute("create table if not exists users (id int(11) NOT NULL auto_increment , username varchar(50) default null, password varchar(20) default null, fullname varchar(60) default null, logintime timestamp , logouttime timestamp, primary key(id))")
cursor.execute("create table if not exists admin (id int(11) NOT NULL auto_increment, username varchar(60) default null, password varchar(20) default null,  logintime timestamp , logouttime timestamp , fullname varchar(60) default null, primary key(id))")
cursor.execute("create table if not exists visitors (id int(11) NOT NULL auto_increment , username varchar(50) default null, password varchar(20) default null, fullname varchar(60) default null, logintime timestamp , logouttime timestamp, primary key(id))")
db.commit()

# Creates the tables if it does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS time_in(full_name varchar(60) Default null, date date, logged_in time)")
db.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS time_out(full_name varchar(60) Default null, date date, logged_out time)")
db.commit()

def show():
    Password.config(show="")

def showAdmin():  # Function to show admin
    Login.destroy()
    import admin_login


def login():  # Function to login
    User = Username.get()
    password = Password.get()
    sql = "select * from users where username=%s and password=%s"
    cursor.execute(sql, [(User), (password)])
    datab = cursor.fetchall()
    login = datetime.now()
    x = login.strftime("%H:%M:%S")

    Date_time = login.strftime("%d/%m/%y")
    time = User, str(Date_time), str(x)
    comm_time = "INSERT INTO time_in(full_name, date, logged_in)VALUES (%s, %s, %s)"
    cursor.execute(comm_time, time)
    db.commit()
    mb.showinfo("Message", "Login successfully")

    if datab:
        Login.destroy()
        logout = datetime.now()
        y = logout.strftime("%H:%M:%S")
        time1 = User, str(Date_time),  str(y)
        comm_time1 = "INSERT INTO time_out(full_name, date, logged_out)VALUES (%s, %s, %s)"
        cursor.execute(comm_time1, time1)
        db.commit()

        phone = Tk()
        phone.title("Logout")
        phone.geometry("400x200")



        mobile = Label(phone, text="Mobile Number", bg="black", fg="white")
        mobile.place(x=10, y=100)

        mobile_ent = Entry(phone)
        mobile_ent.place(x=110, y=100)

        def log_out():
            logout = datetime.now()
            y = logout.strftime("%H:%M:%S")
            time1 = User, str(Date_time), str(y)
            comm_time1 = "INSERT INTO time_out(full_nameRF, date, logout_time)VALUES (%s, %s, %s)"
            cursor.execute(comm_time1, time1)
            db.commit()
            mb.showinfo("Login", "logout successful")
            phone.destroy()

        signOut = Button(phone, text="sign out", command=log_out)
        signOut.place(x=180, y=160)

        # Center Gui to screen
        window_height = 200
        window_width = 400

        screen_width = phone.winfo_screenwidth()
        screen_height = phone.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        phone.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        phone.configure(bg="black")
        phone.mainloop()

    else:
        mb.showerror("Unsuccessful", "Login failed")





def createUser():
    Login.destroy()
    import reg


Login = Tk()
Login.resizable(False, False)
Login.title("Login")


#Welcome intro



User_label = Label(Login, text="Username:", fg="white", bg="black")
Password_label = Label(Login, text="Password:", fg="white", bg="black")
Username = Entry(Login)
Password = Entry(Login, show='*')





button = Button(Login, text="register", width=10, command=createUser)  # Button to create users

Loginbtn = Button(Login, text="login", width=10, command=login)  # Button to login



ShowPassword = Checkbutton(Login, text="Show Password", command=show)
# Placing widgets for Login window
User_label.place(x=10, y=120)
Username.place(x=85, y=120)
Password_label.place(x=10, y=170)
Password.place(x=85, y=170)
ShowPassword.place(x=250, y=145)
button.place(x=110, y=230)
Loginbtn.place(x=210, y=230)


#Center Gui to screen
window_height = 270
window_width = 400

screen_width = Login.winfo_screenwidth()
screen_height = Login.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

Login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

Login.bind("<Control-a>", lambda i: showAdmin())
Login.configure(bg="black")
Login.geometry("400x270")
Login.mainloop()
