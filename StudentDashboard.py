import tkinter as tk
from tkinter import Menu
from subprocess import call
from tkinter import messagebox as mBox


class stdsucApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("STUDENT PANEL")
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
        self.admMenu.add_command(label="List All Books", command=self.clickLstbks)
        self.menuBar.add_cascade(label="Books", menu=self.admMenu)
        self.revMenu = Menu(self.menuBar, tearoff=0)  # 6
        self.revMenu.add_command(label="Reserve Book", command=self.clickReserve)
        self.menuBar.add_cascade(label="Reserve", menu=self.revMenu)
        self.retMenu = Menu(self.menuBar, tearoff=0)
        self.retMenu.add_command(label="Borrow Book", command=self.clickBorrow)
        self.menuBar.add_cascade(label="Loan", menu=self.retMenu)
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

    def clickLstbks(self):
        call(["python", "Viewbook.py"])

    def clickBorrow(self):
        call(["python", "Borrowbook.py"])

    def clickReserve(self):
        call(["python", "Reservebook.py"])

    def clickhelp(self):
        call(["python", "Help.py"])

    def clickabout(self):
        call(["python", "About.py"])


if __name__ == "__main__":
    stdapp = stdsucApp()
    stdapp.mainloop()