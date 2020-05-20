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


class RegistSystem():    
    def Regist(self):
        global registusrentry
        global registpassentry
        global mainregist
        cal = RegistSystem()
        mainregist = Tk()
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
        Button(mainregist, text = "Back", height = "2", width = "30", command = cal.Back).pack()
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
            #messagebox.showinfo(title = "Success", message = "Akun anda berhasil didaftarkan \n\nSilahkan login")
            mainregist.destroy()
            get = main.MainWindow()
            get.Main()
    def Back(self):
        cal = main.MainWindow()
        cal.Main()
        mainregist.destroy()