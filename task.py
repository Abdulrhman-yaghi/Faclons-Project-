from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    done: bool = False

    def mark_done(self):
        self.done = True

    