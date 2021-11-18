import tkinter as tk
from tkinter import *
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db
from datetime import datetime



class ResvApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RESERVE BOOK.")
        self.geometry("387x300+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        # ====================Variables========================#
        isbnno = tk.StringVar
        admno = tk.StringVar
        dated = tk.StringVar
        d = datetime(1, 1, 1).now()
        # ============================================================Frames=====================================================================

        self.MFrame = LabelFrame(self, width=390, height=300, font=('arial', 15, 'bold'), \
                                     bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=10, pady=20)

        self.CFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='RESERVE')
        self.CFrame.grid(row=1, column=0, padx=10)

        self.EFrame = LabelFrame(self,width=200, height=100, font=('arial', 10, 'bold'), \
                                  bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels of CFrame========================================================
        self.Lisbnno = Label(self.CFrame, text='ISBN Number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lisbnno.grid(row=0, column=0, sticky=W, padx=20, pady=10)
        self.Ladmno = Label(self.CFrame, text='STUDENT Number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ladmno.grid(row=1, column=0, sticky=W, padx=20)
        self.Ldated = Label(self.CFrame, text='DATE:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ldated.grid(row=2, column=0, sticky=W, padx=20)




        # ========================================================Entries of CFrame========================================================
        self.Txtisbnno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=isbnno)
        self.Txtisbnno.grid(row=0, column=1, padx=10, pady=5)
        self.Txtadmno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=admno)
        self.Txtadmno.grid(row=1, column=1, padx=10, pady=5)
        self.Txtdated = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=dated)
        self.Txtdated.insert(tk.INSERT, d.strftime('%Y-%m-%d'))
        self.Txtdated.grid(row=2, column=1, padx=10, pady=5)
        # ========================================================Buttons of self.EFrame=========================================================
        self.btnSave = Button(self.EFrame, text='RESERVE', font=('arial', 10, 'bold'), width=8, command=self.resvbk)
        self.btnSave.grid(row=0, column=0, padx=10, pady=10)
        self.btnReset = Button(self.EFrame, text='RESET', font=('arial', 10, 'bold'), width=8, command=self.allclear)
        self.btnReset.grid(row=0, column=1, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=8, command=exit)
        self.btnExit.grid(row=0, column=2, padx=10, pady=10)

    # ========================================================Methods=========================================================
    # ==========Exit Function==========
    def exit(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Clear Function==========
    def allclear(self):
        self.Txtisbnno.delete(0, END)
        self.Txtadmno.delete(0, END)

    # ====================Function To Reserve Book===================
    def resvbk(self):
        isbnno = self.Txtisbnno.get()
        admno = self.Txtadmno.get()
        dated = self.Txtdated.get()

        if isbnno == "" or admno == "" or dated == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                if not ResvApp.isbnck(self, isbnno):
                    mBox.showinfo('Information', "Wrong ISBN Number")
                    self.allclear()
                else:
                    if not ResvApp.admck(self, admno):
                        mBox.showinfo('Information', "Not valid Student number.")
                        self.allclear()
                    else:
                        if ResvApp.isbrvck(self, isbnno):
                            mBox.showinfo('Information', "book already reserved.")
                            self.allclear()
                        else:
                            if ResvApp.isbrwck(self, isbnno):
                                mBox.showinfo('Information', "book already borrowed.")
                                self.allclear()
                            else:
                                cursor.execute("Insert into reservebook( isbnno,admno,dated)""values(%s,%s,%s)",(isbnno, admno, dated))
                                conn.commit()
                                if cursor:
                                    mBox.showinfo("Done", "reserved sucessfully")
                                    ask = mBox.askyesno("Confirm", "reserved another book?")
                                    if ask:
                                        self.allclear()
                                    else:
                                        self.allclear()
                                else:
                                    mBox.showerror("Error", "Unable to Reserve")

                                    cursor.close()
                                    conn.close()
            except Exception as es:
                print('Error', f"due to :{str(es)}")

    # ====================Function To Check if ISBN number Exist or Not====================
    def isbnck(self, isbnno):
        try:
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("select * from bookinfo where isbnno=%s", isbnno)
            rowcount = cursor.rowcount
            if cursor.rowcount == 1:
                return True
            else:
                return False
                cursor.close()
                conn.close()
        except Exception as es:
            print('Error', f"due to :{str(es)}")

    # ====================Function To Check if Student number Exist or Not====================
    def admck(self, admno):
        try:
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("select * from student where admno=%s", admno)
            rowcount = cursor.rowcount
            if cursor.rowcount == 1:
                return True
            else:
                return False
                cursor.close()
                conn.close()
        except Exception as es:
            print('Error', f"due to :{str(es)}")

    # ====================Function To Check if Book has been borrowed or Not====================
    def isbrwck(self, isbnno):
        try:
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("select * from borrowbook where isbnno=%s", isbnno)
            rowcount = cursor.rowcount
            if cursor.rowcount == 1:
                return True
            else:
                return False
                cursor.close()
                conn.close()
        except Exception as es:
            print('Error', f"due to :{str(es)}")

    # ====================Function To Check if Book  has been Reserved or Not===================
    def isbrvck(self, isbnno):
        try:
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("select * from reservebook where isbnno=%s", isbnno)
            rowcount = cursor.rowcount
            if cursor.rowcount == 1:
                return True
            else:
                return False
                cursor.close()
                conn.close()
        except Exception as es:
            print('Error', f"due to :{str(es)}")


if __name__ == "__main__":
    rsvapp = ResvApp()
    rsvapp.mainloop()