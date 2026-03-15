# tests/test_pawpal.py
import pytest
from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

# -------------------------
# Fixtures
# -------------------------
@pytest.fixture
def sample_owner():
    owner = Owner(name="Benita", available_time=120)
    pet1 = Pet(name="Buddy", species="dog", age=3)
    pet2 = Pet(name="Whiskers", species="cat", age=2)

    task1 = Task(name="Feed Buddy", duration=10, priority=10, category="Feeding", time="08:00")
    task2 = Task(name="Walk Buddy", duration=30, priority=5, category="Exercise", time="09:00")
    task3 = Task(name="Play with Whiskers", duration=20, priority=6, category="Enrichment", time="08:30", frequency="daily", date=datetime.today())

    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)

    owner.add_pet(pet1)
    owner.add_pet(pet2)
    return owner

# -------------------------
# Test Sorting by Time
# -------------------------
def test_sort_tasks_by_time(sample_owner):
    scheduler = Scheduler(sample_owner)
    scheduler.sort_tasks_by_time()
    times = [t.time for t in scheduler.tasks if t.time]
    assert times == sorted(times), "Tasks are not sorted by time correctly"

# -------------------------
# Test Recurring Tasks
# -------------------------
def test_recurring_task(sample_owner):
    scheduler = Scheduler(sample_owner)
    daily_task = scheduler.tasks[-1]  # Play with Whiskers
    new_task = daily_task.mark_complete()
    assert new_task is not None, "Completing a daily task should create a new task"
    assert new_task.date > daily_task.date, "The new recurring task should have a future date"

# -------------------------
# Test Conflict Detection
# -------------------------
def test_conflict_detection(sample_owner):
    # Add a conflicting task at same time as Feed Buddy
    conflict_task = Task(name="Feed Whiskers", duration=5, priority=10, category="Feeding", time="08:00")
    sample_owner.pets[1].add_task(conflict_task)

    scheduler = Scheduler(sample_owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) > 0, "Scheduler should detect conflicting tasks"

# -------------------------
# Test Adding a Task
# -------------------------
def test_add_task_to_pet(sample_owner):
    new_task = Task(name="Groom Buddy", duration=15, priority=4, category="Grooming")
    sample_owner.pets[0].add_task(new_task)
    assert new_task in sample_owner.pets[0].tasks, "Task was not added to the pet"

# -------------------------
# Test Filtering Tasks
# -------------------------
def test_filter_tasks(sample_owner):
    scheduler = Scheduler(sample_owner)
    completed_tasks = scheduler.filter_tasks(completed=True)
    pending_tasks = scheduler.filter_tasks(completed=False)
    assert all(t.completed for t in completed_tasks), "Filter by completed=True failed"
    assert all(not t.completed for t in pending_tasks), "Filter by completed=False failed"