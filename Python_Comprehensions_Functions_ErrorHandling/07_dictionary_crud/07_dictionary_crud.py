my_dict = {
    "name": "Alice", 
    "age": 30
  }

# Create - key-value pair 
my_dict['city'] = 'GT'
print(my_dict)

# Read - .get() or square brackets
print(my_dict.get('name'))
print(my_dict['name'])

# Read - .keys()
print(my_dict.keys())

# Read - .values()
print(my_dict.values())

# Read - .items() - all key-value pairs
print(my_dict.items())

# Update - reassigment
my_dict["age"] = 31
print(my_dict)

# Update - .update()
my_dict.update({
  "city": "London",
  "role": "Engineer"
  })
print(my_dict)

# delete - del
del my_dict["role"]
print(my_dict)

# delete - pop(key)
my_dict.pop('age')
print(my_dict)

# delete - popitem() - removes the last inserted key-value pair
print(my_dict.popitem())