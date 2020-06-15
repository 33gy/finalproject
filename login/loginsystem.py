from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import main
import mysql.connector
from dashboard import dashboard, admindashboard


global mydb
global curr

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="users"
)
curr=mydb.cursor()


class LoginSystem():
    def Login(self):
        global loginusrentry
        global loginpassentry
        global mainlogin
        cal = LoginSystem()
        mainlogin = Tk()
        mainlogin.title("Login")
        mainlogin.attributes("-fullscreen", True)
        screen_width = mainlogin.winfo_screenwidth() # get screen width 
        screen_height = mainlogin.winfo_screenheight() # get screen height
        top = Label(mainlogin, text = "LibrarySystem", bg = "spring green", font = ("Calibri", 30, "bold")) # header
        top.place(x = 0, y = 0, width = screen_width, height = screen_height/12) # header placement
        usrname_label = Label(mainlogin, text = "Username : ", bg = "light cyan", font = ("Calibri", 20)) #usrname label
        usrname_label.place(x = screen_width/2.16, y = screen_height/11) #usrname_label placement
        loginusrentry = ttk.Entry(mainlogin) # loginusr entry
        loginusrentry.place(x = screen_width/2.28, y = screen_height/7.5, width = 230, height = 30) #loginusrentry placement
        passwd_label = Label(mainlogin, text = "Password : ", bg = "light cyan", font = ("Calibri", 20)) #passwd label
        passwd_label.place(x = screen_width/2.15, y = screen_height/6) #passwd_label placement
        loginpassentry = ttk.Entry(mainlogin, show = "*") #loginpass entry
        loginpassentry.place(x = screen_width/2.28, y = screen_height/4.8, width = 230, height = 30) #loginpassentry placement
        login_btn = ttk.Button(mainlogin, text = "Login", command = cal.Logindb) #login button
        login_btn.place(x = screen_width/2.28, y = screen_height/4, width=230,height=50) #login_btn placement
        back_btn = ttk.Button(mainlogin, text = "Back", command = cal.Back) #back button
        back_btn.place(x = screen_width/2.28, y = screen_height/3.25, width=230,height=50) #back_btn placement
        mainlogin.configure(bg = "light cyan")
    def Logindb(self):
        usr = loginusrentry.get()
        passwd = loginpassentry.get()
        cal = LoginSystem()
        
        if(usr == "" or passwd == ""):
            cal.NoInput()
        else:
            mydb.commit()
            curr.execute("SELECT * from admin WHERE usrname = %s AND passwd = %s",(usr, passwd))
            usrgetadmin = curr.fetchone()
            curr.execute("SELECT * from user WHERE usrname = %s AND passwd = %s",(usr, passwd))
            usrget = curr.fetchone()
            if (usrgetadmin):
                mainlogin.destroy()
                get = admindashboard.AdminDashboard()
                get.AdminDashboard()
            elif (usrget):
                mainlogin.destroy()
                get = dashboard.Dashboard()
                get.Dashboard()
            else:
                cal.ErrorLogin()
    def Back(self):
        cal = main.MainWindow()
        cal.Main()
        mainlogin.destroy()
    def NoInput(self):
        noinput = Tk()
        noinput.withdraw()
        tkinter.messagebox.showinfo(title="Error", message="Masukan Username dan Password")
        noinput.destroy()
    def ErrorLogin(self):
        cal = LoginSystem()
        errorlogin = Tk()
        errorlogin.withdraw()
        tkinter.messagebox.showinfo(title="Error", message="Username atau Password yang anda masukan salah")
        errorlogin.destroy()