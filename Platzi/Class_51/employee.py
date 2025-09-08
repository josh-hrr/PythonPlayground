# usage of *args, **kwargs
class Employee:
  def __init__(self, name, *args, **kwargs):
    self.name = name
    self.skills = args
    self.detail = kwargs

  def show_employee(self):
    print(f"Name: {self.name}")
    print(f"Skills: {self.skills}")
    print(f"Detail: {self.detail}")


employee = Employee("John", "Python", "C++", age=30, city="Cambridge")

print("employee data: ", employee.show_employee())