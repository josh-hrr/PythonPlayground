'''
transform a given list

'''

list_1 = ['cow', 'chicken', 'corn', 'potato']
#list = [🍔, 🍗, 🍿, 🍟]
list_v2 = [] 
for i in list_1:
  list_v2.append(i * 2) 
print(list_v2)

#using map + lambda
list_v3 = map(lambda i : i * 2, list_1)
print(list(list_v3))
