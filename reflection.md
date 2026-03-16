# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The initial design comprises four main classes: Owner, Pet, Task, and Scheduler. 
- The Owner class manages pet owners' information, including their name, available time, and lists of pets and tasks. 
- The Pet class stores details about pets, such as name, species, and age, and features a method for retrieving pet information. 
- The Task class represents pet care activities, containing details like name, duration, priority, and category, with a method for retrieving task information. 
- The Scheduler class generates daily plans based on available tasks and the owner's time, including methods for sorting tasks by priority and creating a schedule.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.


I converted Pet and Task into Python dataclasses to simplify initialization and reduce boilerplate code.

I clarified that Scheduler should handle all scheduling logic instead of putting any of it in the Owner class. This separation makes the design cleaner and easier to maintain.

Added task conflict detection, sorting by priority/time, and recurring task logic, which were not in the original UML.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers:
Owner available time – the total minutes the owner can spend on tasks in a day.
Task priority – higher-priority tasks are scheduled first.
Task duration – ensures tasks fit within the owner's available time.
Recurring tasks – daily or weekly tasks are automatically rescheduled.
Conflict detection – avoids scheduling two tasks at the same time for the same pet.

I prioritized time and priority because the owner’s availability is the hard limit, and urgent/high-priority tasks should be done first.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler checks conflicts only for tasks with the exact same start time, rather than detecting overlapping durations.
This simplifies the algorithm and covers most common cases while keeping the system fast and understandable. More complex overlap detection could be added in future iterations.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

Brainstorming: Generated UML design ideas and class responsibilities.
Copilot helped write Python class stubs for Owner, Pet, Task, and Scheduler.Copilot suggested ways to sort, filter, and detect conflicts.
Copilot provided  ways to simplify loops and lambda functions.

Used prompts like "use this description and make a UML design" and "check this function and see if it matches the description and the design".

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

Copilot suggested storing scheduling logic inside the Owner class. I rejected this and kept all scheduling inside the Scheduler class for cleaner separation of responsibilities.
I reviewed the design and verified that keeping the Owner class focused on data management, while the Scheduler handles task planning, made the system more modular and maintainable.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

Task Completion: Marking a task complete updates its status correctly.
Task Addition: Adding a task to a Pet increases the task list correctly.
Sorting: Scheduler returns tasks sorted by priority and duration.
Recurring Tasks: Completing a daily task automatically creates the next day's task.
Conflict Detection: Scheduler flags duplicate task times.

These tests ensure the core features behave correctly and help prevent regressions as the project grows.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

Confidence level: ★★★★★ (5/5)

Edge cases for future testing:
- A pet with no tasks.
- Tasks with overlapping durations, not just identical times.
- Adding multiple pets and verifying combined scheduling.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The system works end-to-end: tasks can be added, scheduled, and displayed in the Streamlit UI.
Task sorting, conflict detection, and recurring task automation work correctly.
Using Copilot saved time writing code while still allowing me to guide the design.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

Implement time overlap detection for tasks.
Enhance UI explanations, e.g., showing why a task was skipped if it didn’t fit in available time.
Allow custom recurring intervals beyond daily/weekly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

Being the “lead architect” while collaborating with AI requires careful judgment: you need to decide which AI suggestions to adopt or reject.