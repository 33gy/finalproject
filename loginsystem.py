from tkinter import *
from tkinter import messagebox
import main, dashboard, admindashboard
import mysql.connector


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
        Label(mainlogin, text = "LibrarySystem Login", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(mainlogin, text = "", bg = "light cyan").pack() #Space
        Label(mainlogin, text = "Username : ", bg = "light cyan", font = ("Calibri", 13)).pack()
        loginusrentry = Entry(mainlogin, width = "30")
        loginusrentry.pack()
        Label(mainlogin, text = "", bg = "light cyan").pack() #Space
        Label(mainlogin, text = "Password : ", bg = "light cyan", font = ("Calibri", 13)).pack()
        loginpassentry = Entry(mainlogin, show = "*", width = "30")
        loginpassentry.pack()
        Label(mainlogin, text = "", bg = "light cyan").pack() #Space
        Button(mainlogin, text = "Login", height = "2", width = "30", command = cal.Logindb).pack()
        Label(mainlogin, text = "", bg = "light cyan").pack() #Space
        btn = Button(mainlogin, text = "Back", height = "2", width = "30", command = cal.Back).pack()
        mainlogin.configure(bg = "light cyan")
    def Logindb(self):
        usr = loginusrentry.get()
        passwd = loginpassentry.get()
        
        if(usr == "" or passwd == ""):
            messagebox.showerror(title = "Error", message = "Masukan Username dan Password")
        else:
            curr.execute("SELECT * from admin WHERE usrname = %s AND passwd = %s",(usr, passwd))
            usrgetadmin = curr.fetchone()
            curr.execute("SELECT * from user WHERE usrname = %s AND passwd = %s",(usr, passwd))
            usrget = curr.fetchone()
            if (usrgetadmin):
                #messagebox.showinfo(title = "Success", message = "Welcome "+ usr)
                mainlogin.destroy()
                get = admindashboard.AdminDashboard()
                get.AdminDashboard()
            elif (usrget):
                #messagebox.showinfo(title = "Success", message = "Welcome "+ usr)
                mainlogin.destroy()
                get = dashboard.Dashboard()
                get.Dashboard()
            else:
                #messagebox.showerror(title = "Error", message = "Username atau Password yang anda masukan salah")
                mainlogin.destroy()
    def Back(self):
        cal = main.MainWindow()
        cal.Main()
        mainlogin.destroy()
    def logincal(self):
        mainlogin.mainloop()