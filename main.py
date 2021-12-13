from os.path import basename, splitext
import tkinter as tk
import random
from tkinter.constants import COMMAND

class Appka(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Udělátko"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.bind("<r>", self.random)
        self.varR = tk.StringVar()
        self.varG = tk.StringVar()
        self.varB = tk.StringVar()


        self.frameR = tk.Frame(self)
        self.frameR.pack()
        self.lblR = tk.Label(self.frameR, text = "R",fg = "#000000")
        self.lblR.pack(side = tk.LEFT, anchor = tk.S)
        self.scaleR = tk.Scale(self.frameR, from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command = self.change, fg = "#ff0000", border = 2, variable = self.varR)
        self.scaleR.pack(side = tk.LEFT, anchor = tk.S)
        self.entryR = tk.Entry(self.frameR, width = 3, textvariable = self.varR)
        self.entryR.pack(side = tk.LEFT, anchor = tk.S)

        self.frameG = tk.Frame(self)
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text = "G")
        self.lblG.pack(side = tk.LEFT, anchor = tk.S)
        self.scaleG = tk.Scale(self.frameG, from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command = self.change, fg = "#00ff00", border = 2, variable = self.varG)
        self.scaleG.pack(side = tk.LEFT, anchor = tk.S)
        self.entryG = tk.Entry(self.frameG, width = 3, textvariable = self.varG)
        self.entryG.pack(side = tk.LEFT, anchor = tk.S)

        self.frameB = tk.Frame(self)
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text = "B")
        self.lblB.pack(side = tk.LEFT, anchor = tk.S)
        self.scaleB = tk.Scale(self.frameB, from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, command = self.change, fg = "#0000ff", border = 2, variable = self.varB)
        self.scaleB.pack(side = tk.LEFT, anchor = tk.S)
        self.entryB = tk.Entry(self.frameB, width = 3, textvariable = self.varB)
        self.entryB.pack(side = tk.LEFT, anchor = tk.S)
        
        self.canvasmain = tk.Canvas(width = 255, height = 255, background = "#000000")
        self.canvasmain.pack()

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)
        self.canvasmain.config(background = f"#{r:02x}{g:02x}{b:02x}")


    def quit(self, event = None):
        super().quit()

    def random(self, event = None):
        self.scaleR.set(random.randint(1, 255))
        self.scaleG.set(random.randint(1, 255))
        self.scaleB.set(random.randint(1, 255))

app = Appka()
app.mainloop()
