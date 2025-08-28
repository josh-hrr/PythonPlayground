def check_access(func):
    def wrapper(employee):
        #Validate employee role = 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACCESS DENIED.')
    return wrapper

@check_access
def delete_employee(employee):
    print(f"Employee {employee['name']} has been deleted") 

admin = {
    'name': 'Carlos', 
    'role': 'admin'}

emplooyee = {
    'name': 'Ana',
    'role': 'employee'
}

delete_employee(admin)
delete_employee(emplooyee)