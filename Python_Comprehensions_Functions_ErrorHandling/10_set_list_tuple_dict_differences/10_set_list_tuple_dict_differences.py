'''
---------------------
Set: crud operations

YES mutable
NO ordered
NO idexed
NO duplicate values

.add('value')
for value in set
.update( { })
.remove('value')

---------------------
'''

my_set = {'col', 'mex', 'bol'}
my_set.add('gt')
for country in my_set:
    print(country)
my_set.update({'ar', 'mex', 'gt'})
my_set.remove('col')
print(my_set)




'''
List: crud operations

YES mutable
YES ordered
YES indexed
YES duplicate values

.append('value')
for value in list
list[index] = 'new_value'
.pop()

'''
print('--------------------- list ')
my_list = ['col', 'mex', 'bol']
print(my_list[0])
my_list.append('gt')
for country in my_list:
    print(country)
my_list[0] = 'arg'
my_list.pop() # removes the last value
print(my_list)


'''
---------------------

Tuple: crud operations

NO mutable
YES ordered
YES indexed
YES duplicate values

- cannot be changed (immutable)
tuple[index]
- cannot be changed (immutable)
del tuple     - but cannot delete a specific value



'''

my_tuple = (1, 2, 3, 4, 5, 5, 4) 
print(my_tuple)
print(my_tuple[0])   

'''
---------------------
Dict: crud operations

YES mutable
NO ordered (as of Python 3.7+ insertion ordered)
YES indexed by keys
YES duplicate values (by values, not by keys)

dict['key'] = 'value'
for key, value in dict
dict['key'] = 'new_value'
del dict['key']


'''