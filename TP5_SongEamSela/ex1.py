from tkinter import *
from datetime import date

now = date.today()


def calculate_age(year):
    return now.year - int(year)


def calculate_time_for_bd(day, month):
    bd = date(now.year, int(month), int(day))
    current = now

    if bd < current:
        days = current - bd
        return "Your Birthday is already passed " + str(days.days) + " days ago"
    else:
        days = bd - current
        return "There are " + str(days.days) + " left to celebrate your birthday."


def submit():
    name = e1.get()
    day = e2.get()
    month = e3.get()
    year = e4.get()

    Label(root,
          text="Hi, " + str(name) + " ! You are " + str(calculate_age(year)) + " year old." +
               calculate_time_for_bd(day, month)).grid(row=5, column=1)


root = Tk()
Label(root, text="Name").grid(row=0)
Label(root, text='Day').grid(row=1)
Label(root, text='Month').grid(row=2)
Label(root, text='Year').grid(row=3)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
sub_btn = Button(root, text='Submit',
                 command=submit)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
sub_btn.grid(row=4,column=1)
root.mainloop()
