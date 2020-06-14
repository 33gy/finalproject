from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import mysql.connector
import main
from dashboard import dashboard

global mydb
global curr

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="buku"
)
curr=mydb.cursor()


class CariBuku():
    def CariBuku(self):
        global caribuku
        global tabel1
        global search_entry
        cal = CariBuku()
        caribuku = Tk()
        caribuku.title("Dashboard")
        caribuku.attributes("-fullscreen", True)
        caribuku.configure(bg = "light cyan")
        screen_width = caribuku.winfo_screenwidth() # get screen width 
        screen_height = caribuku.winfo_screenheight() # get screen height
        top = Label(text = "Dashboard", bg = "spring green", font = ("Calibri", 30, "bold")) # header
        top.place(x = 0, y = 0, width = screen_width, height = screen_height/12) # header placement
        tabel1 = ttk.Treeview(caribuku, show = "headings")
        tabel1["column"]=("id", "nama buku","penulis buku", "penerbit buku")
        tabel1.heading("id", text = "ID")
        tabel1.heading("nama buku", text = "Nama Buku")
        tabel1.heading("penulis buku", text = "Penulis Buku")
        tabel1.heading("penerbit buku", text = "Penerbit Buku")
        tabel1.column("id", width = 20, stretch = NO)
        tabel1.place(x = screen_width/2.95, y = screen_height/8)
        search_label = Label(caribuku, text = "Search",  bg = "light cyan", font = ("Calibri", 20))
        search_label.place(x = screen_width/2.10, y = screen_height/2.97)
        search_entry = ttk.Entry(caribuku)
        search_entry.place(x = screen_width/2.28, y = screen_height/2.7, width = 230, height = 30)
        search_btn = ttk.Button(caribuku, text = "search", command= cal.searchbuku)
        search_btn.place(x = screen_width/2.28, y = screen_height/2.40, width=230, height=50)
        get_btn = ttk.Button(caribuku, text = "Show All Book", command = cal.data)
        get_btn.place(x = screen_width/2.28, y = screen_height/2.12, width=230, height=50)
        clear_btn = ttk.Button(caribuku, text = "clear", command = cal.clear)
        clear_btn.place(x = screen_width/4, y = screen_height-250, width=230, height=50)
        logout_btn = ttk.Button(caribuku, text = "Back", command = cal.Logout)
        logout_btn.place(x = screen_width/2.28, y = screen_height-100, width=230, height=50)
        #caribuku.mainloop()
    def Logout(self):
        #back = Tk()
        #back.withdraw()
        #ask = tkinter.messagebox.askokcancel(title = "Back", message = "Apakah anda yakin untuk kembali?")
        #if (ask == 1):
            #mydb.commit()
            caribuku.destroy()
            get = dashboard.Dashboard
            get.Dashboard(self)
        #else:
            #back.destroy()
    def data(self):
        for i in tabel1.get_children():
           tabel1.delete(i)
        curr.execute("SELECT * FROM daftar_buku")
        a = curr.fetchall()
        i = 0
        for row in a:
            tabel1.insert("","end", text=str(i), values=(row[0], row[1], row[2], row[3]))
            i +=1
        mydb.commit()
    def clear(self):
        for i in tabel1.get_children():
           tabel1.delete(i)
    def searchbuku(self):
        get = search_entry.get()
        for i in tabel1.get_children():
           tabel1.delete(i)
        curr.execute("SELECT * FROM daftar_buku WHERE namabuku = %s or penulisbuku = %s or penerbitbuku = %s",(get,get,get))
        a = curr.fetchall()
        i = 0
        for row in a:
            tabel1.insert("","end", text=str(i), values=(row[0], row[1], row[2], row[3]))
            i += 1
        mydb.commit()