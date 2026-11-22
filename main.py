from manager import TaskManager, TaskNotFoundError


MENU = """
TaskFlow — Task menu
1) Create a task
2) Show all tasks
3) Mark a task complete
4) Remove a task
5) Save and exit
"""


def add_task(manager):
    title = input("Enter a title: ").strip()
    if not title:
        print("Please provide a task title.")
        return False
    task = manager.add(title)
    print(f"Created task #{task.id}: {task.title}")
    return True


def show_tasks(manager):
    tasks = manager.list()
    if not tasks:
        print("Your task list is empty.")
    for task in tasks:
        status = "done" if task.done else "pending"
        print(f"#{task.id} [{status}] {task.title}")
    return False


def update_task(manager, action):
    try:
        task_id = int(input("Enter the task ID: "))
    except ValueError:
        print("Task IDs must be whole numbers.")
        return False
    if task_id < 1:
        print("Task IDs must be positive.")
        return False
    try:
        if action == "complete":
            manager.complete(task_id)
            print(f"Task #{task_id} marked complete.")
        else:
            manager.delete(task_id)
            print(f"Removed task #{task_id}.")
    except TaskNotFoundError as error:
        print(error)
        return False
    return True


def main():
    manager = TaskManager()
    actions = {
        "1": lambda: add_task(manager),
        "2": lambda: show_tasks(manager),
        "3": lambda: update_task(manager, "complete"),
        "4": lambda: update_task(manager, "delete"),
    }

    while True:
        print(MENU)
        choice = input("Select 1–5: ").strip()
        if choice == "5":
            print("See you next time!")
            break
        action = actions.get(choice)
        if action is None:
            print("Choose a menu number from 1 to 5.")
            continue
        action()


if __name__ == "__main__":
    main()
