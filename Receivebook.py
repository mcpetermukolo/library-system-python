import tkinter as tk
from tkinter import *
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db
from datetime import datetime, date


class RetnApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RECEIVE BOOK.")
        self.geometry("420x360+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        # ====================Variables========================#
        isbnno = tk.StringVar
        admno = tk.StringVar
        dated = tk.StringVar
        dated1 = tk.IntVar
        fine = tk.StringVar
        fineamnt = tk.IntVar
        d = datetime(1, 1, 1).now()
        # ============================================================Frames=====================================================================

        self.MFrame = LabelFrame(self, width=390, height=300, font=('arial', 15, 'bold'), \
                                     bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=10, pady=20)

        self.CFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='RECEIVE')
        self.CFrame.grid(row=1, column=0, padx=10)

        self.EFrame = LabelFrame(self,width=200, height=100, font=('arial', 10, 'bold'), \
                                  bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels of CFrame========================================================
        self.Lisbnno = Label(self.CFrame, text='ISBN Number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lisbnno.grid(row=0, column=0, sticky=W, padx=20, pady=10)
        self.Ladmno = Label(self.CFrame, text='STUDENT Number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ladmno.grid(row=1, column=0, sticky=W, padx=20)
        self.Ldatedb = Label(self.CFrame, text='DATE BORROWED:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ldatedb.grid(row=2, column=0, sticky=W, padx=20)
        self.Ldated = Label(self.CFrame, text='DATE:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ldated.grid(row=3, column=0, sticky=W, padx=20)
        self.Lfine = Label(self.CFrame, text='FINE:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lfine.grid(row=4, column=0, sticky=W, padx=20)



        # ========================================================Entries of CFrame========================================================
        self.Txtisbnno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=isbnno)
        self.Txtisbnno.grid(row=0, column=1, padx=10, pady=5)
        self.Txtadmno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=admno)
        self.Txtadmno.grid(row=1, column=1, padx=10, pady=5)
        self.Txtdatedb = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=dated1)
        self.Txtdatedb.grid(row=2, column=1, padx=10, pady=5)
        self.Txtdated = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=dated)
        self.Txtdated.insert(tk.INSERT, d.strftime('%Y-%m-%d'))
        self.Txtdated.grid(row=3, column=1, padx=10, pady=5)
        self.Txtfine = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=fine)
        self.Txtfine.grid(row=4, column=1, padx=10, pady=5)

        # ========================================================Buttons of self.EFrame=========================================================
        self.btnReturn = Button(self.EFrame, text='RECEIVE', font=('arial', 10, 'bold'), width=8, command=self.retnbks)
        self.btnReturn.grid(row=0, column=0, padx=10, pady=10)
        self.btnInfo = Button(self.EFrame, text='BOOK INFO', font=('arial', 10, 'bold'), width=9, command=self.searchst)
        self.btnInfo.grid(row=0, column=1, padx=10, pady=10)
        self.btnGetfine = Button(self.EFrame, text='FINE', font=('arial', 10, 'bold'), width=8, command=self.getfine)
        self.btnGetfine.grid(row=0, column=2, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=8, command=self.exitt)
        self.btnExit.grid(row=0, column=3, padx=10, pady=10)

    # ==========Exit Function==========
    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Clear Function==========
    def allclear(self):
        self.Txtisbnno.delete(0, END)
        self.Txtadmno.delete(0, END)
        self.Txtdatedb.delete(0, END)
        self.Txtfine.delete(0, END)

    # ==============Function To Check if borrowed Book with given ISBN Exist or Not==================

    def isbnbkck(self, isbnno):
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

    # ====================Function To Check if Admission number Exist or Not====================

    def admbkck(self, admno):
        try:
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("select * from borrowbook where admno=%s", admno)
            rowcount = cursor.rowcount
            if cursor.rowcount == 1:
                return True
            else:
                return False
                cursor.close()
                conn.close()
        except Exception as es:
            print('Error', f"due to :{str(es)}")

    # ======Function To Check if borrowed Book ISBN and Admission number match====================
    def admretnck(self, admno, isbnno):
        try:
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("select * from borrowbook where admno=%s and isbnno=%s", (admno, isbnno))
            rowcount = cursor.rowcount
            if cursor.rowcount == 1:
                return True
            else:
                return False
                cursor.close()
                conn.close()
        except Exception as es:
            print('Error', f"due to :{str(es)}")

    # ======Function To Delete ISBN from borrowbook Table After being Returned============
    def admretdel(self, isbnno):
        try:
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("delete  from borrowbook where isbnno=%s", isbnno)
            conn.commit()
            rowcount = cursor.rowcount
            if cursor.rowcount == 1:
                return rowcount
                cursor.close()
                conn.close()
        except Exception as es:
            print('Error', f"due to :{str(es)}")

    # ======Function To Get fine============
    def getfine(self):
        isbnno = self.Txtisbnno.get()
        admno = self.Txtadmno.get()
        dated = self.Txtdated.get()
        dated1 = self.Txtdatedb.get()
        if isbnno == "" or admno == "" or dated == "" or dated1 == "":
            mBox.showerror(self, 'Error, Enter ISBN then Click on BOOK INFO')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select dated from borrowbook where admno=%s and isbnno=%s", (admno, isbnno))
                rowcount = cursor.fetchone()
                for row in rowcount:
                    todayy = datetime.now()
                    bday = datetime.strptime(self.Txtdatedb.get(), '%Y-%m-%d')
                    days = (todayy - bday).days
                    fineamnt = 0,
                    if days < 5:
                        self.Txtfine.insert(tk.INSERT, fineamnt)
                        mBox.showinfo("fine is:", fineamnt)
                    else:
                        fineamnt = 5 * days
                        self.Txtfine.insert(tk.INSERT, fineamnt)
                        mBox.showinfo("fine is:", fineamnt)
                    cursor.close()
                    conn.close()
            except Exception as es:
                   print('Error', f"due to :{str(es)}")

    # ======Function To Get book Information============
    def searchst(self):
        isbnno = self.Txtisbnno.get()
        if isbnno == "":
            mBox.showerror(self, 'Error Enter ISBN number', )
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from borrowbook where isbnno=%s", isbnno)
                rowcount = cursor.fetchall()
                for row in rowcount:
                    self.Txtadmno.insert(tk.INSERT, str(row[1]))
                    self.Txtdatedb.insert(tk.INSERT, (row[2]))
                if cursor.rowcount == 1:
                    mBox.showinfo("Information", "record found")
                else:
                    mBox.showinfo("Error", "Unable to Search")
                    self.clear()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ======Function To  Receive Book============
    def retnbks(self):
        isbnno = self.Txtisbnno.get()
        admno = self.Txtadmno.get()
        dated = self.Txtdated.get()
        dated1 = self.Txtdatedb.get()
        fine = self.Txtfine.get()
        if isbnno == "" or admno == "" or dated == "" or dated1 == "" or fine == "":
            mBox.showerror(self, 'Error Enter ISBN NO,Then click on BOOK INFO ')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                if not RetnApp.isbnbkck(self, isbnno):
                    mBox.showinfo('Information', "Wrong ISBN Number.")
                    self.allclear()
                else:
                    if not RetnApp.admretnck(self, admno, isbnno):
                        mBox.showinfo('Information', "Student No and ISBN No dont match.")
                        self.allclear()
                    else:
                        cursor.execute("Insert into receive( isbnno,admno,dated,dated1,fine)""values(%s,%s,%s,%s,%s)",(isbnno, admno, dated, dated1, fine))
                        conn.commit()
                        RetnApp.admretdel(self, isbnno)
                        if cursor:
                            mBox.showinfo("Done", "received sucessfully")
                            ask = mBox.askyesno("Confirm", "Do you want to receive another book?")
                            if ask:
                                self.allclear()
                            else:
                                self.allclear()
                        else:
                            mBox.showerror("Error", "Unable to Receive book")
                            cursor.close()
                            conn.close()
            except Exception as es:
                    print('Error', f"due to :{str(es)}")


if __name__ == "__main__":
    rtnapp = RetnApp()
    rtnapp.mainloop()