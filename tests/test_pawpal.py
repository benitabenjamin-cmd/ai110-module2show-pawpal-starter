# tests/test_pawpal.py
import pytest
from pawpal_system import Pet, Task, Owner, Scheduler

# --------------------------
# Test 1: Task Completion
# --------------------------
def test_task_completion():
    task = Task("Feed Buddy", 10, 10, "Feeding")
    assert not task.completed  # initially pending
    task.completed = True
    assert task.completed  # should now be completed

# --------------------------
# Test 2: Task Addition to Pet
# --------------------------
def test_task_addition():
    pet = Pet("Buddy", "Dog", 3)
    assert len(pet.tasks) == 0  # initially empty
    pet.add_task(Task("Walk Buddy", 30, 5, "Exercise"))
    assert len(pet.tasks) == 1  # should now have one task