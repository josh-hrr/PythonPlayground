# does not need the close()
# only read only rights by default = 'r'
'''
with open('text.txt') as file:
  for line in file:
    print(line)
    #file.write('this is a new line')
'''

# read + write = r+ 
# concat the new line at the end of the last line of text of the file
with open('text2.txt', 'r+') as file: 
  for line in file:
    print(line)
  file.write('\nr+ line')


''' 
# read + write = w+
# write = w
# override content
with open('text2.txt', 'w+') as file: 
  for line in file:
    print(line)
  file.write('\nw+ line') 
''' 
