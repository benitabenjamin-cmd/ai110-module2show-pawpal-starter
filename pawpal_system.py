# pawpal_system.py
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime, timedelta

# -------------------------
# Task Class
# -------------------------
@dataclass
class Task:
    name: str
    duration: int  # in minutes
    priority: int  # higher number = higher priority
    category: str
    time: Optional[str] = None  # "HH:MM" format
    completed: bool = False
    frequency: Optional[str] = None  # "daily" or "weekly"
    date: Optional[datetime] = None  # optional due date

    def mark_complete(self) -> Optional["Task"]:
        """Mark this task as complete and return a new instance if recurring."""
        self.completed = True
        if self.frequency and self.date:
            next_date = self.date + timedelta(days=1 if self.frequency == "daily" else 7)
            return Task(
                name=self.name,
                duration=self.duration,
                priority=self.priority,
                category=self.category,
                time=self.time,
                frequency=self.frequency,
                date=next_date
            )
        return None

    def get_task_details(self) -> str:
        """Return a readable string describing the task."""
        status = "Completed" if self.completed else "Pending"
        time_str = f", scheduled at {self.time}" if self.time else ""
        return f"{self.name} ({self.category}, {self.duration} min, priority {self.priority}, {status}{time_str})"

# -------------------------
# Pet Class
# -------------------------
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = None

    def __post_init__(self):
        if self.tasks is None:
            self.tasks = []

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_pet_info(self) -> str:
        """Return a readable string describing the pet."""
        return f"{self.name} ({self.species}, {self.age} yrs old)"

# -------------------------
# Owner Class
# -------------------------
class Owner:
    def __init__(self, name: str, available_time: int):
        self.name = name
        self.available_time = available_time  # total minutes available per day
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks across all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks

# -------------------------
# Scheduler Class
# -------------------------
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.tasks: List[Task] = owner.get_all_tasks()
        self.available_time = owner.available_time

    def sort_tasks_by_priority(self):
        """Sort tasks in-place by priority (highest first)."""
        self.tasks.sort(key=lambda t: t.priority, reverse=True)

    def sort_tasks_by_time(self):
        """Sort tasks by time (HH:MM). Tasks without a time come first."""
        self.tasks.sort(key=lambda t: datetime.strptime(t.time, "%H:%M") if t.time else datetime.min)

    def filter_tasks(self, pet_name: Optional[str] = None, completed: Optional[bool] = None) -> List[Task]:
        """Return a filtered list of tasks based on pet and/or completion status."""
        filtered = self.tasks
        if pet_name:
            filtered = [t for t in filtered if any(p.name == pet_name and t in p.tasks for p in self.owner.pets)]
        if completed is not None:
            filtered = [t for t in filtered if t.completed == completed]
        return filtered

    def detect_conflicts(self) -> List[str]:
        """Detect tasks that are scheduled at the same time and return warnings."""
        conflicts = []
        scheduled_times = {}
        for task in self.tasks:
            if task.time:
                key = task.time
                if key in scheduled_times:
                    conflicts.append(f"Conflict: {task.name} overlaps with {scheduled_times[key].name}")
                else:
                    scheduled_times[key] = task
        return conflicts

    def generate_daily_plan(self) -> List[Task]:
        """Generate a daily schedule based on priority and available time."""
        self.sort_tasks_by_priority()
        plan = []
        total_time = 0
        for task in self.tasks:
            if total_time + task.duration <= self.available_time and not task.completed:
                plan.append(task)
                total_time += task.duration
        return plan