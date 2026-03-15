from dataclasses import dataclass
from typing import List


# Represents a pet
@dataclass
class Pet:
    name: str
    species: str
    age: int

    def get_pet_info(self):
        pass


# Represents a pet care task
@dataclass
class Task:
    name: str
    duration: int
    priority: int
    category: str

    def get_task_details(self):
        pass


# Represents the pet owner
class Owner:
    def __init__(self, name: str, available_time: int):
        self.name = name
        self.available_time = available_time
        self.pets: List[Pet] = []
        self.tasks: List[Task] = []

    def add_pet(self, pet: Pet):
        pass

    def add_task(self, task: Task):
        pass

    def remove_task(self, task_name: str):
        pass


# Responsible for creating the daily plan
class Scheduler:
    def __init__(self, tasks: List[Task], available_time: int):
        self.tasks = tasks
        self.available_time = available_time

    def sort_tasks_by_priority(self):
        pass

    def generate_daily_plan(self):
        pass