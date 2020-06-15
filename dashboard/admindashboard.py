from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import main
from dashboard.admin_modul.pendaftaranbuku import PendaftaranBuku

class AdminDashboard():
    def AdminDashboard(self):
        global admindashboard
        cal = AdminDashboard()
        admindashboard = Tk()
        admindashboard.title("Admin Dashboard")
        admindashboard.attributes("-fullscreen", True)
        admindashboard.configure(bg = "light cyan")
        screen_width = admindashboard.winfo_screenwidth() # get screen width 
        screen_height = admindashboard.winfo_screenheight() # get screen height
        top = Label(text = "Admin Dashboard", bg = "spring green", font = ("Calibri", 30, "bold")) # header
        top.place(x = 0, y = 0, width = screen_width, height = screen_height/12) # header placement
        pendafataran_buku = ttk.Button(admindashboard, text = "Pendaftaran Buku", command = cal.PendaftaranBuku)
        pendafataran_buku.place(x = screen_width/25, y = screen_height/7, width = 150, height = 150)
        #peminjaman_admin = ttk.Button(admindashboard, text = "Peminjaman Admin")
        #peminjaman_admin.place(x = screen_width/7.5, y = screen_height/7, width = 150, height = 150)
        #peminjaman = ttk.Button(admindashboard, text = "??")
        #peminjaman.place(x = screen_width/4.41, y = screen_height/7, width = 150, height = 150)
        logout_btn = ttk.Button(admindashboard, text = "Log Out", command =   cal.Logout)
        logout_btn.place(x = screen_width/2.28, y = screen_height-100, width=230, height=50)
    def Logout(self):
        back = Tk()
        back.withdraw()
        ask = tkinter.messagebox.askokcancel(title = "Log Out", message = "Apakah anda yakin untuk keluar?")
        if (ask == 1):
            admindashboard.destroy()
            get = main.MainWindow()
            get.Main()
        else:
            back.destroy()
    def PendaftaranBuku(self):
        admindashboard.destroy()
        get = PendaftaranBuku()
        get.PendaftaranBuku()