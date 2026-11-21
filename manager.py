from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add(self, title):
        task = Task(len(self.tasks) + 1, title)
        self.tasks.append(task)
        return task

    

