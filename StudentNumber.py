import tkinter as tk
from tkinter import *
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db
from datetime import datetime


class AddmnApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("STUDENT NUMBER")
        self.geometry("688x400+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        # ====================Variables========================#
        admno = tk.StringVar
        adate = tk.IntVar
        d = datetime(1, 1, 1).now()
        # ============================================================Frames==========================================

        self.MFrame = LabelFrame(self, width=600, height=390, font=('arial', 15, 'bold'), \
                                     bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=10, pady=20)

        self.CFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='STUDENT NUMBER')
        self.CFrame.grid(row=1, column=0, padx=10)

        self.DFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='ADMISSION INFO')
        self.DFrame.grid(row=1, column=1, padx=10)

        self.EFrame = LabelFrame(self,width=500, height=100, font=('arial', 10, 'bold'), \
                                  bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels of CFrame====================================

        self.Ladmno = Label(self.CFrame, text='STUDENT Number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ladmno.grid(row=0, column=0, sticky=W, padx=20)
        self.Ldated = Label(self.CFrame, text='DATE:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ldated.grid(row=1, column=0, sticky=W, padx=20)

        # ========================================================Entries of CFrame==================================

        self.Txtadmno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=admno)
        self.Txtadmno.grid(row=0, column=1, padx=10, pady=5)
        self.Txtdated = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=adate)
        self.Txtdated.insert(tk.INSERT, d.strftime('%Y-%m-%d'))
        self.Txtdated.grid(row=1, column=1, padx=10, pady=5)
        # ========================================================Buttons of EFrame=============================
        self.btnSave = Button(self.EFrame, text='SAVE', font=('arial', 10, 'bold'), width=8, command=self.savdmin)
        self.btnSave.grid(row=0, column=0, padx=10, pady=10)
        self.btnReset = Button(self.EFrame, text='RESET', font=('arial', 10, 'bold'), width=8, command=self.allclear)
        self.btnReset.grid(row=0, column=1, padx=10, pady=10)
        self.btnDelete = Button(self.EFrame, text='DELETE', font=('arial', 10, 'bold'), width=8, command=self.deldmin)
        self.btnDelete.grid(row=0, column=2, padx=10, pady=10)
        self.btnSearch = Button(self.EFrame, text='SEARCH', font=('arial', 10, 'bold'), width=8, command=self.seadmin)
        self.btnSearch.grid(row=0, column=3, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=8, command=self.exitt)
        self.btnExit.grid(row=0, column=4, padx=10, pady=10)

        # ===============================================List Box and scrollbar==================================
        self.scrollbar = Scrollbar(self.DFrame)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.listbox = Listbox(self.DFrame, width=30, height=10, font=('arial', 10, 'bold'))
        self.listbox.grid(row=0, column=0)

    # ==========Exit Function==========
    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Clear Function===========
    def allclear(self):
        self.Txtadmno.delete(0, END)
        self.listbox.delete(0, 1)

    # ==========Function for save Student Number==========
    def savdmin(self):
        admno = self.Txtadmno.get()
        adate = self.Txtdated.get()
        if admno == "" or adate == "":
            mBox.showerror(self, 'Error Enter adm no')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from admissionnumber where admno=%s", admno)
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "Student number. already registered")
                else:
                    cursor.execute("Insert into admissionnumber( admno,dated)""values(%s,%s)", (admno, adate))
                    conn.commit()
                    if cursor:
                        mBox.showinfo("Done", "Student no. Inserted Successfully")
                        ask = mBox.askyesno("Confirm", "Do you want to add another Number?")
                        if ask:
                            self.allclear()
                        else:
                            self.allclear()
                    else:
                        mBox.showerror("Error", "Unable to Save")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Function to Delete Student Number==========
    def deldmin(self):
        admno = self.Txtadmno.get()
        adate = self.Txtdated.get()
        if admno == "" or adate == "":
            mBox.showerror(self, 'Error Enter student no')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM admissionnumber where admno=%s", admno)
                conn.commit()
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "deleted Successfully")
                    ask = mBox.askyesno("Confirm", "Do you want to delete another Student no.?")
                    if ask:
                        self.allclear()
                else:
                    mBox.showinfo("Error", "wrong student number unable to delete")
                    self.clearall()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Function to Search Student number==========
    def seadmin(self):
        admno = self.Txtadmno.get()
        adate = self.Txtdated.get()
        if admno == "":
            mBox.showerror(self, 'Error Enter Student number')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from admissionnumber where admno=%s", admno)
                rowcount = cursor.fetchall()
                for row in rowcount:
                    self.listbox.insert(1, "Student Number. :" + str(row[0]))
                    self.listbox.insert(2, "Date Registered :" + str(row[1]))
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "record found")
                    ask = mBox.askyesno("Confirm", "Do you want to search another Student no.?")
                    if ask:
                        self.allclear()
                else:
                    mBox.showinfo("Error", "Unable to search")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")


if __name__ == "__main__":
    adnapp = AddmnApp()
    adnapp.mainloop()