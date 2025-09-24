my_list = [1, 2]

# Create
my_list.append(3) # adds a new item at the end
print(my_list)

my_list.insert(0, 0) # index, value
print(my_list)

my_list.extend([4,5]) # extending original list
print(my_list)

# Read
print(my_list[-1]) # reads by index

# Read - Slicing
print(my_list[1:3])

# Read - Slicing + Step
print(my_list[::2])

# Read - for _ in loop
for value in my_list:
  print(value) 

# Read Index - index() receives a value from the list as argument to retrieve its first occurrence index.
print(my_list.index(1))

# Update - reassignment by index
my_list[0] = 10
print(my_list)

# Update - Slicing
my_list[1:3] = [20, 30]
print(my_list)

# Delete - del
del my_list[0]
print(my_list)

# Delete - remove() receives a value from the list as argument, to remove it.
my_list.remove(30)
print(my_list)

# Delete - pop() receives the index as argument, to remove it, or deletes the last element from the list, and stores it.
my_list.pop()
print(my_list)

my_list.clear()
print(my_list)
