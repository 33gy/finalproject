from tkinter import *
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
        Label(dashboard, text = "Dashboard", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(dashboard, text = "", bg = "light cyan").pack() #Space
        caribuku = Button(dashboard, text = "Cari Buku", height = "7", width = "20", bg = "pale green", command = cal.CariBuku)
        caribuku.place(x = 30, y = 120)
        pinjambuku = Button(dashboard, text = "Pinjam Buku", height = "7", width = "20", bg = "pale green")
        pinjambuku.place(x = 200, y = 120)
        peminjaman = Button(dashboard, text = "Peminjaman", height = "7", width = "20", bg = "pale green")
        peminjaman.place(x = 370, y = 120)
        Label(dashboard, text = "", bg = "light cyan").pack() #Space
        Button(dashboard, text = "Log out", height = "2", width = "30", command = cal.Logout).pack()
        dashboard.mainloop()
    def Logout(self):
        back = Tk()
        back.withdraw()
        ask = tkinter.messagebox.askokcancel(title = "Log Out", message = "Apakah anda yakin untuk keluar?")
        if (ask == 1):
            dashboard.destroy()
            #curr.reset(free=True)
            get = main.MainWindow()
            get.Main()
        else:
            back.destroy()
    def CariBuku(self):
        dashboard.destroy()
        get = CariBuku()
        get.CariBuku()
        