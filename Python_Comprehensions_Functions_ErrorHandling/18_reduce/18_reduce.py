import functools

'''

reduces the list into 0
reduce only returns a value, no need to cast into list.
prev = accum, starts at 0 value


'''
numbers = [1, 2, 3, 4]
result = functools.reduce(lambda prev, item: prev + item, numbers)
print(result)

#def 
def accum(prev, item):
  return prev + item

result_two = functools.reduce(accum, numbers)
print(result_two)