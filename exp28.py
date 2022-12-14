from tkinter import *

root = Tk()

Label(root,text="first variable").grid(row=0,column=0)
Label(root,text="second variable").grid(row=1,column=0)

label3 = Label(root).grid(row = 3, column= 1)

num1 = IntVar()
num2 = IntVar()

first = Entry(root,textvariable=num1).grid(row = 0, column= 1)
second = Entry(root,textvariable=num2).grid(row = 1, column= 1)

def add():
    s = num1.get() + num2.get()
    label3.config("the result is",str(s))

but = Button(root,text="calculate",command=add).grid(row = 1, column= 3)

root.mainloop()




