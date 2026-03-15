# main.py - CLI demo for PawPal+
from pawpal_system import Owner, Pet, Task, Scheduler

# --------------------------
# Create Owner
# --------------------------
owner = Owner("Lily", available_time=120)  # 2 hours available

# --------------------------
# Create Pets
# --------------------------
dog = Pet("Buddy", "Dog", 3)
cat = Pet("Whiskers", "Cat", 2)

# --------------------------
# Add Tasks to Pets
# --------------------------
dog.add_task(Task("Feed Buddy", 10, 10, "Feeding"))
dog.add_task(Task("Walk Buddy", 30, 5, "Exercise"))
cat.add_task(Task("Feed Whiskers", 5, 10, "Feeding"))
cat.add_task(Task("Play with Whiskers", 20, 6, "Enrichment"))

# --------------------------
# Add Pets to Owner
# --------------------------
owner.add_pet(dog)
owner.add_pet(cat)

# --------------------------
# Create Scheduler
# --------------------------
scheduler = Scheduler(owner)

# --------------------------
# Generate Daily Plan
# --------------------------
daily_plan = scheduler.generate_daily_plan()

# --------------------------
# Print Schedule Clearly
# --------------------------
print("\nToday's Schedule for", owner.name)
print("="*40)
for i, task in enumerate(daily_plan, start=1):
    print(f"{i}. {task.get_task_details()}")
print("="*40)



# Sort and filter tasks
scheduler.sort_tasks_by_time()
print("Sorted tasks by time:")
for t in scheduler.tasks:
    print(t.get_task_details())

# Filter only pending tasks for a specific pet
pending_buddy_tasks = scheduler.filter_tasks(pet_name="Buddy", completed=False)
print("\nPending tasks for Buddy:")
for t in pending_buddy_tasks:
    print(t.get_task_details())

# Detect conflicts
conflicts = scheduler.detect_conflicts()
for c in conflicts:
    print("⚠️", c)