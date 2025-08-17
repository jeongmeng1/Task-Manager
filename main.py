# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font, messagebox
import ttkbootstrap as tb
from ttkbootstrap.tooltip import ToolTip
import calendar
from datetime import datetime, timedelta, date
import os
import ast

# --- Main Application Window ---
root = tb.Window(themename="flatly")
root.title("Taskly")
root.geometry("700x700")
root.resizable(False, False)

# --- Fonts ---
titleFont = font.Font(family='Montserrat', size=28, weight='bold')
labelFont = font.Font(family='Montserrat', size=12, weight='normal')

# Fallback if Montserrat is not available
try:
    font.netamtofont('Montserrat')
except Exception:
    titleFont = font.Font(family='Arial', size=28, weight='bold')
    labelFont = font.Font(family='Arial', size=12, weight='normal')

# --- Task Storage ---
tasks = []
# Load previous entries from last_task.txt if it exists
if os.path.exists("last_task.txt"):
    with open("last_task.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    task = ast.literal_eval(line)
                    tasks.append(task)
                except Exception:
                    pass

# --- Status Bar ---
status_var = StringVar(value="Welcome to Taskly!")
status_bar = tb.Label(root, textvariable=status_var, bootstyle="secondary inverse", anchor=W, padding=8)
status_bar.pack(side=BOTTOM, fill=X)

# --- Menu Bar ---
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Taskly\nA modern task calendar app."))
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# --- Title in a Card-like Frame ---
title_frame = tb.Frame(root, bootstyle="info", padding=(20, 10), borderwidth=0)
title_frame.pack(pady=(18, 8), padx=0, fill=X)
tb.Label(title_frame, text="Taskly", font=titleFont, bootstyle="info inverse").pack(anchor=CENTER)

# --- Notebook (Tabs) ---
notebook = tb.Notebook(root, bootstyle="info")
notebook.pack(fill="both", expand=True, padx=0, pady=0)

# --- Tabs ---
tab1 = tb.Frame(notebook, padding=0)
tab2 = tb.Frame(notebook, padding=0)
tab3 = tb.Frame(notebook, padding=0)
notebook.add(tab1, text="Home")
notebook.add(tab2, text="Tasks")
notebook.add(tab3, text="Settings")

# --- Home Tab ---
# Dynamically set the form_container style based on the current theme

def get_form_container_style():
    theme = root.style.theme.name
    if theme == "cyborg":  # Pitch Dark
        return {
            "bootstyle": "dark",
            "padding": (30, 18, 30, 18),
            "borderwidth": 0,
            "relief": "flat"
        }
    elif theme == "darkly":  # Dark
        return {
            "bootstyle": "dark",
            "padding": (30, 18, 30, 18),
            "borderwidth": 0,
            "relief": "flat"
        }
    else:  # Light
        return {
            "bootstyle": "light",
            "padding": (30, 18, 30, 18),
            "borderwidth": 0,
            "relief": "flat"
        }

form_container = tb.Frame(tab1, **get_form_container_style())
form_container.pack(pady=(30, 0), padx=40, fill=None, anchor=CENTER)

form = tb.Frame(form_container)
form.pack()

def update_form_bg():
    pass  # No-op for compatibility

def update_form_container_style():
    style = get_form_container_style()
    form_container.configure(**{k: v for k, v in style.items() if k != 'padding'})
    form_container['padding'] = style['padding']

# Use grid for perfect alignment
row = 0
# Due Date
label_due = tb.Label(form, text="Due Date", font=labelFont, width=16, anchor=E)
label_due.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
my_date = tb.DateEntry(form, bootstyle="info", width=16)
my_date.grid(row=row, column=1, columnspan=2, sticky=W+E, pady=8)
ToolTip(my_date, text="Select the due date for your task.")

row += 1
# Due Time
label_time = tb.Label(form, text="Due Time (Hr:Min)", font=labelFont, width=16, anchor=E)
label_time.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
time_frame = tb.Frame(form)
time_frame.grid(row=row, column=1, columnspan=2, sticky=W, pady=8)
hourValue = tb.StringVar()
hrbox = tb.Combobox(time_frame, textvariable=hourValue, width=6, bootstyle="info")
hrbox['values'] = [f"{i:02d}" for i in range(24)]
hrbox.pack(side=LEFT, padx=(0,5))
minValue = tb.StringVar()
minbox = tb.Combobox(time_frame, textvariable=minValue, width=6, bootstyle="info")
minbox['values'] = [f"{i:02d}" for i in range(60)]
minbox.pack(side=LEFT)
ToolTip(hrbox, text="Select the hour (00-23)")
ToolTip(minbox, text="Select the minute (00-59)")

row += 1
# Task Name
label_name = tb.Label(form, text="Task Name", font=labelFont, width=16, anchor=E)
label_name.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
name_widget = tb.Entry(form, bootstyle="info", width=20)
name_widget.grid(row=row, column=1, columnspan=2, sticky=W+E, pady=8)
ToolTip(name_widget, text="Enter the name of your task.")

row += 1
# Task Duration
label_dur = tb.Label(form, text="Duration (Hr:Min)", font=labelFont, width=16, anchor=E)
label_dur.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
dur_frame = tb.Frame(form)
dur_frame.grid(row=row, column=1, columnspan=2, sticky=W, pady=8)
hourDuration = tb.StringVar()
hrDuration = tb.Combobox(dur_frame, textvariable=hourDuration, width=6, bootstyle="info")
hrDuration['values'] = [f"{i:02d}" for i in range(24)]
hrDuration.pack(side=LEFT, padx=(0,5))
minDur = tb.StringVar()
minDuration = tb.Combobox(dur_frame, textvariable=minDur, width=6, bootstyle="info")
minDuration['values'] = [f"{i:02d}" for i in range(60)]
minDuration.pack(side=LEFT)
ToolTip(hrDuration, text="Duration hours (00-23)")
ToolTip(minDuration, text="Duration minutes (00-59)")

row += 1
# Task Priority
label_pri = tb.Label(form, text="Priority", font=labelFont, width=16, anchor=E)
label_pri.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
prioritystuff = tb.StringVar()
priority = tb.Combobox(form, textvariable=prioritystuff, width=16, bootstyle="warning")
priority['values'] = ["Low", "Med", "High"]
priority.grid(row=row, column=1, columnspan=2, sticky=W+E, pady=8)
ToolTip(priority, text="Select the priority of your task.")

# --- Enter Button ---
def add_task():
    dueDate = my_date.entry.get()
    duehr = hrbox.get()
    duemin = minbox.get()
    desc = name_widget.get()
    durationhr = hrDuration.get()
    durationmin = minDuration.get()
    priorities = priority.get()
    if not (desc and dueDate and duehr and duemin and durationhr and durationmin and priorities):
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return
    task = {
        "name": desc,
        "due_date": dueDate,
        "due_time": f"{duehr.zfill(2)}:{duemin.zfill(2)}",
        "duration": f"{durationhr.zfill(2)}:{durationmin.zfill(2)}",
        "priority": priorities,
        "status": "Pending"
    }
    tasks.append(task)
    # Append the new task to the text file with a new line
    with open("last_task.txt", "a", encoding="utf-8") as f:
        f.write(str(task) + "\n")
    refresh_tasks()
    name_widget.delete(0, END)
    hrbox.set("")
    minbox.set("")
    hrDuration.set("")
    minDuration.set("")
    priority.set("")
    status_var.set("Task added.")

# Make the button fill the width of the form_container and add more vertical space
btn_frame = tb.Frame(form_container, bootstyle="light")
btn_frame.pack(pady=(18, 0), fill=X)
tb.Button(
    btn_frame,
    text="Add Task",
    command=add_task,
    bootstyle="success",
    width=1,  # width is ignored when fill=X
    padding=10
).pack(fill=X, padx=0)

# --- Clear Database Button ---
clear_db_frame = tb.Frame(form_container, bootstyle="light")
clear_db_frame.pack(pady=(6, 0))

def clear_database():
    with open("last_task.txt", "w", encoding="utf-8") as f:
        f.write("")
    status_var.set("Database cleared.")

tb.Button(
    clear_db_frame,
    text="Clear Database",
    command=clear_database,
    bootstyle="danger",
    width=18,
    padding=6
).pack()

# --- Tasks Tab: Treeview for displaying tasks ---
columns = ("Task Name", "Due Date", "Due Time", "Duration", "Priority", "Status")
task_tree = tb.Treeview(tab2, columns=columns, show="headings", bootstyle="info")
for col in columns:
    task_tree.heading(col, text=col)
    task_tree.column(col, anchor=CENTER, width=110)
task_tree.pack(fill=BOTH, expand=True, pady=18, padx=18)

def refresh_tasks():
    # Configure lighter pastel tag colors
    task_tree.tag_configure('high', background='#ffe5e5')  # lighter pastel red
    task_tree.tag_configure('med', background='#fff2cc')   # lighter pastel orange/yellow
    task_tree.tag_configure('low', background='#e5ffe5')   # lighter pastel green
    task_tree.tag_configure('completed', background='#ffffff')  # white for completed tasks
    
    for row in task_tree.get_children():
        task_tree.delete(row)
    for i, task in enumerate(tasks):
        # Determine which tag to use based on priority or completion
        tag = 'completed' if task["status"].lower() == 'completed' else task["priority"].lower()
        task_tree.insert("", END, iid=i, values=(
            task["name"],
            task["due_date"],
            task["due_time"],
            task["duration"],
            task["priority"],
            task["status"]
        ), tags=(tag,))  # Apply the appropriate tag
    status_var.set(f"{len(tasks)} task(s) loaded.")

def delete_task():
    selected = task_tree.selection()
    if not selected:
        messagebox.showinfo("Delete Task", "Please select a task to delete.")
        return
    idx = int(selected[0])
    if messagebox.askyesno("Delete Task", f"Delete task '{tasks[idx]['name']}'?"):
        del tasks[idx]
        refresh_tasks()
        status_var.set("Task deleted.")

def mark_complete():
    selected = task_tree.selection()
    if not selected:
        messagebox.showinfo("Mark Complete", "Please select a task to mark as complete.")
        return
    idx = int(selected[0])
    tasks[idx]["status"] = "Completed"
    refresh_tasks()
    status_var.set("Task marked as completed.")

def on_tree_double_click(event):
    selected = task_tree.selection()
    if not selected:
        return
    idx = int(selected[0])
    task = tasks[idx]
    messagebox.showinfo(
        "Task Details",
        f"Name: {task['name']}\nDue: {task['due_date']} {task['due_time']}\nDuration: {task['duration']}\nPriority: {task['priority']}\nStatus: {task['status']}"
    )

task_tree.bind("<Double-1>", on_tree_double_click)

# --- Task Action Buttons ---
action_frame = tb.Frame(tab2, bootstyle="light")
action_frame.pack(pady=10)
tb.Button(action_frame, text="Delete Task", command=delete_task, bootstyle="danger", width=14, padding=5).pack(side=LEFT, padx=10)
tb.Button(action_frame, text="Mark Complete", command=mark_complete, bootstyle="success", width=14, padding=5).pack(side=LEFT, padx=10)

# --- Settings Tab: Theme Selector ---
# Only show three themes: pitch dark, dark, and light
THEMES = [
    ("Pitch Dark", "cyborg"),   # pitch dark
    ("Dark", "darkly"),         # dark
    ("Light", "flatly")         # light
]

def change_theme(event):
    selected_label = theme_combo.get()
    for label, theme in THEMES:
        if label == selected_label:
            root.style.theme_use(theme)
            status_var.set(f"Theme changed to {label}.")
            update_form_container_style()
            update_form_bg()
            break

tb.Label(tab3, text="Select Theme:", font=labelFont).pack(pady=(18, 5))
theme_combo = tb.Combobox(tab3, values=[label for label, _ in THEMES], width=20, bootstyle="info")
theme_combo.set(THEMES[2][0])  # Default to Light
root.style.theme_use(THEMES[2][1])
theme_combo.pack(pady=8)
theme_combo.bind("<<ComboboxSelected>>", change_theme)

# --- Reload tasks function ---
def reload_tasks_from_file():
    tasks.clear()
    if os.path.exists("last_task.txt"):
        with open("last_task.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        task = ast.literal_eval(line)
                        tasks.append(task)
                    except Exception:
                        pass

def on_tab_changed(event):
    if notebook.index(notebook.select()) == 1:  # Tasks tab index
        reload_tasks_from_file()
        refresh_tasks()

notebook.bind("<<NotebookTabChanged>>", on_tab_changed)

# --- Run the app ---
refresh_tasks()
root.mainloop()
