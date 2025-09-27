import functools

'''

reduces the list into 0
reduce only returns a value, no need to cast into list.
counter = that accum, starting at 0 value


'''
numbers = [1, 2, 3, 4]
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

#def 
def accum(counter, item):
  return counter + item

result_two = functools.reduce(accum, numbers)
print(result_two)