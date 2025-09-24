# Example of dictionary without comprehension v1
my_dict = {}
for i in range(1, 11):
  my_dict[i] = i * 2 
print(my_dict)

# Example of dictionary with comprehension v1
dict_comp = {i: i * 2 for i in range(1, 11)}
print(dict_comp)

# Another example of dictionary without comprehension v2
import random
countries = ['col', 'mex', 'bol', 'pe'] 
population = {} 
for country in countries: 
  population[country] = random.randint(1, 100) 
print(population)

# Another example of dictionary with comprehension v2
population_comp = { country: random.randint(1, 100) for country in countries }
print(population_comp)

# Example of dictionary without comprehension v3
names = ['nico', 'zule', 'santi']
ages = [12, 1, 98]
print(list(zip(names, ages)))

# Example of dictionary with comprehension v3
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

# Example of dictionary with comprehension v4 (conditional)
new_dict_conditional = {name: age for (name, age) in zip(names, ages) if name == 'santi'}
print(new_dict_conditional)

