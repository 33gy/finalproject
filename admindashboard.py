from tkinter import *
import main

class AdminDashboard():
    def AdminDashboard(self):
        global admindashboard
        cal = AdminDashboard()
        admindashboard = Tk()
        admindashboard.title("Admin Dashboard")
        admindashboard.attributes("-fullscreen", True)
        admindashboard.configure(bg = "light cyan")
        Label(admindashboard, text = "Admin Dashboard", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(admindashboard, text = "", bg = "light cyan").pack() #Space
        Button(admindashboard, text = "Log out", height = "2", width = "30", command = cal.Logout).pack()
    def Logout(self):
        admindashboard.destroy()
        get = main.MainWindow()
        get.Main()
        