import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# ---------------------------
# Page config and title
# ---------------------------
st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ app.

Plan your pet care tasks and generate a daily schedule based on priorities and available time.
"""
)

# ---------------------------
# Scenario & instructions
# ---------------------------
with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** helps a pet owner plan care tasks for their pet(s)
based on constraints like time, priority, and preferences.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, duration, priority)
- Represent pets and the owner (basic info)
- Build a daily plan respecting constraints
- Explain the plan to the user
"""
    )

st.divider()

# ---------------------------
# Quick Demo Inputs
# ---------------------------
st.subheader("Owner & Pet Info")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# Initialize Owner in session_state
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name, available_time=120)

# Add Pet button
if st.button("Add Pet"):
    new_pet = Pet(name=pet_name, species=species, age=1)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added pet: {pet_name}")

# Show current pets
if st.session_state.owner.pets:
    st.markdown("**Current Pets:**")
    for pet in st.session_state.owner.pets:
        st.write(f"- {pet.name} ({pet.species}, {pet.age} yrs)")
else:
    st.info("No pets yet. Add one above.")

st.divider()

# ---------------------------
# Add Tasks
# ---------------------------
st.subheader("Add Tasks")

if st.session_state.owner.pets:
    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    # Select pet to assign task
    pet_names = [pet.name for pet in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Assign to Pet", pet_names)

    if st.button("Add Task to Pet"):
        new_task = Task(
            name=task_title,
            duration=int(duration),
            priority={"low": 3, "medium": 6, "high": 10}[priority],
            category="General"
        )
        # Add task to the selected pet
        pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet_name)
        pet.add_task(new_task)
        st.success(f"Added task '{task_title}' to {selected_pet_name}")

    # Show tasks per pet
    for pet in st.session_state.owner.pets:
        if pet.tasks:
            st.markdown(f"**Tasks for {pet.name}:**")
            for t in pet.tasks:
                st.write(f"- {t.get_task_details()}")
        else:
            st.info(f"No tasks for {pet.name} yet.")
else:
    st.info("Add a pet first to assign tasks.")

st.divider()

# ---------------------------
# Generate Daily Schedule
# ---------------------------
st.subheader("Build Today's Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler(st.session_state.owner)
    daily_plan = scheduler.generate_daily_plan()

    if daily_plan:
        st.markdown(f"### Today's Schedule for {st.session_state.owner.name}")
        for i, task in enumerate(daily_plan, start=1):
            pet_name = next(p.name for p in st.session_state.owner.pets if task in p.tasks)
            st.write(f"{i}. {task.get_task_details()} (Pet: {pet_name})")
    else:
        st.info("No tasks to schedule or time exceeded available time.")