from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add(self, title):
        task = Task(len(self.tasks) + 1, title)
        self.tasks.append(task)
        return task

    def find(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError("Task not found")



    


class TaskNotFoundError(Exception):
    pass