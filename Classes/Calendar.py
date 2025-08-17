import tkinter as tk
from datetime import datetime, timedelta
from taskmanager import taskMgr

# Example tasks
tasks = [
    {
        "Task Name": "Item A",
        "Due Date": "2025-04-20 01:34:00",
        "Duration": 60,
        "Priority": 1
    },
    {
        "Task Name": "Item B",
        "Due Date": "2025-04-22 14:00:00",
        "Duration": 120,
        "Priority": 2
    },
    {
        "Task Name": "Item C",
        "Due Date": "2025-04-25 09:00:00",
        "Duration": 90,
        "Priority": 1
    },
    {
        "Task Name": "Item D",
        "Due Date": "2025-04-29 10:00:00",
        "Duration": 45,
        "Priority": 3
    },
    {
        "Task Name": "Item E",
        "Due Date": "2025-05-03 15:30:00",
        "Duration": 30,
        "Priority": 2
    }
]

print(type(taskMgr.listtasks))

# Priority colors
priority_colors = {
    1: "#ff4c4c",  # red for highest priority
    2: "#ffa64c",  # orange for medium
    3: "#4cafff"   # blue for low
}

class CalendarApp(tk.Tk):
    def __init__(self, tasks):
        super().__init__()
        self.title("Task Calendar")
        self.geometry("1100x700")
        self.configure(bg="white")

        self.tasks = [self.parse_task(t) for t in tasks]
        
        self.start_date = self.get_week_start(datetime(2025, 4, 20))  # Default week

        self.create_widgets()
        self.populate_tasks()

    def parse_task(self, task):
        task["Due Date"] = datetime.strptime(task["Due Date"], "%Y-%m-%d %H:%M:%S")
        return task

    def get_week_start(self, date):
        # Move back to Sunday
        return date - timedelta(days=date.weekday() + 1) if date.weekday() != 6 else date

    def create_widgets(self):
        # Navigation Buttons
        nav_frame = tk.Frame(self, bg="white")
        nav_frame.pack(fill="x", pady=10)

        prev_btn = tk.Button(nav_frame, text="<< Previous Week", command=self.prev_week)
        prev_btn.pack(side="left", padx=10)

        self.week_label = tk.Label(nav_frame, text="", font=("Arial", 14, "bold"), bg="white")
        self.week_label.pack(side="left", expand=True)

        next_btn = tk.Button(nav_frame, text="Next Week >>", command=self.next_week)
        next_btn.pack(side="right", padx=10)

        # Calendar grid
        self.calendar_frame = tk.Frame(self, bg="white")
        self.calendar_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Header Row: Days
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i, day in enumerate(days):
            label = tk.Label(self.calendar_frame, text=day, bg="lightgray", font=("Arial", 12, "bold"))
            label.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)
            self.calendar_frame.columnconfigure(i, weight=1)

        # Create frames for each day
        self.day_frames = {}
        for i in range(7):
            frame = tk.Frame(self.calendar_frame, bg="white", bd=1, relief="solid")
            frame.grid(row=1, column=i, sticky="nsew", padx=1, pady=1)
            self.day_frames[i] = frame

    def clear_tasks(self):
        for frame in self.day_frames.values():
            for widget in frame.winfo_children():
                widget.destroy()

    def populate_tasks(self):
        self.clear_tasks()
        week_start = self.start_date
        week_end = week_start + timedelta(days=6)

        self.week_label.config(
            text=f"Week: {week_start.strftime('%Y-%m-%d')} - {week_end.strftime('%Y-%m-%d')}"
        )

        for task in self.tasks:
            day_index = (task["Due Date"].date() - self.start_date.date()).days
            if 0 <= day_index < 7:
                frame = self.day_frames[day_index]
                self.add_task_widget(frame, task)

    def add_task_widget(self, parent, task):
        color = priority_colors.get(task["Priority"], "#cccccc")

        base_height_per_minute = 1  # 1 pixel per minute
        height = max(30, task["Duration"] * base_height_per_minute)

        task_frame = tk.Frame(parent, bg=color, bd=2, relief="raised", height=height)
        task_frame.pack(fill="x", pady=5, padx=5)
        task_frame.pack_propagate(False)

        name_label = tk.Label(task_frame, text=task["Task Name"], bg=color, font=("Arial", 10, "bold"))
        name_label.pack(anchor="w")

        time_label = tk.Label(task_frame,
                              text=task["Due Date"].strftime("%H:%M") + f" ({task['Duration']} min)",
                              bg=color,
                              font=("Arial", 8))
        time_label.pack(anchor="w")

    def next_week(self):
        self.start_date += timedelta(days=7)
        self.populate_tasks()

    def prev_week(self):
        self.start_date -= timedelta(days=7)
        self.populate_tasks()

if __name__ == "__main__":
    app = CalendarApp(tasks)
    app.mainloop()

print(taskMgr.listtasks)