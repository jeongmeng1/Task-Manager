from datetime import datetime
class Task:
    def __init__(self, description, duration, duedate, priority, duetime):
        """
        duedate -> MM-DD-YYYY
        dueTime -> [HH, MM]
        descriptio -> String
        priority -> INT
        duration -> INT      
        """
        duedateSplit = duedate.split("-")   
        self.description = description
        self.duration = duration
        self.duedate = datetime(int(duedateSplit[2]), int(duedateSplit[0]), int(duedateSplit[1]), int(duetime[0]), int(duetime[1]))
        self.priority = priority
    
    def __repr__(self):
        return f"\nTask Name: {self.description}\nDue Date: {self.duedate}\nDuration: {self.duration} min\nPriority: {self.priority}\n"



