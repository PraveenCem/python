'''
    A simple TO-DO LIST program
    which let's user to 
        1. Add Task
        2. View Tasks
        3. Complete Task
        4. Delete Task
'''

def to_do_list():
    menu_items = (  '1. Add Task',
                    '2. View Tasks',
                    '3. Complete Task',
                    '4. Delete Task',
                    '5. Exit'
                )
    tasks = {}
    task_id = 0
    print('***** TO-DO LIST PROGRAM *****')
    while True:
        for menu in menu_items:
            print(menu)
        print('-----'*3)
        choice = input('Please enter your choice: ')
        
        match choice:
            case '1': 
                task = input('Please enter you task: ')
                tasks[task_id] = {
                            'task':task,
                            'completed': False
                        }
                task_id += 1
            case '2':
                if not tasks:
                    print('No tasks available to display!')
                else:
                    print('*****'*3)
                    print('LIST')
                    for current_id,details in tasks.items():
                        status = 'completed' if details['completed'] else 'pending'
                        print(f"{current_id}.{details['task']} - {status}")
                    print('*****'*3)
            case '3':
                if not tasks:
                    print('No tasks available to display!')
                    continue
                while True:
                    try:
                        selected_id  = int(input('Please enter you task task_id: '))
                        if selected_id  in tasks:
                            if tasks[selected_id ]['completed']:
                                print('Task is already completed')
                                break
                            else:
                                tasks[selected_id ]['completed'] = True
                                print('Task completed successfully!')
                                break
                        else:
                            print('Task does not exist!')
                    except ValueError:
                        print('Please enter a valid Task ID. ')
            case '4':
                if not tasks:
                    print('No tasks available!')
                    continue
                else:
                    while True:
                        try:
                            selected_id  = int(input('Please enter your task task_id: '))
                            if selected_id  in tasks:
                                tasks.pop(selected_id )
                                print('Task deleted successfully!')
                                break
                            else:
                                print('Task does not exist!')
                        except ValueError:
                            print('Please enter a valid Task ID.')
            case '5':
                print('Thank you for using!')
                break
            case _:
                print('Invalid choice')
                continue


##################### CALL TO_DO_LIST PROGRAM

to_do_list()