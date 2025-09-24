def add_employee(employee_list, employee_name):
    """Add an employee to the employee list."""
    employee_list.append(employee_name)
    return employee_list

def remove_employee(employee_list, employee_name):
    """Remove an employee from the employee list."""
    if employee_name in employee_list:
        employee_list.remove(employee_name)
    else:
        raise ValueError(f"Employee {employee_name} not found.")
    return employee_list

def list_employees(employee_list):
    """List all employees."""
    return employee_list

if __name__ == "__main__":
    employees = []
    employees = add_employee(employees, "Alice")
    employees = add_employee(employees, "Bob")
    print("Employees after adding:", list_employees(employees))
    
    employees = remove_employee(employees, "Alice")
    print("Employees after removing Alice:", list_employees(employees))
    
    try:
        employees = remove_employee(employees, "Charlie")
    except ValueError as e:
        print(e)