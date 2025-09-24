'''

delete repeated elements from four sets

'''

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

# new_set = countries.union(northAm, centralAm, southAm)
# Escribe tu solución 👇  

#alternative using pipe |
new_set_two = countries | northAm | centralAm | southAm

print(new_set_two) # pass