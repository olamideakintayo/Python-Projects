# to_do_list_manager.py

tasks = []

def add_tasks(task):
    task = {"task": task}
    
    if not task:
        raise ValueError("Numeric value only cannot be entered or tasks can't be an empty field.")
        
    elif task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")
        
    return tasks
    raise ValueError
        
def view_tasks():
	return tasks