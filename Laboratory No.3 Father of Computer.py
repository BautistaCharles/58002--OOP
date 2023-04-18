from tkinter import *

class MyWindow:
    def __init__(self,win):

        self.text = Label(win, text="Charles Babbage",foreground='black', background='cyan')
        self.text.place(x=50,y=50)

window = Tk()
mywin = MyWindow(window)
window.geometry("300x150")
window.title("Father of Computer")
window.mainloop()