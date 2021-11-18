import tkinter as tk
from tkinter import Menu
from subprocess import call
from tkinter import messagebox as mBox


class libsucApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LIBRARIAN PANEL")
        self.geometry("963x600+5+5")
        self.configure(bg="gray")
        self.resizable(0, 0)
        # ==========Add Menu==========
        self.menuBar = Menu(self)
        self.configure(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.exitt)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.admMenu = Menu(self.menuBar, tearoff=0)  # 6
        self.admMenu.add_command(label="Add Book", command=self.clickAdbknApp)
        self.admMenu.add_command(label="List All Books", command=self.clickLstbks)
        self.admMenu.add_command(label="List Borrowed Books", command=self.clickbr)
        self.admMenu.add_command(label="List Reserved Books", command=self.clickrev)
        self.menuBar.add_cascade(label="Books", menu=self.admMenu)
        self.libMenu = Menu(self.menuBar, tearoff=0)  # 6
        self.libMenu.add_command(label="Add Student", command=self.clickAdstd)
        self.menuBar.add_cascade(label="Student", menu=self.libMenu)
        self.retMenu = Menu(self.menuBar, tearoff=0)
        self.retMenu.add_command(label="Receive Book", command=self.clickretbks)
        self.menuBar.add_cascade(label="Receive", menu=self.retMenu)
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="Help", command=self.clickhelp)
        self.helpMenu.add_command(label="About", command=self.clickabout)
        self.menuBar.add_cascade(label="About", menu=self.helpMenu)

    # ==========Exit Function==========
    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Functions to call scripts==========
    def clickAdbknApp(self):
        call(["python", "Book.py"])

    def clickLstbks(self):
        call(["python", "Viewbook.py"])

    def clickLstbrbks(self):
        call(["python", "Viewbook.py"])

    def clickLstrevbks(self):
        call(["python", "Viewbook.py"])

    def clickAdstd(self):
        call(["python", "Addstudent.py"])

    def clickretbks(self):
        call(["python", "Receivebook.py"])

    def clickhelp(self):
        call(["python", "Help.py"])

    def clickabout(self):
        call(["python", "About.py"])

    def clickbr(self):
        call(["python", "Viewbrbook.py"])

    def clickrev(self):
        call(["python", "Viewrvbook.py"])


if __name__ == "__main__":
    libapp = libsucApp()
    libapp.mainloop()