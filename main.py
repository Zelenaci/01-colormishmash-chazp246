from os.path import basename, splitext
import tkinter as tk
from tkinter.constants import HORIZONTAL

# from tkinter import ttk what???


class Appka(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Udělátko"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)
        
        self.lblR = tk.Label(self, text="R")
        self.lblR.pack()
        self.scaleR = tk.Scale(from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command=self.change)
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = tk.Scale(from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command=self.change)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB= tk.Scale(from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command=self.change)
        self.scaleB.pack()
        
        self.canvasmain = tk.Canvas(width=255, height=255, background="#000000")
        self.canvasmain.pack()
        
        """
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        
        self.btn2 = tk.Button(self, text="About2", command=self.quit)
        self.btn2.pack()

        self.btn3 = tk.Button(self, text="About3", command=self.quit)
        self.btn3.pack()
        """

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasmain.config(background=f"#{r:02x}{g:02x}{b:02x}")

    def quit(self, event=None):
        super().quit()


app = Appka()
app.mainloop()
