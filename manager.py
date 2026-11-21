from task import Task


class TaskNotFoundError(Exception):
    pass


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def find(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError("Task not found")

    def list(self):
        return self.tasks

    

