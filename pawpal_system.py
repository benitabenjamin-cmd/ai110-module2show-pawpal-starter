from dataclasses import dataclass
from typing import List

# Represents a pet
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = None

    def __post_init__(self):
        """Initialize the tasks list if not provided."""
        if self.tasks is None:
            self.tasks = []

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_pet_info(self):
        """Return a string describing the pet."""
        return f"{self.name} ({self.species}, {self.age} yrs)"


# Represents a pet care task
@dataclass
class Task:
    name: str
    duration: int
    priority: int
    category: str
    completed: bool = False

    def get_task_details(self):
        """Return a string describing the task."""
        status = "Done" if self.completed else "Pending"
        return f"{self.name} ({self.category}, {self.duration} min, priority {self.priority}, {status})"


# Represents the pet owner
class Owner:
    ...
    def add_pet(self, pet: Pet):
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str):
        """Remove a pet from the owner's pet list by name."""
        self.pets = [p for p in self.pets if p.name != pet_name]

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks across all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


# Responsible for scheduling
class Scheduler:
    ...
    def sort_tasks_by_priority(self):
        """Sort the owner's tasks in descending order of priority."""
        self.tasks.sort(key=lambda t: t.priority, reverse=True)

    def generate_daily_plan(self) -> List[Task]:
        """Return a daily plan of tasks that fit within available time."""
        self.sort_tasks_by_priority()
        plan = []
        total_time = 0
        for task in self.tasks:
            if not task.completed and total_time + task.duration <= self.available_time:
                plan.append(task)
                total_time += task.duration
        return plan

    def mark_task_complete(self, task_name: str):
        """Mark a task as completed by name."""
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                break