from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import mysql.connector

global mydb
global curr

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="users"
)
curr=mydb.cursor()
 
 
class MainWindow():
    def Main(self):
        cal = MainWindow()
        global main
        main = Tk()
        main.title("LibrarySystem")
        main.attributes("-fullscreen", True)
        Label(text = "LibrarySystem", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(text = "", bg = "light cyan").pack() #Space
        Button(text = "Login", height = "2", width = "30", command = cal.login).pack()
        Label(text = "", bg = "light cyan").pack() #Space
        Button(text = "Register",height = "2", width = "30", command = cal.Regist).pack()
        Label(text = "", bg = "light cyan").pack() #Space
        Button(text = "Exit",height = "2", width = "30", command = cal.Quit).pack()
        main.configure(bg = "light cyan")
    def Quit(self):
        sys.exit()
    def login(self):
        global loginusrentry
        global loginpassentry
        global mainlogin
        cal = MainWindow()
        mainlogin = Toplevel(main)
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
        btn = Button(mainlogin, text = "Back", height = "2", width = "30", command = mainlogin.destroy).pack()
        mainlogin.configure(bg = "light cyan")
    def Regist(self):
        global registusrentry
        global registpassentry
        global mainregist
        cal = MainWindow()
        mainregist = Toplevel(main)
        mainregist.title("Login")
        mainregist.attributes("-fullscreen", True)
        Label(mainregist, text = "LibrarySystem Register", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(mainregist, text = "", bg = "light cyan").pack() #Space
        Label(mainregist, text = "Username : ", bg = "light cyan", font = ("Calibri", 13)).pack()
        registusrentry = Entry(mainregist, width = "30")
        registusrentry.pack()
        Label(mainregist, text = "", bg = "light cyan").pack() #Space
        Label(mainregist, text = "Password : ", bg = "light cyan", font = ("Calibri", 13)).pack()
        registpassentry = Entry(mainregist, show = "*", width = "30")
        registpassentry.pack()
        Label(mainregist, text = "", bg = "light cyan").pack() #Space
        Button(mainregist, text = "Register", height = "2", width = "30", command = cal.Registdb).pack()
        Label(mainregist, text = "", bg = "light cyan").pack() #Space
        Button(mainregist, text = "Back", height = "2", width = "30", command = mainregist.destroy).pack()
        mainregist.configure(bg = "light cyan")
    def Registdb(self):
        usr = registusrentry.get()
        passwd = registpassentry.get()
        
        if(usr == "" or passwd == ""):
            messagebox.showerror(title = "Error", message = "Masukan Username dan Password")
            mainregist.destroy()
        else:
            curr.execute("INSERT into user(usrname, passwd) values (%s, %s)", (usr, passwd))
            mydb.commit()
            messagebox.showinfo(title = "Success", message = "Akun anda berhasil didaftarkan \n\nSilahkan login")
            mainregist.destroy()
    def Logindb(self):
        cal = MainWindow()
        usr = loginusrentry.get()
        passwd = loginpassentry.get()
        
        if(usr == "" or passwd == ""):
            messagebox.showerror(title = "Error", message = "Masukan Username dan Password")
            mainlogin.destroy()
        else:
            curr.execute("SELECT * from user WHERE usrname = %s AND passwd = %s ",(usr, passwd))
            a = curr.fetchone()
            if a:
                messagebox.showinfo(title = "Success", message = "Welcome "+ usr)
                mainlogin.destroy()
                cal.dashboard()
            else:
                messagebox.showerror(title = "Error", message = "Username atau Password yang anda masukan salah")
                mainlogin.destroy()
    def dashboard(self):
        dashboard = Toplevel(main)
        dashboard.title("Dashboard")
        dashboard.attributes("-fullscreen", True)
        dashboard.configure(bg = "light cyan")
        Label(dashboard, text = "Dashboard", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(dashboard, text = "", bg = "light cyan").pack() #Space
        Button(dashboard, text = "Log out", height = "2", width = "30", command = dashboard.destroy).pack()
        
if __name__ == "__main__":
    cal = MainWindow()
    cal.Main()
    main.mainloop()