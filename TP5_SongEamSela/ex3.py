from tkinter import *
import math


def submit():
    a = e1.get()
    b = e2.get()
    c = e3.get()

    delta = math.pow(float(b), 2) - (4 * float(a) * float(c))

    if delta < 0:
        Label(root, text="the equation does not have any root").grid(row=5, column=1)
    elif delta == 0:
        x = - float(b) / (2 * float(a))
        Label(root, text="the equation has the same root : x = " + str(x)).grid(row=5, column=1)
    else:
        x1 = (- float(b) - math.sqrt(delta)) / (2 * float(a))
        x2 = (- float(b) + math.sqrt(delta)) / (2 * float(a))
        Label(root, text="the equation have root x1 = " + str(x1) + ", x2 = " + str(x2)).grid(row=5, column=1)


root = Tk()

Label(root, text='Input a, b, c as the constant of equation ax^2 + bx + c = 0').grid(row=0, column=1)
Label(root, text='a :').grid(row=1)
Label(root, text='b :').grid(row=2)
Label(root, text='c :').grid(row=3)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
sub_btn = Button(root, text='Submit',command=submit)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
sub_btn.grid(row=4, column=1)

root.mainloop()
