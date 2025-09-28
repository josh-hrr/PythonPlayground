from collections import Counter

my_list = [1,2,3,4,5, 5, 5]

# counts each repetive value, creates a dict.
result = Counter(my_list) 
print(result)