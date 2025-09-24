'''
Datastructure

Set:

Collection of unique elements.
Does not allow duplicates.
Does not have an specific order.
Values are inmutables

do not confuse with dict. 
set does not include keys.
''' 

set_countries = { 'col', 'mex', 'bol', 'col' }
print(set_countries)
print(type(set_countries))

set_types = {1, 'hey', False, 12.2}
print(set_types)

set_from_string = set('holaaa') # creates a set from a string.
print(set_from_string)

set_from_tuple = set(('abc', 'zbc', 'bbc')) # creates a set from a tuple
print(set_from_tuple)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers) # creates a set from a list
print(set_numbers)


