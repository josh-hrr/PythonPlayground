#keep track of every log_employee_action and store the log in a txt file

from datetime import datetime

now = datetime.now().replace(microsecond=0)

def log_employee_action(user_action):
    def wrapper(employee):
        #log any update to the employee in a txt file 
        if employee.get('name') != '': 
            with open('Platzi/Class_44/demo.txt', 'a') as f:
                f.write(f"datetime: {now} - User has made updates - user: {employee['name']}.\n")
            return user_action(employee)
        else:
            return print('The name is empty')
    return wrapper

@log_employee_action
def delete_employee(employee):
    print(f"Employee {employee['name']} has been deleted")

@log_employee_action
def update_employee_name(employee):
    print(f"Employee {employee['name']} has been updated")

@log_employee_action
def add_employee(employee):
    print(f"Employee {employee['name']} has been added")

admin = {
    'name': 'Carlos', 
    'role': 'admin'
    }

emplooyee = {
    'name': 'Ana',
    'age': 30,
    'role': 'employee',
    'department': 'IT'
    }
 
delete_employee(emplooyee)
update_employee_name(emplooyee)
add_employee(emplooyee)