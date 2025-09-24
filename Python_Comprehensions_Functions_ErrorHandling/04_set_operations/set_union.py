set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union: combines all unique elements from both sets
set_c = set_a.union(set_b)
print(set_c)

# union alternative using pipe |
set_c_alternative = set_a | set_b
print(set_c_alternative)