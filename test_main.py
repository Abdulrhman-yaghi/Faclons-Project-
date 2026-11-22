import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ENTRY_POINT = Path(__file__).with_name("main.py")


class TaskMenuTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.saved_tasks = Path(self.directory.name) / "tasks.json"

    def run_menu(self, *answers):
        result = subprocess.run(
            [sys.executable, "-B", str(ENTRY_POINT)],
            input="\n".join(answers) + "\n",
            text=True,
            encoding="utf-8",
            capture_output=True,
            cwd=self.directory.name,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_task_lifecycle_and_restart(self):
        output = self.run_menu("2", "1", "  Write notes  ", "3", "1", "2", "5")
        self.assertIn("Your task list is empty.", output)
        self.assertIn("#1 [done] Write notes", output)
        self.assertEqual(json.loads(self.saved_tasks.read_text()), [
            {"id": 1, "title": "Write notes", "done": True},
        ])

        output = self.run_menu("1", "Review notes", "4", "1", "2", "5")
        self.assertIn("#2 [pending] Review notes", output)
        self.assertEqual(json.loads(self.saved_tasks.read_text()), [
            {"id": 2, "title": "Review notes", "done": False},
        ])

    def test_invalid_input_does_not_change_saved_tasks(self):
        output = self.run_menu(
            "9", "1", "   ", "3", "abc", "4", "0", "3", "99", "4", "99", "5",
        )
        self.assertIn("Choose a menu number from 1 to 5.", output)
        self.assertIn("Please provide a task title.", output)
        self.assertIn("Task IDs must be whole numbers.", output)
        self.assertIn("Task IDs must be positive.", output)
        self.assertEqual(output.count("Task not found"), 2)
        self.assertEqual(json.loads(self.saved_tasks.read_text()), [])


if __name__ == "__main__":
    unittest.main()
