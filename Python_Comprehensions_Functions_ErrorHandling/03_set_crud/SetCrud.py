'''

Important: set does not have indexes.

'''

set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print('col' in set_countries) #reading set

# create
set_countries.add('gt')
print(set_countries)

# update
'''
Note: values are inmutable, we can add more values,
but, cannot modified a specific one.
we have to delete the value we want to modify 
and, add the new value.
'''
set_countries.update({'ar', 'ecua', 'gt'})
print(set_countries)

# remove
set_countries.remove('col') 
print(set_countries)

# discard
set_countries.discard('arg') # removes, but if value does not exists, it does not show an expection
print(set_countries)

# clear all set values
set_countries.clear()
print(set_countries)
