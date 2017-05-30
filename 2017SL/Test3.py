from tkinter import *
window = Tk()

class rendertext:
    def helloCallBack(self):
        self.txt.insert(END, "lol")

    def init_ui(self):
        self.txt = Text(window, width=24, height=10)
        self.txt.grid(column=0, row=0)

        load_button = Button(window, text="Load Wave Data", command=self.helloCallBack)
        load_button.grid(column=1, row=0, sticky="E")

window = rendertext()

init_ui(window)
helloCallBack(window)