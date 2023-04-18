from tkinter import *

class MyWindow:
    def __init__(self,win):

        self.txt1 = Label(win, text="Laboratory Activity 5")
        self.txt1.place(x=50,y=50)
        self.txt2 = Label(win, text="Submitted to:Mam Sayo")
        self.txt2.place(x=50,y=70)

window = Tk()
mywin = MyWindow(window)
window.geometry("300x150")
window.title("Label")
window.mainloop()