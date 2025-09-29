'''

creates the new file, it fails if it already exists.

'''

with open('text.txt', 'x') as file:
  file.write("testing")