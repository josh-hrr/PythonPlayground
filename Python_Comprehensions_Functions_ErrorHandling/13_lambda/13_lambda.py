def increment(x):
    return x + 1
result = increment(5)
print(result)

# lambda syntax
# lambda param : content
increment_lambda = lambda x : x + 1
print(increment_lambda(5))

full_name = lambda name, last_name: f'full name is {name.title()} {last_name.title()}'
my_full_name = full_name('nico', 'vega')
print(my_full_name)