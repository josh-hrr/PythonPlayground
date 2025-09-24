set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# symetric difference: keeps elements in either set_a or set_b but not in both
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# symetric difference alternative using caret ^
set_c_alternative = set_a ^ set_b
print(set_c_alternative)