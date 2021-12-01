from os.path import basename, splitext
import tkinter as tk
import random

class Appka(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Udělátko"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)
        self.bind("<r>", self.random)
        
        self.lblR = tk.Label(self, text="R",fg = "#000000")
        self.lblR.pack()
        self.scaleR = tk.Scale(from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command = self.change, fg = "#ff0000", border = 2)
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = tk.Scale(from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command = self.change, fg = "#00ff00", border = 2)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB = tk.Scale(from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command = self.change, fg = "#0000ff", border = 2)
        self.scaleB.pack()
        
        self.canvasmain = tk.Canvas(width=255, height=255, background="#000000")
        self.canvasmain.pack()

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasmain.config(background=f"#{r:02x}{g:02x}{b:02x}")

    def quit(self, event = None):
        super().quit()

    def random(self, event = None):
        r = self.scaleR.set(random.randint(1, 255))
        g = self.scaleG.set(random.randint(1, 255))
        b = self.scaleB.set(random.randint(1, 255))

app = Appka()
app.mainloop()
