import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

class HelpApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HELP")
        self.geometry("670x360+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        WIDTH, HEIGHT = 630, 340

        # ============================================================Frames=====================================================================

        self.MFrame = LabelFrame(self, width=650, height=350, font=('arial', 15, 'bold'), bg='lightblue', bd=15,
                                 relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=5, pady=5)

        # Add image on a Label.
        self.img = ImageTk.PhotoImage(
            Image.open("images\help.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.lbl = tk.Label(self.MFrame, image=self.img)
        self.lbl.img = self.img
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.


if __name__ == "__main__":
    hepapp = HelpApp()
    hepapp.mainloop()