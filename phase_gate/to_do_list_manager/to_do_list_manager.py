# to_do_list_manager.py

tasks = []

def add_tasks(task):
    task = {"task": task, "completed": False}
         
    if not task:
        raise ValueError("Numeric value only cannot be entered or tasks can't be an empty field.")
        
    elif task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")
        
    return tasks
    raise ValueError
    
def add_tasks_input(task):
    task = input("Enter a new task: ").lower()
        
def view_tasks(task):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
def mark_a_task_as_complete(task):
    view_tasks(task)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if task_number > 0 and task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def remove_tasks(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

    
            
         