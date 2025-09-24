#example 1
class Order:
  global_discount = 10  # percentage

  @classmethod
  def apply_global_discount(cls, new_discount): 
    cls.global_discount = new_discount
   
# Testing the class method    
Order.apply_global_discount(15)  
print(Order.global_discount)

#example 2
class Date:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day
  
  @classmethod
  def date_from_string(cls, date_str):
    year, month, day = map(int, date_str.split('-'))
    return cls(year, month, day)
  
d1 = Date(2025, 9, 9)
d2 = Date.date_from_string("2025-09-09")

# Testing the class method
print("d1: ", d1.year, d1.month, d1.day)
print("d2: ", d2.year, d2.month, d2.day)