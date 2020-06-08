from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import mysql.connector
import main
from dashboard import dashboard

class CariBuku():
    def CariBuku(self):
        global caribuku
        cal = CariBuku()
        caribuku = Tk()
        caribuku.title("Dashboard")
        caribuku.attributes("-fullscreen", True)
        caribuku.configure(bg = "light cyan")
        Label(caribuku, text = "Cari Buku", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(caribuku, text = "", bg = "light cyan").pack() #Space
        test = ttk.Button(text = "test").pack()
        Button(caribuku, text = "Back", height = "2", width = "30", command = cal.Logout).pack()
        caribuku.mainloop()
    def Logout(self):
        back = Tk()
        back.withdraw()
        ask = tkinter.messagebox.askokcancel(title = "Back", message = "Apakah anda yakin untuk kembali?")
        if (ask == 1):
            caribuku.destroy()
            get = dashboard.Dashboard
            get.Dashboard(self)
        else:
            back.destroy()
