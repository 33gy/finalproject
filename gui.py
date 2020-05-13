from tkinter import *
from tkinter import ttk
 
class MainWindow():
    def Main(self):
        root = Tk()
        root.title('LibrarySystem')
        #root.geometry('600x600')
        label1  = Label(root, text = 'Username').grid(row = 0, column = 0)
        form1   = Entry(root).grid(row = 0, column = 1)
        label2  = Label(root, text = 'Password').grid(row = 1, column = 0)
        form2   = Entry(root).grid(row = 1, column = 1)
        button  = ttk.Button(root, text = 'Login', width = 20).grid(row = 2, column = 1)
        root.mainloop()
        
if __name__ == "__main__":
    cal = MainWindow()
    cal.Main()