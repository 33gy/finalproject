from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import mysql.connector
import main
from dashboard import admindashboard

global mydb
global curr

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="buku"
)
curr=mydb.cursor()


class PendaftaranBuku():
    def PendaftaranBuku(self):
        global pendaftaranbuku
        global nama_buku_entry
        global penulis_buku_entry
        global penerbit_buku_entry
        cal = PendaftaranBuku()
        pendaftaranbuku = Tk()
        pendaftaranbuku.title("Pendaftaran Buku")
        pendaftaranbuku.attributes("-fullscreen", True)
        pendaftaranbuku.configure(bg = "light cyan")
        screen_width = pendaftaranbuku.winfo_screenwidth() # get screen width 
        screen_height = pendaftaranbuku.winfo_screenheight() # get screen height
        top = Label(text = "Pendaftaran Buku", bg = "spring green", font = ("Calibri", 30, "bold")) # header
        top.place(x = 0, y = 0, width = screen_width, height = screen_height/12) # header placement
        nama_buku = Label(pendaftaranbuku, text = "Nama buku : ", bg = "light cyan", font = ("Calibri", 20))
        nama_buku.place(x = screen_width/2.18, y = screen_height/11)
        nama_buku_entry = ttk.Entry(pendaftaranbuku)
        nama_buku_entry.place(x = screen_width/2.28, y = screen_height/7.5, width = 230, height = 30)
        penulis_buku = Label(pendaftaranbuku, text = "Penulis buku : ", bg = "light cyan", font = ("Calibri", 20))
        penulis_buku.place(x = screen_width/2.19, y = screen_height/6)
        penulis_buku_entry = ttk.Entry(pendaftaranbuku)
        penulis_buku_entry.place(x = screen_width/2.28, y = screen_height/4.8, width = 230, height = 30)
        penerbit_buku = Label(pendaftaranbuku, text = "Penerbit : ",  bg = "light cyan", font = ("Calibri", 20))
        penerbit_buku.place(x = screen_width/2.13, y = screen_height/4.2)
        penerbit_buku_entry = ttk.Entry(pendaftaranbuku)
        penerbit_buku_entry.place(x = screen_width/2.28, y = screen_height/3.6, width = 230, height = 30)
        back_btn = ttk.Button(pendaftaranbuku, text = "Back", command = cal.InsertBuku)
        back_btn.place(x = screen_width/2.28, y = screen_height-100, width=230, height=50)
        #caribuku.mainloop()
    def Back(self):
        #back = Tk()
        #back.withdraw()
        #ask = tkinter.messagebox.askokcancel(title = "Back", message = "Apakah anda yakin untuk kembali?")
        #if (ask == 1):
            pendaftaranbuku.destroy()
            get = admindashboard.AdminDashboard
            get.AdminDashboard(self)
        #else:
            #back.destroy()
    def NoInput(self):
        noinput = Tk()
        noinput.withdraw()
        tkinter.messagebox.showinfo(title="Error", message="Masukan Username dan Password")
        noinput.destroy()
    def InsertBuku(self):
        nama = nama_buku_entry.get()
        penulis = penulis_buku_entry.get()
        penerbit = penerbit_buku_entry.get()
        cal = PendaftaranBuku()
        
        if (nama == "" or penulis == "" or penerbit == ""):
            cal.NoInput()
        else:
                curr.execute("INSERT into daftar_buku(namabuku, penulisbuku, penerbitbuku) values (%s, %s, %s)", (nama, penulis, penerbit))
                mydb.commit()
                print("ssss")