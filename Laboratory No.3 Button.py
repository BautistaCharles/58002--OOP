from tkinter import *

class MyWindow:
    def __init__(self, win):

        self.txt1 = Label(win, text="Charles Babbage", foreground='red', background='blue')
        self.txt1.place(x=50, y=50)
        self.btn1 = Button(win, text="<---Click to change the color of the button", command=self.change_color)
        self.btn1.place(x=150, y=47)

    def change_color(self):
        self.txt1.config(background='yellow')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x200")
window.title("Button")
window.mainloop()