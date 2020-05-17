from tkinter import *
from tkinter import ttk
import sys
import mysql.connector
from tkinter import messagebox

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
        main.title('LibrarySystem')
        main.attributes("-fullscreen", True)
        #main.geometry('600x600')
        Label(text = "LibrarySystem", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, 'bold')).pack()
        Label(text = '', bg = 'light cyan').pack() #Space
        Button(text = "Login", height = "2", width = "30", command = cal.login).pack()
        Label(text = '', bg = 'light cyan').pack() #Space
        Button(text = "Register",height = "2", width = "30", command = cal.Regist).pack()
        Label(text = '', bg = 'light cyan').pack() #Space
        Button(text = "Exit",height = "2", width = "30", command = cal.Quit).pack()
        main.configure(bg='light cyan')
        #main.mainloop()
    def Quit(self):
        sys.exit()
    def login(self):
        global loginusrentry
        global loginpassentry
        cal = MainWindow()
        mainlogin = Toplevel(main)
        mainlogin.title('Login')
        mainlogin.attributes("-fullscreen", True)
        Label(mainlogin, text = "LibrarySystem Login", bg = "spring green", width = '300', height = "2", font = ("Calibri", 20, 'bold')).pack()
        Label(mainlogin, text = '', bg = 'light cyan').pack() #Space
        Label(mainlogin, text = 'Username : ', bg = 'light cyan', font = ('Calibri', 13)).pack()
        loginusrentry = Entry(mainlogin, width = '30')
        loginusrentry.pack()
        Label(mainlogin, text = '', bg = 'light cyan').pack() #Space
        Label(mainlogin, text = 'Password : ', bg = 'light cyan', font = ('Calibri', 13)).pack()
        loginpassentry = Entry(mainlogin, show = '*', width = '30')
        loginpassentry.pack()
        Label(mainlogin, text = '', bg = 'light cyan').pack() #Space
        Button(mainlogin, text = "Login", height = "2", width = "30").pack()
        Label(mainlogin, text = '', bg = 'light cyan').pack() #Space
        btn = Button(mainlogin, text = "Back", height = "2", width = "30", command = mainlogin.destroy).pack()
        mainlogin.configure(bg='light cyan')
        #mainlogin.geometry('600x600')
    def Regist(self):
        global registusrentry
        global registpassentry
        global mainregist
        cal = MainWindow()
        mainregist = Toplevel(main)
        mainregist.title('Login')
        mainregist.attributes("-fullscreen", True)
        Label(mainregist, text = "LibrarySystem Register", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, 'bold')).pack()
        Label(mainregist, text = '', bg = 'light cyan').pack() #Space
        Label(mainregist, text = 'Username : ', bg = 'light cyan', font = ('Calibri', 13)).pack()
        registusrentry = Entry(mainregist, width = '30')
        registusrentry.pack()
        Label(mainregist, text = '', bg = 'light cyan').pack() #Space
        Label(mainregist, text = 'Password : ', bg = 'light cyan', font = ('Calibri', 13)).pack()
        registpassentry = Entry(mainregist, show = '*', width = '30')
        registpassentry.pack()
        Label(mainregist, text = '', bg = 'light cyan').pack() #Space
        Button(mainregist, text = "Register", height = "2", width = "30", command = cal.Registdb).pack()
        Label(mainregist, text = '', bg = 'light cyan').pack() #Space
        Button(mainregist, text = "Back", height = "2", width = "30", command = mainregist.destroy).pack()
        mainregist.configure(bg='light cyan')
        #mainlogin.geometry('600x600')
    def Registdb(self):
        data = (
            registusrentry.get(),
            registpassentry.get()
        )
        a=registusrentry.get()
        b=registpassentry.get()
        if(a=="" or b==""):
            messagebox.showerror(title = 'Error', message='Masukan Username dan Password')
            mainregist.destroy()
        else:
            curr.execute('INSERT into user(usrname, passwd) values (%s, %s)', data)
            mydb.commit()
            messagebox.showinfo(title = 'Success', message = 'Akun anda berhasil didaftarkan')
            mainregist.destroy()
    #def Logindb(self):
        #data = (
            #loginusrentry.get()
            #loginpassentry.get()
        #)
        #curr.execute()
        
if __name__ == "__main__":
    cal = MainWindow()
    cal.Main()
    main.mainloop()