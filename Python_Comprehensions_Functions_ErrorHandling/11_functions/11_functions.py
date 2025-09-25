'''

design principles that make code more readable and maintainable.

DRY: Don't Repeat Yourself
KISS: Keep It Simple, Stupid
YAGNI: You Aren't Gonna Need It
SOLID


'''

# without Return, no value is returned. 
# it returns None. 
# Cannot be reused.

print("----- without Return -----")
def test():
  print("this is a test")
test()
print(test())

# with Return, a value is returned. 
# it can be reused.

print("----- with Return -----")
def testTwo():
  return "this is a test" 
testTwo()
result = testTwo()
print(result) 

# tuple is returned if multiple values are returned.
print("----- with multiple Return values -----")
def testThree(my_str="default", my_int=5, my_list=None):
  return "test", my_int, my_list
storing_str, storing_int, storing_list = testThree()
print(storing_str, storing_int, storing_list)