# creating a list from a range of numbers
numbers = []
for element in range(1, 11):
  if element % 2 == 0:
    numbers.append(element*2)
print(numbers)

# using list comprehension to create the same list
# syntax: [element for element in iterable]
numbers_two = [element for element in range(1,11)]
print(numbers_two)

# using list comprehension to create the same list + adding a condition
# syntax: [element for element in iterable if condition]  
numbers_three = [i*2 for i in range(1,101) if i % 2 == 0]
print(numbers_three)