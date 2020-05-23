from tkinter import *
import tkinter.messagebox
import sys
from login import loginsystem, registsystem
from dashboard import dashboard, admindashboard


class MainWindow():
    def Main(self):
        cal = MainWindow()
        global main
        main = Tk()
        main.title("LibrarySystem")
        main.attributes("-fullscreen", True)
        Label(text = "LibrarySystem", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(text = "", bg = "light cyan").pack() #Space
        Button(text = "Login", height = "2", width = "30", command = cal.Login).pack()
        Label(text = "", bg = "light cyan").pack() #Space
        Button(text = "Register",height = "2", width = "30", command = cal.Regist).pack()
        Label(text = "", bg = "light cyan").pack() #Space
        Button(text = "Exit",height = "2", width = "30", command = cal.Quit).pack()
        main.configure(bg = "light cyan")
    def Quit(self):
        back = Tk()
        back.withdraw()
        ask = tkinter.messagebox.askokcancel(title = "Quit", message = "Apakah anda yakin untuk keluar?")
        if (ask == 1):
            back.destroy()
            sys.exit()
        else:
            back.destroy()  
    def Login(self):
        get = loginsystem.LoginSystem()
        get.Login()
        main.destroy()
    def Regist(self):
        get = registsystem.RegistSystem()
        get.Regist()
        main.destroy()
if __name__ == "__main__":
    cal = MainWindow()
    cal.Main()
    main.mainloop()