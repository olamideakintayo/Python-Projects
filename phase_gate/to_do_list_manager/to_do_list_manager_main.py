# to_do_list_manager_main.py
from to_do_list_manager import tasks, add_tasks, view_tasks, add_tasks_input, mark_a_task_as_complete, remove_tasks
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
        user_input = input("Choose an option: ").strip()

        if user_input == '1':
        	add_tasks_input(tasks)
        	add_tasks(user_input)
            
        elif user_input == '2':
            view_tasks(tasks)
            
        elif user_input == '3':
        	  mark_a_task_as_complete(tasks)
        	  
        elif user_input == '4':
        	  remove_tasks(tasks)	
        	  
        elif user_input == '5':
        	  print("GoodBye!! Have a nice day!!")
        	  break
        	  
	 
	