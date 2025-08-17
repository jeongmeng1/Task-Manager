from Task import Task
import tkinter as tk
from datetime import datetime, timedelta

class TaskManager:
    def __init__(self):
        self.listtasks = []

    def add(self):
        #Temporary questions
        duration = input("\nHow long is your task? ")
        duedate = input("When is your task due?(MM-DD-YYYY) ")
        priority = input("How important is your task? ")
        description = input("Whats the name of your task?")

        #Set duetime due to list being needed
        duetime = [5, 10]
        curTask = Task(description, duration, duedate, priority, duetime)

        #Appending to list
        self.listtasks.append(curTask)

    def sortbydate(self):
        n = len(self.listtasks)

        for i in range(n):
            swapped = False

            for j in range (0, n-i-1):
                
                if (self.listtasks[j].duedate > self.listtasks[j+1].duedate):
                    self.listtasks[j], self.listtasks[j+1] = self.listtasks[j+1], self.listtasks[j]
                    swapped = True
                elif(self.listtasks[j].duedate == self.listtasks[j+1].duedate):
                    if (self.listtasks[j].priority > self.listtasks[j+1].priority):
                        self.listtasks[j], self.listtasks[j+1] = self.listtasks[j+1], self.listtasks[j]
                        swapped = True
            if (swapped == False):
                break






taskMgr = TaskManager()


#Dummy tasks for testing
taskMgr.listtasks.append(Task("Item A", 60, "04-20-2025", 5, [1, 34]))
taskMgr.listtasks.append(Task("Item B", 60, "04-20-2025", 2, [1, 34]))
taskMgr.listtasks.append(Task("Item C", 60, "04-20-2025", 1, [1, 34]))
taskMgr.listtasks.append(Task("Item D", 60, "04-20-2025", 3, [1, 34]))
taskMgr.listtasks.append(Task("Item E", 60, "04-20-2025", 2, [1, 34]))

taskMgr.sortbydate()

print(taskMgr.listtasks)






        
