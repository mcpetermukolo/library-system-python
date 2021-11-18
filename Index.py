import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db
from subprocess import call
from AdminDashboard import AdsucApp
from LibrarianDashboard import libsucApp
from StudentDashboard import stdsucApp

# ==========Splash window==========.
SplashApp = tk.Tk()
SplashApp.title("LIBRARY SYSTEM")
# ==========set center screen window==========
XLeft = (SplashApp.winfo_screenwidth() - 340) / 2
XTop = (SplashApp.winfo_screenheight() - 80) / 2
SplashApp.geometry("%dx%d+%d+%d" % (340, 80, XLeft, XTop))
SplashApp.resizable(0, 0)
SplashApp.configure(bg="gray")
WIDTH, HEIGHT = 326, 76

# ==========Add splash image on label==========.
img = ImageTk.PhotoImage(Image.open("images\splash.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
lbl = tk.Label(SplashApp, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

# ========================================================Login class===================================================


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LIBRARY SYSTEM")
        self.resizable(0, 0)
        self.configure(bg="gray")
        # ==========set center screen window==========
        SLeft = (self.winfo_screenwidth() - 418) / 2
        STop = (self.winfo_screenheight() - 380) / 2
        self.geometry("%dx%d+%d+%d" % (418, 380, SLeft, STop))

        # ====================Variables========================#
        desig = tk.StringVar()
        admuname = tk.StringVar()
        admupass = tk.StringVar()
        staffno = tk.IntVar()
        admno = tk.IntVar()
        upass = tk.StringVar()
        WIDTH, HEIGHT = 400, 360

        # ==========Adding a background image==========
        self.img = ImageTk.PhotoImage(Image.open("images\libp.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.lbl = tk.Label(self, image=self.img)
        self.lbl.img = self.img  # Keep a reference in case this code put is in a function.
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

        # ============================================================Frames============================================
        self.MFrame = LabelFrame(self, width=350, height=300, font=('arial', 15, 'bold'), bg='lightblue', bd=15,
                                     relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=40, pady=20)
        self.EFrame = LabelFrame(self, width=200, height=100, font=('arial', 10, 'bold'), bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        self.GFrame = LabelFrame(self, width=200, height=100, font=('arial', 10, 'bold'), bg='lightblue',
                                 relief='ridge', bd=13)
        self.GFrame.grid(row=3, column=0, pady=10)

        # ========================================================Labels================================================
        self.Lsyslogin = Label(self.MFrame, text='SYSTEM LOGIN:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lsyslogin.grid(row=1, column=0, sticky=W, padx=20)
        self.Lchoose = Label(self.MFrame, text='Choose:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lchoose.grid(row=2, column=0, sticky=W, padx=20)
        self.LUsername = Label(self.MFrame, text='Username:', font=('arial', 10, 'bold'), bg='lightblue')
        self.LUsername.grid(row=3, column=0, sticky=W, padx=20)
        self.Lupass = Label(self.MFrame, text='Password:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lupass.grid(row=4, column=0, sticky=W, padx=20)

        # ========================================================Entries of Frame======================================
        self.Txtdesig = Entry(self.MFrame, font=('arial', 10, 'bold'), textvariable=desig)
        self.Txtdesig.grid(row=3, column=1, padx=10, pady=5)
        self.desigChosen = ttk.Combobox(self.MFrame, font=('arial', 10, 'bold'), width=17, textvariable=desig,
                                        state='readonly')
        self.desigChosen['values'] = ("Admin", "Librarian", "Student")
        self.desigChosen.grid(row=2, column=1, padx=10, pady=5)
        self.desigChosen.current(0)
        self.TxtUsername = Entry(self.MFrame, font=('arial', 10, 'bold'), textvariable=admuname)
        self.TxtUsername.grid(row=3, column=1, padx=10, pady=5)
        self.Txtupass = Entry(self.MFrame, font=('arial', 10, 'bold'), show="*", textvariable=admupass)
        self.Txtupass.grid(row=4, column=1, padx=10, pady=5)

        # ========================================================Buttons of EFrame=====================================
        self.btnlogin = Button(self.EFrame, text='LOGIN', font=('arial', 10, 'bold'), width=9, command=self.logn)
        self.btnlogin.grid(row=0, column=0, padx=10, pady=10)
        self.btnReg = Button(self.EFrame, text='REGISTER', font=('arial', 10, 'bold'), width=9, command=self.clickStdApp)
        self.btnReg.grid(row=0, column=1, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=9, command=self.exitt)
        self.btnExit.grid(row=0, column=2, padx=10, pady=10)

        self.btnHelp = Button(self.GFrame, text='HELP', font=('arial', 10, 'bold'), width=9, command=self.clickhelp)
        self.btnHelp.grid(row=0, column=0, padx=10, pady=10)
        self.btnAbout = Button(self.GFrame, text='ABOUT', font=('arial', 10, 'bold'), width=9, command=self.clickabout)
        self.btnAbout.grid(row=0, column=1, padx=10, pady=10)

    # ========================================================functions=================================================
    # ==========Exit Function==========
    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Functions to call scripts==========

    def clickhelp(self):
        call(["python", "Help.py"])

    def clickabout(self):
        call(["python", "About.py"])

    def clickStdApp(self):
        call(["python", "Student.py"])

    # ==========Function for Combobox==========.

    def logn(self):
        dess = self.desigChosen.get()
        if dess == 'Admin':
            self.adlogn()
        elif dess == 'Librarian':
            self.liblogn()
        elif dess == 'Student':
            self.stdlogn()
        else:
            mBox.showerror(self, 'Please choose')

    # ==========Function for Admin login==========.

    def adlogn(self):
        admuname = self.TxtUsername.get()
        admupass = self.Txtupass.get()
        if admuname == "" or admupass == "":
            mBox.showerror(self, 'Error Enter username & password')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from admin where admuname=%s and admupass=%s", (admuname, admupass))
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "Login Successfully")
                    self.destroy()
                    AdsucApp()
                else:
                    mBox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
                cursor.close()
                conn.close()
            except Exception as es:
                print('Error', f"due to :{str(es)}")

    # ==========Function for Librarian login==========.

    def liblogn(self):
        staffno = self.TxtUsername.get()
        upass = self.Txtupass.get()
        if staffno == "" or upass == "":
            mBox.showerror(self, 'Error Enter username & password')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from librarian where staffno=%s and upass=%s", (staffno, upass))
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "Login Successfully")
                    self.destroy()
                    libsucApp()
                else:
                    mBox.showinfo('Information', "Login failed,Invalid Staffno. or Password.Try again!!!")
                cursor.close()
                conn.close()
            except Exception as es:
                print('Error', f"due to :{str(es)}")

    # ==========Function for Student login==========.

    def stdlogn(self):
        admno = self.TxtUsername.get()
        upass = self.Txtupass.get()
        if admno == "" or upass == "":
            mBox.showerror(self, 'Error Enter username & password')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from student where admno=%s and upass=%s", (admno, upass))
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "Login Successfully")
                    self.destroy()
                    stdsucApp()
                else:
                    mBox.showinfo('Information', "Login failed,Invalid Student.no. or Password.Try again!!!")
                cursor.close()
                conn.close()
            except Exception as es:
                print('Error', f"due to :{str(es)}")


# ==========Function for to call main window==========

def callmainroot():
    SplashApp.destroy()
    LoginApp()

# ==========Display splash window then main window==========


SplashApp.after(2000, callmainroot)

mainloop()

