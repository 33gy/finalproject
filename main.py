from tkinter import *
import tkinter.ttk as ttk
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
        screen_width = main.winfo_screenwidth() # get screen width 
        screen_height = main.winfo_screenheight() # get screen height
        top = Label(text = "LibrarySystem", bg = "spring green", font = ("Calibri", 30, "bold")) # header
        top.place(x = 0, y = 0, width = screen_width, height = screen_height/12) # header placement
        #text_header = Label(text = "Silahkan pilih menu di bawah", bg = "light cyan", font = ("Calibri", 17)) 
        #text_header.place(x = screen_width/2.33, y = screen_height/11)
        login_btn = ttk.Button(text = "Login", width = "30", command = cal.Login) # login button
        login_btn.place(x = screen_width/2.27, y = screen_height/8, width=230,height=50)# login_btn placement
        regist_btn = ttk.Button(text = "Register", width = "30", command = cal.Regist) # register button
        regist_btn.place(x = screen_width/2.27, y = screen_height/5.5, width=230,height=50) # regist_btn placement
        exit_btn = ttk.Button(text = "Exit", width = "30", command = cal.Quit) # Exit button
        exit_btn.place(x = screen_width/2.27, y = screen_height/4.2, width=230,height=50) # exit_btn placement
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