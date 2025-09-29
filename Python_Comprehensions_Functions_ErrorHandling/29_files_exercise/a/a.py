# a = append

'''

creates the file if it does not exists.
If exists, adds the new line at the end.

'''

with open('text.txt', 'a') as file:
  file.write('\nthis is a test')