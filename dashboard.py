from tkinter import *


class Dashboard():
    def Dashboard(self):
        dashboard = Tk()
        dashboard.title("Dashboard")
        dashboard.attributes("-fullscreen", True)
        dashboard.configure(bg = "light cyan")
        Label(dashboard, text = "Dashboard", bg = "spring green", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()
        Label(dashboard, text = "", bg = "light cyan").pack() #Space
        Button(dashboard, text = "Log out", height = "2", width = "30", command = dashboard.destroy).pack()