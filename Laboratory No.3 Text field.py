from tkinter import *

class MyWindow:
    def __init__(self,win):

        self.txt = Entry(win,bd=1,width=30)
        self.txt.place(x=50,y=50)

window = Tk()
mywin = MyWindow(window)
window.geometry("300x150")
window.title("Text field")
window.mainloop()