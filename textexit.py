from tkinter import (
    Frame, Button, Tk, Text, Scrollbar, END
)
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Application(Frame):
    def __init__(self, master=None):
        self.root = master
        super().__init__(self.root)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.text = Text(self, height=24, width=80)
        self.scrollbar = Scrollbar(self, command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.QUIT = Button(
            self, text="QUIT", fg="red", command=self.root.destroy
        )
        self.SAVE = Button(
            self, text="SAVE", command=self.save_text
        )
        self.LOAD = Button(
            self, text="LOAD", command=self.load_text
        )

        self.QUIT.grid(row=0, column=0)
        self.SAVE.grid(row=1, column=0)
        self.LOAD.grid(row=2, column=0)
        self.text.grid(row=0, column=1, rowspan=3)
        self.scrollbar.grid(row=0, column=2, rowspan=3)

    def load_text(self):
        with open(askopenfilename()) as fd:
            self.text.delete(0.0, 'end')
            self.text.insert(END, fd.read())

    def save_text(self):
        with open(asksaveasfilename(), 'w') as fd:
            fd.write(self.text.get(1.0, END))


if __name__ == "__main__":
    Application(master=Tk()).mainloop()
