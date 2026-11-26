class Task:
    def __init__(self,
                title:str,
                description:str,
                due_date:str|None=None)->None:
        self.title=title
        self.description=description
        self.due_date=due_date
        self.is_completed=False

    def mark_completed(self)->None:
        self.is_completed=True

    def update_due_date(self,new_date:str|None)->None:
        self.due_date=new_date

    def display_info(self)->None:
        status = "Completed" if self.is_completed else "Pending"

        print("Task info: ")
        print("Title: ",self.title)
        print("Description: ",self.description)
        print("Due Date: ",self.due_date)
        print("Completion Status:", status)


class TaskManager:
    def __init__(self)->None:
        self.tasks:list[Task]=[]

    def add_task(self,task:Task)->None:
        self.tasks.append(task)

    def find_task(self,title:str)->Task|None:
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    @staticmethod
    def is_task_completed(task:Task)->bool:
        return task.is_completed

    def get_completed_tasks(self)->list[Task]:
        completed_tasks:list[Task]=[]
        for task in self.tasks:
            if TaskManager.is_task_completed(task):
                completed_tasks.append(task)
        return completed_tasks

    def get_pending_tasks(self) -> list[Task]:
        pending_tasks: list[Task] = []
        for task in self.tasks:
            if not TaskManager.is_task_completed(task):
                pending_tasks.append(task)
    
        return pending_tasks


    
# Create tasks
task1 = Task("Study Python", "Revise OOP", "2026-11-30")
task2 = Task("Practice DSA", "Solve problems")
task3 = Task("Study ML", "Revise Linear Regression")

# Create TaskManager
manager = TaskManager()

# Add tasks
manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)

# Complete some tasks
task1.mark_completed()
task3.mark_completed()

# Display all tasks
for task in manager.tasks:
    task.display_info()

# Find a task
found_task = manager.find_task("Study Python")
print(found_task.title if found_task else None)

# Search for a non-existing task
print(manager.find_task("Learn C++"))

# Get completed and pending tasks
completed = manager.get_completed_tasks()
pending = manager.get_pending_tasks()

print("Completed Tasks:")
for task in completed:
    print(task.title)

print("Pending Tasks:")
for task in pending:
    print(task.title)

# Update due date
task2.update_due_date("2026-12-05")
task2.display_info()


