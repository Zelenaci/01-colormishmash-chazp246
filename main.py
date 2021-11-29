from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk what???


class Appka(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.quit)
        self.btn2.pack()


    def quit(self, event=None):
        super().quit()


app = Appka()
app.mainloop()
