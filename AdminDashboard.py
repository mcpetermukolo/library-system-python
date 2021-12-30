import tkinter as tk
from tkinter import Menu
from subprocess import call


class AdsucApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ADMIN PANEL")
        self.geometry("963x600+5+5")
        self.configure(bg="gray")
        self.resizable(0, 0)
        self.menuBar = Menu(self)
        self.configure(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.exitt)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.admMenu = Menu(self.menuBar, tearoff=0)  # 6
        self.admMenu.add_command(label="Add ADM NO.", command=self.clickAddmnApp)
        self.menuBar.add_cascade(label="Student", menu=self.admMenu)
        self.libMenu = Menu(self.menuBar, tearoff=0)  # 6
        self.libMenu.add_command(label="Add Librarian", command=self.clickLibApp)
        self.menuBar.add_cascade(label="Librarian", menu=self.libMenu)
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="Help", command=self.clickhelp)
        self.helpMenu.add_command(label="About", command=self.clickabout)
        self.menuBar.add_cascade(label="About", menu=self.helpMenu)

    def exitt(self):
        self.destroy()

    def clickAddmnApp(self):
        call(["python", "StudentNumber.py"])

    def clickLibApp(self):
        call(["python", "Librarian.py"])

    def clickhelp(self):
        call(["python", "Help.py"])

    def clickabout(self):
        call(["python", "About.py"])


if __name__ == "__main__":
   adapp = AdsucApp()
   adapp.mainloop()
