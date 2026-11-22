import json
from dataclasses import asdict
from pathlib import Path

from task import Task


class Storage:
    """Load and save tasks in a JSON file."""

    def __init__(self, filename="tasks.json"):
        self.path = Path(filename)

    def save(self, tasks):
        data = [asdict(task) for task in tasks]
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def load(self):
        if not self.path.exists():
            return []
        try:
            with open(self.path, encoding="utf-8") as file:
                data = json.load(file)
            return [Task(**item) for item in data]
        except (json.JSONDecodeError, TypeError):
            self._backup_broken_file()
            return []

    def _backup_broken_file(self):
        # Keep the broken file so its data is not lost.
        backup = self.path.with_name(self.path.stem + ".backup.json")
        self.path.replace(backup)
