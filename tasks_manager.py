import json

# --------- Task ---------
class Task:
    def __init__(self, title: str, priority: int, status="todo"):
        self.title = title
        self.priority = priority
        self.status = status

    def __str__(self):
        return f'[{self.status}] ({self.priority}) {self.title}'

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        return Task(
            title=data["title"],
            priority=data["priority"],
            status=data["status"]
        )

# --------- TaskManager ---------
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Такой задачи не существует")

    def show_tasks(self, status=None):
        tasks_to_show = self.tasks if status is None else [
            task for task in self.tasks if task.status == status
        ]

        if not tasks_to_show:
            print("Нет задач с таким статусом")
        else:
            print("\n".join(str(task) for task in tasks_to_show))

    def sort_by_priority(self):
        self.tasks.sort(key=lambda t: t.priority)
        print("Список отсортирован по приоритету.")

    def save_to_json(self, filename="tasks.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)
        print("Задачи сохранены в JSON")

    def load_from_json(self, filename="tasks.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(obj) for obj in data]
            print("Задачи загружены из JSON")
        except FileNotFoundError:
            print("Файл не найден, создаём пустой список задач")
            self.tasks = []

    def __len__(self):
        return len(self.tasks)

# --------- Пример использования ---------
tm = TaskManager()

tm.add_task(Task("Сделать урок по Python", 2))
tm.add_task(Task("Пройти тест по ООП", 1))

tm.save_to_json()

tm2 = TaskManager()
tm2.load_from_json()

tm2.show_tasks()