import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db


class VwbksApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VIEW RESERVED BOOKS.")
        self.geometry("508x430+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)

        # ============================================================Frames============================================

        self.MFrame = LabelFrame(self, width=350, height=350, font=('arial', 15, 'bold'), \
                                     bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=10, pady=20)

        self.DFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='RESERVED BOOKS')
        self.DFrame.grid(row=1, column=0, padx=10)

        self.EFrame = LabelFrame(self,width=300, height=100, font=('arial', 10, 'bold'), \
                                  bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Buttons of EFrame=====================================

        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=9,
                             command=self.exitt)
        self.btnExit.grid(row=0, column=1, padx=10, pady=10)
        # ===============================================Treeview and scrollbar=========================================
        self.scrollbary = Scrollbar(self.DFrame, orient=VERTICAL)
        self.scrollbarx = Scrollbar(self.DFrame, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.DFrame, columns=("ISBN NO", "STUDENT NO", "DATE"), selectmode="extended",  height=10,
                            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('ISBN NO', text="ISBN NO", anchor=W)
        self.tree.heading('STUDENT NO', text="STUDENT NO", anchor=W)
        self.tree.heading('DATE', text="DATE RESERVED", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.pack()
        try:
            self.tree.delete(*self.tree.get_children())
            conn = pymysql.connect(**Db.dbConfig)
            cursor = conn.cursor()
            cursor.execute("select * from reservebook")
            rowcount = cursor.fetchall()
            for row in rowcount:
                self.tree.insert('', 'end', values=(row[0], row[1], row[2]))
            cursor.close()
            conn.close()
        except Exception as es:
                 print('Error', f"due to :{str(es)}")

    # ==========Exit Function==========

    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()


if __name__ == "__main__":
    vbksapp = VwbksApp()
    vbksapp.mainloop()