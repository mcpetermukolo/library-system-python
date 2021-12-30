import tkinter as tk
from tkinter import *
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db


class AdlibApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ADD LIBRARIAN.")
        self.geometry("690x400+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        # ====================Variables========================#
        staffno = tk.StringVar
        fname = tk.StringVar
        sname = tk.StringVar
        phoneno = tk.StringVar
        upass = tk.StringVar
        cupass = tk.StringVar

        # ============================================================Frames=====================================================================

        self.MFrame = LabelFrame(self, width=600, height=450, font=('arial', 15, 'bold'), \
                                     bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=10, pady=20)

        self.CFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='ADD LIBRARIAN')
        self.CFrame.grid(row=1, column=0, padx=10)

        self.DFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='LIBRARIAN INFO')
        self.DFrame.grid(row=1, column=1, padx=10)

        self.EFrame = LabelFrame(self,width=500, height=100, font=('arial', 10, 'bold'), \
                                  bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels of CFrame========================================================
        self.Lstafno = Label(self.CFrame, text='Staff Number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lstafno.grid(row=0, column=0, sticky=W, padx=20, pady=10)
        self.Lfname = Label(self.CFrame, text='First Name:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lfname.grid(row=1, column=0, sticky=W, padx=20)
        self.Lsname = Label(self.CFrame, text='Sur Name:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lsname.grid(row=2, column=0, sticky=W, padx=20)
        self.Lphoneno = Label(self.CFrame, text='Phone Number:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lphoneno.grid(row=3, column=0, sticky=W, padx=20)
        self.Lupass = Label(self.CFrame, text='Password:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lupass.grid(row=4, column=0, sticky=W, padx=20)
        self.Lcupass = Label(self.CFrame, text='Confirm Password:', font=('arial', 10, 'bold'), bg='lightblue')
        self.Lcupass.grid(row=5, column=0, sticky=W, padx=20)

        # ========================================================Entries of CFrame========================================================
        self.Txtstafno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=staffno)
        self.Txtstafno.grid(row=0, column=1, padx=10, pady=5)
        self.Txtfname = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=fname)
        self.Txtfname.grid(row=1, column=1, padx=10, pady=5)
        self.Txtsname = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=sname)
        self.Txtsname.grid(row=2, column=1, padx=10, pady=5)
        self.Txtphoneno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=phoneno)
        self.Txtphoneno.grid(row=3, column=1, padx=10, pady=5)
        self.Txtupass = Entry(self.CFrame, font=('arial', 10, 'bold'), show="*", textvariable=upass)
        self.Txtupass.grid(row=4, column=1, padx=10, pady=5)
        self.Txtcupass = Entry(self.CFrame, font=('arial', 10, 'bold'), show="*", textvariable=cupass)
        self.Txtcupass.grid(row=5, column=1, padx=10, pady=5)

        # ========================================================Buttons of self.EFrame=========================================================
        self.btnSave = Button(self.EFrame, text='SAVE', font=('arial', 10, 'bold'), width=8, command=self.savlib)
        self.btnSave.grid(row=0, column=0, padx=10, pady=10)
        self.btnReset = Button(self.EFrame, text='RESET', font=('arial', 10, 'bold'), width=8, command=self.allclear)
        self.btnReset.grid(row=0, column=1, padx=10, pady=10)
        self.btnUpdate = Button(self.EFrame, text='UPDATE', font=('arial', 10, 'bold'), width=8, command=self.updlib)
        self.btnUpdate.grid(row=0, column=2, padx=10, pady=10)
        self.btnDelete = Button(self.EFrame, text='DELETE', font=('arial', 10, 'bold'), width=8, command=self.dellib)
        self.btnDelete.grid(row=0, column=3, padx=10, pady=10)
        self.btnSearch = Button(self.EFrame, text='SEARCH', font=('arial', 10, 'bold'), width=8, command=self.searchlib)
        self.btnSearch.grid(row=0, column=4, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=8, command=self.exitt)
        self.btnExit.grid(row=0, column=5, padx=10, pady=10)

        # ===============================================List Box and self.scrollbar========================================================
        self.scrollbar = Scrollbar(self.DFrame)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.listbox = Listbox(self.DFrame, width=30, height=10, font=('arial', 10, 'bold'))
        self.listbox.grid(row=0, column=0)


    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()


    def clear(self):
        self.Txtstafno.config(state=NORMAL)
        self.Txtstafno.delete(0, END)
        self.Txtfname.delete(0, END)
        self.Txtsname.delete(0, END)
        self.Txtphoneno.delete(0, END)
        self.Txtupass.delete(0, END)
        self.Txtcupass.delete(0, END)


    def allclear(self):
        self.Txtstafno.delete(0, END)
        self.Txtfname.delete(0, END)
        self.Txtsname.delete(0, END)
        self.Txtphoneno.delete(0, END)
        self.Txtupass.delete(0, END)
        self.Txtcupass.delete(0, END)
        self.listbox.delete(0,4)



    def savlib(self):
        staffno = self.Txtstafno.get()
        fname = self.Txtfname.get()
        sname = self.Txtsname.get()
        phoneno = self.Txtphoneno.get()
        upass = self.Txtupass.get()
        cupass = self.Txtcupass.get()
        if staffno == "" or fname == "" or sname == "" or phoneno == "" or upass == "" or cupass == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        elif upass != cupass:
            mBox.showerror(self, 'Passwords do not match')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from librarian where staffno=%s", staffno)
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "staff no. already registered")
                else:
                    cursor.execute("Insert into librarian( staffno,fname,sname,phoneno,upass,cupass)"
                                   "values(%s,%s,%s,%s,%s,%s)", (staffno, fname, sname, phoneno, upass, cupass))
                    conn.commit()
                    if cursor:
                        mBox.showinfo("Done", "Librarian Inserted Successfully")
                        ask = mBox.askyesno("Confirm", "Do you want to add another Librarian?")
                        if ask:
                            self.clear()
                        else:
                            self.clear()
                    else:
                        mBox.showerror("Error", "Unable to save")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")


    def dellib(self):
        staffno = self.Txtstafno.get()
        if staffno == "":
            mBox.showerror(self, 'Enter staff number')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM librarian where staffno=%s", (staffno))
                conn.commit()
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "deleted Successfully")
                    ask = mBox.askyesno("Confirm", "Do you want to delete another record?")
                    if ask:
                        self.clear()
                else:
                    mBox.showinfo("Error", "Unable to Delete")
                    self.clear()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")


    def updlib(self):
        staffno = self.Txtstafno.get()
        fname = self.Txtfname.get()
        sname = self.Txtsname.get()
        phoneno = self.Txtphoneno.get()
        upass = self.Txtupass.get()
        cupass = self.Txtcupass.get()
        if staffno == "" or fname == "" or sname == "" or phoneno == "" or upass == "" or cupass == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        elif upass != cupass:
            mBox.showerror(self, 'Passwords do not match')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("Update librarian set fname =%s,sname =%s,phoneno =%s,upass =%s,cupass =%s where staffno=%s", (fname, sname, phoneno, upass, cupass,staffno))
                conn.commit()
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo("Done", "Librarian Updated Successfully")
                    ask = mBox.askyesno("Confirm", "Do you want to Update another record?")
                    if ask:
                        self.clear()
                    else:
                          self.clear()
                else:
                    mBox.showerror("Error", "Unable to update wrong staff number")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")


    def searchlib(self):
        staffno = self.Txtstafno.get()
        if staffno == "":
            mBox.showerror(self, 'Error Enter staffno', )
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from librarian where staffno=%s", (staffno))
                rowcount = cursor.fetchall()
                for row in rowcount:
                    self.listbox.insert(1, "STAFF NO. :" + str(row[0]))
                    self.listbox.insert(2, "FIRST NAME :" + str(row[1]))
                    self.listbox.insert(3, "SUR NAME :" + str(row[2]))
                    self.listbox.insert(4, "PHONE NO. :" + str(row[3]))
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "record found")
                    ask = mBox.askyesno("Confirm", "Do you want to search another record?")
                    if ask:
                        self.clear()
                else:
                    mBox.showinfo("Error", "Unable to search")
                    self.clear()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")


if __name__ == "__main__":
    adlapp = AdlibApp()
    adlapp.mainloop()