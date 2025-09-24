import random
from collections import defaultdict
# Example 1 - using if conditional
my_list = ['col', 'mex', 'test']
my_dict = {random.randint(1,10): value for value in my_list}
print(my_dict)

# Example 2 - using if conditional
text = 'Hola, soy Nicolas'
vowels = 'aeiou'
new_dict = defaultdict(int) 

for value in text:
  if value.lower() in vowels:  
    new_dict[value.lower()] += 1
print(new_dict)

new_short_dict = {value: text.lower().count(value) for value in text if value in vowels}
print(new_short_dict)

# Example 3 - using short if conditional