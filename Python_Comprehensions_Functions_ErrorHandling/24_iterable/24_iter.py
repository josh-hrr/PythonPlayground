'''
my_iter = range(1, 11, 2)

for value in my_iter:
  print(value)
''' 

# Range: datatype that creates a iterable on demand.
# iter(): creates a iterator object
#  -----> receives iterable: list, tuple, object, strings, dict

# next(): navigates manually to next iteration


my_iter_v2 = iter(range(1,11))
print(my_iter_v2)
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2)) 
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2))
print(next(my_iter_v2))