# to_do_list_manager_main.py
from to_do_list_manager import add_tasks, tasks, view_tasks
menu = """
        To-Do List Manager
        1. Add a task
        2. View all tasks
        3. Mark a task as complete
        4. Delete a task
        5. Exit
	   """
while True:
        print(menu)
        userInput = input("Choose an option: ").strip()

        if userInput == '1':
            add_tasks(choice)
        elif choice == '2':
            view_tasks(tasks)
        
		 