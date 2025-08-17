from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("CALENDAR")
root.geometry("500x1000")
my_date = tb.DateEntry(root,bootstyle = "danger")
my_date.pack(pady=50)

name_label = tb.label = tb.Label(root,text = "Enter Task Name: ")
name_label.pack(side = "left")
name_widget = tb.Entry(root)
name_widget.pack(pady = 20)

date_label = tb.label = tb.Label(root,text = "Enter when the task is due (hrs-min-DD-MM-YYYY): ")
date_label.pack(pady = 50)
due_widget = tb.Entry(root)
due_widget.pack(pady = 20)

duration_label = tb.label = tb.Label(root,text = "Enter How Long The Task Takes: ")
duration_label.pack(pady = 50)
duration_widget = tb.Entry()
duration_widget.pack(pady = 20)




def speak():
    my_label.config(text=f"You Entered: {rawDate_entry.get()}")

rawDate_label = tb.label = tb.Label(root,text = "Enter How Long The Task Takes: ")
rawDate_label.pack(pady = 50)
rawDate_entry = tb.Entry(root)
rawDate_entry.pack(pady=50)

mybutton = tb.Button(root,bootstyle="danger outline",text="Enter",command = speak)
mybutton.pack(pady = 50)

my_label = tb.Label(root,text="")
my_label.pack(pady=50)

root.mainloop()

import datetime

def date_entry():
    while True:
        while True:
            rawDate = input("Enter when the task is due (hrs-min-DD-MM-YYYY): ")
            try:
                hrs, min, day, month, year = rawDate.split("-")
            except ValueError:
                print("Incorrect date. Use the [hrs-min-DD-MM-YYYY] format")
                continue
            break
        try:
            dueDate = datetime.datetime(int(year), int(month), int(day), int(hrs), int(min))
        except:
            print("Date is incorrect. Please try again.")
            continue
        break
    return dueDate


class Task:
    def __init__(self):
        self.name = input("Task name: ")
        self.dueDate = date_entry()
        self.priority = input("Enter the priority(High/Med/Low): ")



task1 = Task()
print(task1.name)
print(task1.dueDate)