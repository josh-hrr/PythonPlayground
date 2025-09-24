class Employee:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary  # Protected attribute

  @property   # getter
  def salary_method(self):
    return self._salary
  
  @salary_method.setter   # setter
  def salary_method(self, value):
    if value < 0:
      raise ValueError("Salary cannot be negative.")
    self._salary = value

  @salary_method.deleter  # deleter
  def salary_method(self):
    print(f"The salary of {self.name} has been deleted.")
    del self._salary

emp = Employee("Alice", 50000)
emp.salary_method = 600     #using setter
print(emp.salary_method)    #using getter

del emp.salary_method       #using deleter




