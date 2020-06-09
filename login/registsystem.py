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

class RegistSystem():    
    def Regist(self):
        global registusrentry
        global registpassentry
        global mainregist
        cal = RegistSystem()
        mainregist = Tk()
        mainregist.title("Login")
        mainregist.attributes("-fullscreen", True)
        screen_width = mainregist.winfo_screenwidth() # get screen width 
        screen_height = mainregist.winfo_screenheight() # get screen height
        top = Label(mainregist, text = "LibrarySystem", bg = "spring green", font = ("Calibri", 30, "bold")) # header
        top.place(x = 0, y = 0, width = screen_width, height = screen_height/12) # header placement
        usrname_label = Label(mainregist, text = "Username : ", bg = "light cyan", font = ("Calibri", 20)) #usrname label
        usrname_label.place(x = screen_width/2.16, y = screen_height/11) #usrname_label placement
        registusrentry = ttk.Entry(mainregist) # loginusr entry
        registusrentry.place(x = screen_width/2.28, y = screen_height/7.5, width = 230, height = 30) #registusrentry placement
        passwd_label = Label(mainregist, text = "Password : ", bg = "light cyan", font = ("Calibri", 20)) #passwd label
        passwd_label.place(x = screen_width/2.15, y = screen_height/6) #passwd_label placement
        registpassentry = ttk.Entry(mainregist, show = "*") #registpass entry
        registpassentry.place(x = screen_width/2.28, y = screen_height/4.8, width = 230, height = 30) #registpassentry placement
        regist_btn = ttk.Button(mainregist, text = "Register", command = cal.Registdb) #regist button
        regist_btn.place(x = screen_width/2.28, y = screen_height/4, width=230,height=50) #regist_btn placement
        back_btn = ttk.Button(mainregist, text = "Back", command = cal.Back) #back button
        back_btn.place(x = screen_width/2.28, y = screen_height/3.25, width=230,height=50) #back_btn placement
        mainregist.configure(bg = "light cyan")
    def Registdb(self):
        usr = registusrentry.get()
        passwd = registpassentry.get()
        cal = RegistSystem()
       
        if(usr == "" or passwd == ""):
            cal.NoInput()
        else:
            try:
                curr.execute("INSERT into user(usrname, passwd) values (%s, %s)", (usr, passwd))
                mydb.commit()
                cal.RegistSuccess()
                mainregist.destroy()
                get = main.MainWindow()
                get.Main()
            except mysql.connector.Error as Error:
                cal.UsrDouble()
    def Back(self):
        cal = main.MainWindow()
        cal.Main()
        mainregist.destroy()
    def NoInput(self):
        noinput = Tk()
        noinput.withdraw()
        tkinter.messagebox.showwarning(title="Error", message="Masukan Username dan Password")
        noinput.destroy()
    def RegistSuccess(self):
        cal = RegistSystem()
        registsuccess = Tk()
        registsuccess.withdraw()
        tkinter.messagebox.showinfo(title="Success", message="Akun anda berhasil didaftarkan \n\nSilahkan login")
        registsuccess.destroy()
    def UsrDouble(self):
        cal = RegistSystem()
        UserDouble = Tk()
        UserDouble.withdraw()
        tkinter.messagebox.showinfo(title="Error", message="Username yang anda masukan sudah terdaftar\nLogin dengan username yang telah ada atau pilih username lain")
        UserDouble.destroy()