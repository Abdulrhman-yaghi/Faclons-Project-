# TaskFlow

TaskFlow is a Python console application for managing everyday tasks. You can create tasks, view their status, mark them complete, and delete them. Tasks are saved locally so you can continue where you left off.

## Getting started

Install Python 3.7 or newer. The project uses only the Python standard library, so no additional packages are required.

Download or clone this repository, then open a terminal in the project folder. Start the application with:

```console
python main.py
```

If your system uses `python3` instead of `python`, use that command for both the application and the tests.

## Using the menu

Enter `1` to create a task, then type its title. Leading and trailing spaces are removed. Empty titles are rejected.

Enter `2` to show all tasks. Each entry includes its ID, title, and either `pending` or `done`. An empty list displays a message.

Enter `3` to mark a task complete. Provide the ID shown in the task list.

Enter `4` to delete a task by ID. Deletion happens immediately without a confirmation prompt.

Enter `5` to save and exit.

Task IDs must be positive whole numbers. Invalid menu choices, invalid IDs, and missing tasks produce a message and return you to the menu.

## Saving and loading

The application reads `tasks.json` when it starts. If the file does not exist, it begins with an empty list. Successful additions, completions, and deletions are saved immediately. Exiting through the menu also saves the current list.

The data file is created in the terminal's current working directory. Run the application from the same folder each time to load the same tasks.

Each saved task contains an integer `id`, a string `title`, and a boolean `done` value. For example:

```json
[
  {
    "id": 1,
    "title": "Review project notes",
    "done": false
  }
]
```

At startup, the next task ID is set to one greater than the highest saved ID. This avoids duplicating IDs of existing tasks after a restart.

If loading encounters invalid JSON or a task constructor type error, storage moves the file to `tasks.backup.json` and starts with an empty list. This recovery does not cover every possible data or filesystem error. An existing backup can be replaced by a later recovery.

## Project files

`main.py` provides the menu, validates user input, connects the manager to storage, and restores the task ID counter.

`manager.py` defines `TaskManager`, which adds, finds, lists, completes, and deletes tasks. It raises `TaskNotFoundError` when a requested task does not exist.

`task.py` defines the `Task` data class with its ID, title, and completion state. Its `mark_done()` method marks a task complete.

`storage.py` defines `Storage`, which reads and writes task data as JSON. Its constructor accepts an optional filename and defaults to `tasks.json`.

`test_main.py` contains integration tests that run the console application in temporary folders.

`.gitignore` excludes `.env` files from Git tracking. Task data and backup files are not currently ignored automatically.

## Running tests

From the project folder, run:

```console
python test_main.py
```

The tests cover the task lifecycle, saved data across restarts, task ID allocation after loading, and invalid input. They use temporary storage and do not change your normal task data.
