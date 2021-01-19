from tkinter import *


def add():
    n1 = e1.get()
    n2 = e2.get()
    Label(root, text="Answer is " + str(float(n1) + float(n2))).grid(row=5)


def subtract():
    n1 = e1.get()
    n2 = e2.get()
    Label(root, text="Answer is " + str(float(n1) - float(n2))).grid(row=5)


def multi():
    n1 = e1.get()
    n2 = e2.get()
    Label(root, text="Answer is " + str(float(n1) * float(n2))).grid(row=5)


def divide():
    n1 = e1.get()
    n2 = e2.get()
    Label(root, text="Answer is " + str(float(n1) / float(n2))).grid(row=5)


root = Tk()
Label(root, text="Input number for do operation").grid(row=0)
e1 = Entry(root)
e2 = Entry(root)
Label(root, text="Select operation").grid(row=3)
add_button = Button(root, text=' + ',
                    command=add).grid(row=4, column=0)
subtract_button = Button(root, text=' - ',
                         command=subtract).grid(row=4, column=1)
multi_button = Button(root, text=' * ',
                      command=multi).grid(row=4, column=2)
divide_button = Button(root, text=' / ',
                       command=divide).grid(row=4, column=3)
e1.grid(row=1)
e2.grid(row=2)
root.mainloop()
