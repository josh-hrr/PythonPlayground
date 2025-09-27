'''

creates a new list

'''
numbers = [1, 2, 3, 4, 5]
new_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(new_numbers)) # [2, 4]