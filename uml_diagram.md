classDiagram

class Owner {
    name: str
    available_time: int
    pets: list
    tasks: list
    add_pet()
    add_task()
    remove_task()
}

class Pet {
    name: str
    species: str
    age: int
}

class Task {
    name: str
    duration: int
    priority: int
    category: str
}

class Scheduler {
    tasks: list
    available_time: int
    generate_daily_plan()
    sort_tasks_by_priority()
}

Owner "1" --> "*" Pet : owns
Owner "1" --> "*" Task : manages
Scheduler --> Task : schedules