import tkinter as tk
from tkinter import *
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db
from datetime import datetime


class AdbkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ADD BOOK.")
        self.geometry("700x400+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        # ====================Variables========================#
        isbnno = tk.StringVar
        subject = tk.StringVar
        author = tk.StringVar
        edno = tk.StringVar
        shelfno = tk.StringVar
        dated = tk.IntVar
        d = datetime(1, 1, 1).now()
        # ============================================================Frames============================================

        self.MFrame = LabelFrame(self, width=600, height=450, font=('arial', 15, 'bold'), \
                                     bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=10, pady=20)

        self.CFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='ADD NEW BOOK')
        self.CFrame.grid(row=1, column=0, padx=10)

        self.DFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='BOOK INFO')
        self.DFrame.grid(row=1, column=1, padx=10)

        self.EFrame = LabelFrame(self,width=500, height=100, font=('arial', 10, 'bold'), \
                                  bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels of CFrame======================================
        self.Lisbnno = Label(self.CFrame, text='ISBN number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lisbnno.grid(row=0, column=0, sticky=W, padx=20, pady=10)
        self.Lsubject = Label(self.CFrame, text='Subject:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lsubject.grid(row=1, column=0, sticky=W, padx=20)
        self.Lauthor = Label(self.CFrame, text='Author(s):', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lauthor.grid(row=2, column=0, sticky=W, padx=20)
        self.Ledno = Label(self.CFrame, text='Edition number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ledno.grid(row=3, column=0, sticky=W, padx=20)
        self.Lshelfno = Label(self.CFrame, text='Shelf No:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lshelfno.grid(row=4, column=0, sticky=W, padx=20)
        self.Ldated = Label(self.CFrame, text='DATE:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Ldated.grid(row=5, column=0, sticky=W, padx=20)

        # ========================================================Entries of CFrame=====================================
        self.Txtisbnno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=isbnno)
        self.Txtisbnno.grid(row=0, column=1, padx=10, pady=5)
        self.Txtsubject = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=subject)
        self.Txtsubject.grid(row=1, column=1, padx=10, pady=5)
        self.Txtauthor = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=author)
        self.Txtauthor.grid(row=2, column=1, padx=10, pady=5)
        self.Txtedno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=edno)
        self.Txtedno.grid(row=3, column=1, padx=10, pady=5)
        self.Txtshelfno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=shelfno)
        self.Txtshelfno.grid(row=4, column=1, padx=10, pady=5)
        self.Txtdated = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=dated)
        self.Txtdated.insert(tk.INSERT, d.strftime('%Y-%m-%d'))
        self.Txtdated.grid(row=5, column=1, padx=10, pady=5)

        # ========================================================Buttons of EFrame================================
        self.btnSave = Button(self.EFrame, text='SAVE', font=('arial', 10, 'bold'), width=8, command=self.savbk)
        self.btnSave.grid(row=0, column=0, padx=10, pady=10)
        self.btnReset = Button(self.EFrame, text='RESET', font=('arial', 10, 'bold'), width=8, command=self.allclear)
        self.btnReset.grid(row=0, column=1, padx=10, pady=10)
        self.btnUpdate = Button(self.EFrame, text='UPDATE', font=('arial', 10, 'bold'), width=8, command=self.upbk)
        self.btnUpdate.grid(row=0, column=2, padx=10, pady=10)
        self.btnDelete = Button(self.EFrame, text='DELETE', font=('arial', 10, 'bold'), width=8, command=self.delbk)
        self.btnDelete.grid(row=0, column=3, padx=10, pady=10)
        self.btnSearch = Button(self.EFrame, text='SEARCH', font=('arial', 10, 'bold'), width=8, command=self.searchbk)
        self.btnSearch.grid(row=0, column=4, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=8, command=self.exitt)
        self.btnExit.grid(row=0, column=5, padx=10, pady=10)

        # ===============================================List Box and scrollbar====================================
        self.scrollbar = Scrollbar(self.DFrame)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.listbox = Listbox(self.DFrame, width=30, height=10, font=('arial', 10, 'bold'))
        self.listbox.grid(row=0, column=0)

    # ==========Exit Function==========
    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Clear Function==========
    def allclear(self):
        self.Txtisbnno.delete(0, END)
        self.Txtsubject.delete(0, END)
        self.Txtauthor.delete(0, END)
        self.Txtedno.delete(0, END)
        self.Txtshelfno.delete(0, END)
        self.listbox.delete(0, 5)

    # ==========Save Book Function==========
    def savbk(self):
        isbnno = self.Txtisbnno.get()
        subject = self.Txtsubject.get()
        author = self.Txtauthor.get()
        edno = self.Txtedno.get()
        shelfno = self.Txtshelfno.get()
        dated = self.Txtdated.get()
        if isbnno == "" or subject == "" or author == "" or edno == "" or shelfno == "" or dated == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from bookinfo where isbnno=%s", isbnno)
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "isbnno. already registered")
                else:
                    cursor.execute("Insert into bookinfo( isbnno,subject,author,edno,shelfno,dated)"
                                   "values(%s,%s,%s,%s,%s,%s)", (isbnno, subject, author, edno, shelfno, dated))
                    conn.commit()
                    if cursor:
                        mBox.showinfo("Done", "book Inserted Successfully")
                        ask = mBox.askyesno("Confirm", "Do you want to add another book?")
                        if ask:
                            self.allclear()
                        else:
                            self.allclear()
                    else:
                        mBox.showerror("Error", "Unable to Add book")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Delete Book Function==========
    def delbk(self):
        isbnno = self.Txtisbnno.get()
        if isbnno == "":
            mBox.showerror(self, 'Enter isbn number')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM bookinfo where isbnno=%s", isbnno)
                conn.commit()
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "deleted Successfully")
                    ask = mBox.askyesno("Confirm", "Do you want to delete another Book?")
                    if ask:
                        self.allclear()
                    else:
                        self.allclear()
                else:
                    mBox.showinfo("Error", "Unable to Delete")
                    self.clear()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Update Book Function==========
    def upbk(self):
        isbnno = self.Txtisbnno.get()
        subject = self.Txtsubject.get()
        author = self.Txtauthor.get()
        edno = self.Txtedno.get()
        shelfno = self.Txtshelfno.get()
        dated = self.Txtdated.get()
        if isbnno == "" or subject == "" or author == "" or edno == "" or shelfno == "" or dated == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("Update bookinfo set subject =%s,author =%s,edno =%s,shelfno =%s,dated =%s where "
                               "isbnno=%s", (subject, author, edno, shelfno, dated,isbnno))
                conn.commit()
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo("Done", "Book Updated Successfully")
                    ask = mBox.askyesno("Confirm", "Do you want to Update another record?")
                    if ask:
                        self.allclear()
                    else:
                        self.allclear()
                else:
                    mBox.showerror("Error", "Unable to update wrong ISBN number")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Search Book Function==========
    def searchbk(self):
        isbnno = self.Txtisbnno.get()
        if isbnno == "":
            mBox.showerror(self, 'Error Enter isbn number', )
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from bookinfo where isbnno=%s", isbnno)
                rowcount = cursor.fetchall()
                for row in rowcount:
                    self.listbox.insert(1, "ISBN number. :" + str(row[0]))
                    self.listbox.insert(2, "Subject :" + str(row[1]))
                    self.listbox.insert(3, "Author(s) :" + str(row[2]))
                    self.listbox.insert(4, "Edition number. :" + str(row[3]))
                    self.listbox.insert(3, "Shelf No :" + str(row[4]))
                    self.listbox.insert(4, "Date. :" + str(row[5]))
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "record found")
                    ask = mBox.askyesno("Confirm", "Do you want to search another record?")
                    if ask:
                        self.allclear()
                else:
                    mBox.showinfo("Error", "Unable to Search")
                    self.clear()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")


if __name__ == "__main__":
    adkapp = AdbkApp()
    adkapp.mainloop()