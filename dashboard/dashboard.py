from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import mysql.connector
import main
from dashboard.modul.caribuku import CariBuku


global mydb
global curr

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="users"
)
curr=mydb.cursor()

class Dashboard():
    def Dashboard(self):
        global dashboard
        cal = Dashboard()
        dashboard = Tk()
        dashboard.title("Dashboard")
        dashboard.attributes("-fullscreen", True)
        dashboard.configure(bg = "light cyan")
        screen_width = dashboard.winfo_screenwidth() # get screen width 
        screen_height = dashboard.winfo_screenheight() # get screen height
        top = Label(text = "Dashboard", bg = "spring green", font = ("Calibri", 30, "bold")) # header
        top.place(x = 0, y = 0, width = screen_width, height = screen_height/12) # header placement
        caribuku = ttk.Button(dashboard, text = "Cari Buku", command = cal.CariBuku)
        caribuku.place(x = screen_width/25, y = screen_height/7, width = 150, height = 150)
        #pinjambuku = ttk.Button(dashboard, text = "Pinjam Buku")
        #pinjambuku.place(x = screen_width/7.5, y = screen_height/7, width = 150, height = 150)
        #peminjaman = ttk.Button(dashboard, text = "Peminjaman")
        #peminjaman.place(x = screen_width/4.41, y = screen_height/7, width = 150, height = 150)
        logout_btn = ttk.Button(dashboard, text = "Log out", command = cal.Logout)
        logout_btn.place(x = screen_width/2.28, y = screen_height-100, width=230, height=50)
        dashboard.mainloop()
    def Logout(self):
        back = Tk()
        back.withdraw()
        ask = tkinter.messagebox.askokcancel(title = "Log Out", message = "Apakah anda yakin untuk keluar?")
        if (ask == 1):
            dashboard.destroy()
            get = main.MainWindow()
            get.Main()
        else:
            back.destroy()
    def CariBuku(self):
        dashboard.destroy()
        get = CariBuku()
        get.CariBuku()
        