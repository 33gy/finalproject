from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
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
        global lokasi_buku_entry
        global canvas
        global screen_height, screen_width
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
        lokasi_buku = Label(pendaftaranbuku, text = "Lokasi Buku : ",  bg = "light cyan", font = ("Calibri", 20))
        lokasi_buku.place(x = screen_width/2.18, y = screen_height/3.2)
        lokasi_buku_entry = ttk.Entry(pendaftaranbuku)
        lokasi_buku_entry.place(x = screen_width/2.28, y = screen_height/2.8, width = 230, height = 30)
        canvas = Canvas(pendaftaranbuku, width = 300, height = 400)
        canvas.place(x = screen_width/7, y = screen_height/11)
        insert_img = ttk.Button(pendaftaranbuku, text = "Insert Image", command = cal.InsertImage)
        insert_img.place(x = screen_width/2.28, y = screen_height/2.5, width=230, height=50)
        insert_btn = ttk.Button(pendaftaranbuku, text = "Insert", command = cal.InsertBuku)
        insert_btn.place(x = screen_width/2.28, y = screen_height/2.2, width=230, height=50)
        back_btn = ttk.Button(pendaftaranbuku, text = "Back", command = cal.Back)
        back_btn.place(x = screen_width/2.28, y = screen_height-100, width=230, height=50)
    def Back(self):
        pendaftaranbuku.destroy()
        get = admindashboard.AdminDashboard
        get.AdminDashboard(self)
    def NoInput(self):
        noinput = Tk()
        noinput.withdraw()
        tkinter.messagebox.showinfo(title="Error", message="Masukan Tidak Lengkap")
        noinput.destroy()
    def InsertBuku(self):
        nama = nama_buku_entry.get()
        penulis = penulis_buku_entry.get()
        penerbit = penerbit_buku_entry.get()
        lokasi = lokasi_buku_entry.get()
        cal = PendaftaranBuku()
        
        if (nama == "" or penulis == "" or penerbit == ""):
            cal.NoInput()
        else:
            curr.execute("INSERT into daftar_buku(namabuku, penulisbuku, penerbitbuku, lokasi) values (%s, %s, %s, %s)", (nama, penulis, penerbit, lokasi))
            mydb.commit()
            cal.SuccessInsert()
    def InsertImage(self):
        img = filedialog.askopenfilename(title = "Select A File", filetypes=(("png files", "*.png"),("jpg files","*.jpg")))
        openimg = Image.open(img).resize((300, 400), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(openimg)
        #im = PhotoImage(file = img, height = 400, width = 300)
        mylabel = Label(pendaftaranbuku, image = im)
        mylabel.image = im
        mylabel.place(x = screen_width/7, y = screen_height/11, width = 300, height = 400)
        
    def SuccessInsert(self):
        success = Tk()
        success.withdraw()
        tkinter.messagebox.showinfo(title="success", message="success mendaftarkan buku")
        success.destroy()
        nama_buku_entry.delete(0, 'end')
        penulis_buku_entry.delete(0, 'end')
        penerbit_buku_entry.delete(0, 'end')
        lokasi_buku_entry.delete(0, 'end')