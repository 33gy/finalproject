from tkinter import *
import main

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
        test = Button(dashboard, text = "test", height = "7", width = "20")
        test.place(x = 20, y = 100)
        Label(dashboard, text = "", bg = "light cyan").pack() #Space
        Button(dashboard, text = "Log out", height = "2", width = "30", command = cal.Logout).pack()
        dashboard.mainloop()
    def Logout(self):
        dashboard.destroy()
        get = main.MainWindow()
        get.Main()
