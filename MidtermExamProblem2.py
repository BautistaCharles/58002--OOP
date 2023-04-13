from tkinter import *

class MyWindow:
    def __init__(self,win):

        font = ('Verdana', 10)
        color = 'red'
        self.lbl5 = Label(win,text="My Full Name")
        self.lbl5.place(x=130,y=30)
        self.lbl5.config(font=font, fg=color)
        self.lbl1 = Label(win,text="Enter Given Name:")
        self.lbl1.place(x=50,y=50)
        self.lbl1.config(font=font, fg=color)
        self.lbl2 = Label(win, text= "Enter Middle Name:")
        self.lbl2.place(x=50,y=100)
        self.lbl2.config(font=font, fg=color)
        self.lbl3 = Label(win, text="Enter Last name:")
        self.lbl3.place(x=50,y=150)
        self.lbl3.config(font=font, fg=color)
        self.lbl4 = Label(win, text="My Full Name is:")
        self.lbl4.place(x=50,y=200)
        self.lbl4.config(font=font, fg=color)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=200,y=50)
        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=200,y=100)
        self.txt3 = Entry(win,bd=1)
        self.txt3.place(x=200,y=150)
        self.txt4 = Entry(win, bd=2)
        self.txt4.place(x=200,y=200)
        self.btnclr = Button(win,text="Clear All")
        self.btnclr.place(x=150,y=300)
        self.btnclr.bind('<Button-1>',self.clr)
        self.btnadd = Button(win,text="Show Full Name")
        self.btnadd.place(x=130,y=250)
        self.btnadd.bind('<Button-1>',self.add)


    def add(self,add):
        color = 'red'
        First = self.txt1.get()
        Middle = self.txt2.get()
        Last = self.txt3.get()
        result = f"{First} {Middle} {Last}"
        self.txt4.delete(0, END)
        self.txt4.insert(END, result)
        self.txt4.config(fg=color)


    def clr(self,Clr):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("400x400")
window.title("Midterm Exam Problem 2")
window.mainloop()